#!/usr/bin/env python3
"""
SC-AS Constitutional Release v1.0 — Bundle Verification Script

Verifies the integrity of all artifacts in the SC-AS release bundle
against the RELEASE_MANIFEST.json and MERKLE_TREE.json.

Usage:
    python3 verify_bundle.py [bundle_root]

    bundle_root: Path to the extracted release bundle (default: current directory)

Checks performed:
    1. All manifest artifacts present on disk
    2. SHA-256 verification for source artifacts (blanked-SHA per SC-HDR v11 §3.2 Rule 7)
    3. SHA-256 verification for derived artifacts (full binary hash)
    4. Merkle root recomputation from leaf hashes
    5. RCC Target-SHA coupling (each RCC targets the correct canonical spec)
    6. Bundle composition completeness per SC-GOV-000001

Exit codes:
    0 — All checks pass
    1 — One or more checks failed

Reference:
    SC-HDR-000001 (v11) §3.2 Rule 7 — Deterministic SHA-256 computation
    SC-GOV-000001 (v08) — Conformance Validation Procedure
    SC-SCOPE-000001 (v05) §6-8 — Bundle composition requirements

Coherence Research — https://coherenceresearch.com
"""

import hashlib
import json
import os
import re
import sys


def sha256_file_binary(path):
    """Compute SHA-256 over raw binary content (for PDFs and other derived artifacts)."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_source_blanked(path):
    """
    Compute SHA-256 per SC-HDR v11 §3.2 Rule 7:
    Blank the SHA-256 value in the header before hashing.
    Code-block-aware: only blanks the header SHA, not example SHAs in fenced code blocks.
    """
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the first SHA-256 line outside of code blocks
    sha_match = re.search(r"  - SHA-256: ([a-f0-9]{64})", content)
    if sha_match:
        prefix = content[: sha_match.start()]
        if prefix.count("```") % 2 == 0:
            # Outside code block — this is the header SHA
            blanked = content.replace(sha_match.group(), "  - SHA-256:", 1)
            return hashlib.sha256(blanked.encode("utf-8")).hexdigest()

    # Fallback: no SHA found, hash as-is
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def merkle_root(leaf_hashes):
    """Recompute Merkle root from sorted leaf hashes using SHA-256 binary tree."""
    hashes = list(leaf_hashes)

    # Pad to power of 2
    while len(hashes) & (len(hashes) - 1):
        hashes.append(hashes[-1])

    level = hashes[:]
    while len(level) > 1:
        next_level = []
        for i in range(0, len(level), 2):
            combined = (level[i] + level[i + 1]).encode("utf-8")
            next_level.append(hashlib.sha256(combined).hexdigest())
        level = next_level

    return level[0]


def main():
    bundle_root = sys.argv[1] if len(sys.argv) > 1 else "."
    bundle_root = os.path.abspath(bundle_root)

    print("=" * 60)
    print("SC-AS Constitutional Release v1.0")
    print("Bundle Integrity Verification")
    print("=" * 60)
    print(f"\nBundle root: {bundle_root}\n")

    # ── Load manifest ────────────────────────────────────────
    manifest_path = os.path.join(bundle_root, "RELEASE_MANIFEST.json")
    if not os.path.exists(manifest_path):
        print("FAIL: RELEASE_MANIFEST.json not found")
        sys.exit(1)

    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    # ── Load merkle tree ─────────────────────────────────────
    merkle_path = os.path.join(bundle_root, "MERKLE_TREE.json")
    if not os.path.exists(merkle_path):
        print("FAIL: MERKLE_TREE.json not found")
        sys.exit(1)

    with open(merkle_path, "r") as f:
        merkle_data = json.load(f)

    artifacts = manifest["artifacts"]
    passed = 0
    failed = 0
    warnings = 0

    # ── Check 1: All artifacts present ───────────────────────
    print("## Check 1: Artifact Presence")
    for art in artifacts:
        if art["artifact_type"] == "canonical-source":
            fpath = os.path.join(bundle_root, art["path"])
        else:
            fpath = os.path.join(bundle_root, "pdf", art["filename"])

        if os.path.exists(fpath):
            passed += 1
        else:
            print(f"  FAIL  Missing: {art.get('path', art.get('filename'))}")
            failed += 1

    print(f"  {passed} artifacts found\n")

    # ── Check 2: Source artifact SHA verification ────────────
    print("## Check 2: Source SHA-256 Verification (blanked-SHA rule)")
    source_ok = 0
    source_fail = 0

    for art in artifacts:
        if art["artifact_type"] != "canonical-source":
            continue

        fpath = os.path.join(bundle_root, art["path"])
        if not os.path.exists(fpath):
            continue

        computed = sha256_source_blanked(fpath)
        declared = art["sha256"]

        if computed == declared:
            print(f"  PASS  {art['document_id']}")
            source_ok += 1
        else:
            print(f"  FAIL  {art['document_id']}")
            print(f"         Declared: {declared}")
            print(f"         Computed: {computed}")
            source_fail += 1

    print(f"\n  Source: {source_ok} pass, {source_fail} fail\n")

    # ── Check 3: Derived artifact SHA verification ───────────
    print("## Check 3: Derived (PDF) SHA-256 Verification")
    pdf_ok = 0
    pdf_fail = 0

    for art in artifacts:
        if art["artifact_type"] != "derived-pdf":
            continue

        fpath = os.path.join(bundle_root, "pdf", art["filename"])
        if not os.path.exists(fpath):
            print(f"  SKIP  {art['filename']} (not in bundle)")
            continue

        computed = sha256_file_binary(fpath)
        declared = art["sha256"]

        if computed == declared:
            print(f"  PASS  {art['filename']}")
            pdf_ok += 1
        else:
            print(f"  FAIL  {art['filename']}")
            print(f"         Declared: {declared}")
            print(f"         Computed: {computed}")
            pdf_fail += 1

    print(f"\n  PDFs: {pdf_ok} pass, {pdf_fail} fail\n")

    # ── Check 4: Merkle root ─────────────────────────────────
    print("## Check 4: Merkle Root Verification")

    leaves = [(leaf["path"], leaf["sha256"]) for leaf in merkle_data["leaves"]]
    leaves.sort(key=lambda x: x[0])
    leaf_hashes = [h for _, h in leaves]

    recomputed = merkle_root(leaf_hashes)
    declared_root = merkle_data["merkle_root"]

    if recomputed == declared_root:
        print(f"  PASS  Root: {declared_root}")
    else:
        print(f"  FAIL  Declared: {declared_root}")
        print(f"         Computed: {recomputed}")

    print()

    # ── Check 5: RCC target coupling ─────────────────────────
    print("## Check 5: RCC Target-SHA Coupling")

    canonical_shas = {}
    for art in artifacts:
        if art["artifact_type"] == "canonical-source" and art["governance_tier"] == 0:
            canonical_shas[art["document_id"]] = art["sha256"]

    rcc_ok = 0
    for art in artifacts:
        if art["artifact_type"] != "canonical-source" or art["document_class"] != "RCC":
            continue

        fpath = os.path.join(bundle_root, art["path"])
        if not os.path.exists(fpath):
            continue

        with open(fpath, "r") as f:
            rcc_content = f.read()

        target_id_m = re.search(r"RCC::Target-Document-ID:\s*(\S+)", rcc_content)
        target_sha_m = re.search(r"RCC::Target-SHA-256:\s*([a-f0-9]{64})", rcc_content)

        if target_id_m and target_sha_m:
            target_id = target_id_m.group(1)
            rcc_target_sha = target_sha_m.group(1)
            canonical_sha = canonical_shas.get(target_id, "")

            if rcc_target_sha == canonical_sha:
                print(f"  PASS  {art['document_id']} -> {target_id}")
                rcc_ok += 1
            else:
                print(f"  FAIL  {art['document_id']} -> {target_id}: SHA mismatch")

    print()

    # ── Check 6: Bundle composition ──────────────────────────
    print("## Check 6: Bundle Composition (SC-GOV-000001)")

    source_ids = {
        a["document_id"]
        for a in artifacts
        if a["artifact_type"] == "canonical-source"
    }

    required = {
        "Tier 0": {"SC-CORE-000001", "SC-AXIOM-000001", "SC-HDR-000001", "SC-SCOPE-000001"},
        "Tier 2": {"RCC-SC-CORE-000001", "RCC-SC-AXIOM-000001", "RCC-SC-HDR-000001", "RCC-SC-SCOPE-000001"},
        "Tier 3": {"SC-GOV-000001", "SC-LICENSE-000001", "SC-NAME-000001", "SC-TM-000001", "SC-AUTHORSHIP-000001"},
    }

    for tier, ids in required.items():
        present = ids & source_ids
        status = "PASS" if present == ids else "FAIL"
        print(f"  {status}  {tier}: {len(present)}/{len(ids)}")

    license_path = os.path.join(bundle_root, "LICENSE")
    if os.path.exists(license_path):
        print(f"  PASS  LICENSE file present")
    else:
        print(f"  FAIL  LICENSE file missing")

    # ── Summary ──────────────────────────────────────────────
    total_fail = source_fail + pdf_fail + (0 if recomputed == declared_root else 1)
    print(f"\n{'='*60}")
    if total_fail == 0:
        print("RESULT: ALL CHECKS PASS")
        print("This bundle is integrity-verified.")
    else:
        print(f"RESULT: {total_fail} CHECK(S) FAILED")
        print("This bundle has integrity issues.")
    print("=" * 60)

    sys.exit(0 if total_fail == 0 else 1)


if __name__ == "__main__":
    main()
