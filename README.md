# Structural Coherence — Anchor Specification (SC-AS)

**A universal structural specification for coherent systems.**

Published by [Coherence Research](https://coherenceresearch.com)

---

## What is SC-AS?

The Structural Coherence — Anchor Specification defines the minimal, self-contained structural foundation from which coherent configurations can be recognized, validated, and maintained across any domain.

It is not a framework, methodology, or toolkit. It is a **specification** — a set of structural axioms and constraints that any coherent system must satisfy.

## Canonical Set

The SC-AS canonical specification consists of exactly four documents:

| Document | Purpose |
|---|---|
| **SC-CORE-000001** | Core structural specification |
| **SC-AXIOM-000001** | Axiomatic foundations |
| **SC-HDR-000001** | Canonical document header schema |
| **SC-SCOPE-000001** | Scope and admissibility boundary |

This set is **closed** — no external document may extend, override, or enter the canonical set.

## Companion Documents

The release includes stewardship artifacts that support the ecosystem but do not alter canonical meaning:

- **SC-GOV-000001** — Governance and versioning (non-normative)
- **SC-LICENSE-000001** — License terms (CC BY-ND 4.0)
- **SC-TM-000001** — Trademark policy
- **SC-NAME-000001** — Naming and claims policy
- **SC-AUTHORSHIP-000001** — Authorship declaration

## Releases

Each release is a deterministic, integrity-verified bundle:

- Structured export bundle with SHA-256 hashes
- Knowledge bundle for ingestion systems
- Merkle tree integrity verification
- PGP-signed root hash
- DOI-registered archival snapshot (Zenodo)

See [`SC-AS/v1.0/`](SC-AS/v1.0/) for the current release.

## License

SC-AS specification text is released under [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/).

This license governs text redistribution. It does **not** restrict independent implementation.
Anyone may build systems that conform to SC-AS without permission or license.

See [SC-LICENSE-000001](SC-AS/v1.0/specs/SC-LICENSE-000001.md) and [TRADEMARK_POLICY](SC-AS/v1.0/specs/SC-TM-000001.md) for full terms.

## Verification

To verify a release:
1. Check file hashes against `RELEASE_MANIFEST.json`
2. Verify Merkle root against `MERKLE_TREE.json` and `MERKLE_ROOT.txt`
3. Verify PGP signature: `gpg --verify SIGNATURE.asc MERKLE_ROOT.txt`
4. Confirm DOI resolves to the archived Zenodo snapshot

See [`VERIFICATION.md`](SC-AS/v1.0/VERIFICATION.md) for detailed instructions.

---

© 2026 Coherence Research. All rights reserved.
https://coherenceresearch.com
