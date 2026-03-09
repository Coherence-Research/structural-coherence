# Release Verification — SC-AS v1.0

This document explains how to verify the integrity and authenticity of the SC-AS v1.0 release.

## Step 1 — File Integrity

Verify each file's SHA-256 hash against `RELEASE_MANIFEST.json`:

```bash
sha256sum -c <(jq -r '.artifacts[] | "\(.sha256)  \(.filename)"' RELEASE_MANIFEST.json)
```

## Step 2 — Merkle Tree Integrity

Verify that `MERKLE_ROOT.txt` matches the root computed from `MERKLE_TREE.json`:

```bash
# Recompute the Merkle root from the leaf hashes in MERKLE_TREE.json
# and compare against the value in MERKLE_ROOT.txt
```

## Step 3 — PGP Signature

Verify the PGP signature over the Merkle root:

```bash
gpg --verify SIGNATURE.asc MERKLE_ROOT.txt
```

The signing key fingerprint is published in `SC-AUTHORSHIP-000001`.

## Step 4 — DOI Resolution

Confirm the DOI resolves to the archived Zenodo snapshot:

```
DOI: [TO BE POPULATED]
Zenodo URL: [TO BE POPULATED]
```

The Zenodo archive is an immutable snapshot of this release.

## Step 5 — Header Conformance

Each specification document contains a Canonical Document Header (per SC-HDR-000001).
The header is the authoritative source of identity — not the filename.

---

© 2026 Coherence Research
