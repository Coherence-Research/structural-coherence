# SC-AS Document Index

**Source:** AuraDB Document nodes + repo headers  
**Updated:** 2026-03-25  
**Authority:** SC-REGISTRY-000001 (living ledger)

This index covers all SC-AS governed artifacts included in the Constitutional Release v1.0 bundle. It is derived from and consistent with SC-REGISTRY-000001. For dependency graph, cascade rules, namespace allocation, and lifecycle state machine, see SC-REGISTRY-000001.

---

## Summary

| Tier | Count | Issued | Draft |
|---|---|---|---|
| Tier 0 — Canonical (constitutional) | 4 | 4 | 0 |
| Tier 2 — Certificates (RCCs) | 4 | 4 | 0 |
| Tier 3 — Stewardship | 5 | 5 | 0 |
| **Release Bundle Total** | **13** | **13** | **0** |

---

## Tier 0 — Canonical (Constitutional)

The closed, immutable canonical set. These four documents define the rules of the system. Amendment requires extraordinary governance per SC-GOV-000001. No elevation mechanism exists (per SC-SCOPE-000001 §6.1).

### SC-CORE-000001

| Field | Value |
|---|---|
| Canonical Name | THE COHERENCE CORE SPECIFICATION |
| Document Class | SPEC |
| Issuance ID | v39d |
| Version | 1.2.5 |
| Release Status | ISSUED |
| SHA-256 | `3a9b7ac0b9f2c896e7206d6892e9992ebaedab6054e83b97885ad1c55ade93d9` |
| Repository Path | `specs/canonical/SC-CORE-000001.md` |

**Abstract:** Defines foundational structural framework, core terms (T0–T7), binding clauses, and meta-structural governance for all SC-AS-governed artifacts. 76 kernel terms: 11 object primitives, 32 meta-definitions, 14 foundational conditions, 8 valid emergence conditions, 11 admissibility rules.

---

### SC-AXIOM-000001

| Field | Value |
|---|---|
| Canonical Name | THE COHERENCE AXIOMS SPECIFICATION |
| Document Class | SPEC |
| Issuance ID | v11l |
| Version | 1.0.0 |
| Release Status | ISSUED |
| SHA-256 | `05369abb763240e0a5689cd387706784c55fce98c0b9bc29338172b86ed891cc` |
| Repository Path | `specs/canonical/SC-AXIOM-000001.md` |

**Abstract:** Defines 10 canonical axioms (I-X) as derivations from SC-CORE primitives. Introduces no new primitives; all predicates are abbreviations of SC-CORE terms via a binding expansion discipline register.

---

### SC-HDR-000001

| Field | Value |
|---|---|
| Canonical Name | Structural Coherence Document Header Specification |
| Document Class | SPEC |
| Issuance ID | v11 |
| Version | 0.4.0 |
| Release Status | ISSUED |
| SHA-256 | `7ae85cc4eba408ba7602434be7daaacb24223a7075c97dba296d682f6c74f54d` |
| Repository Path | `specs/canonical/SC-HDR-000001.md` |

**Abstract:** Defines the normalized base header, 8 document class extensions with namespace tokens, integrity computation rules (blanked-SHA), and validation requirements for all SC-AS artifacts.

---

### SC-SCOPE-000001

| Field | Value |
|---|---|
| Canonical Name | Canonical Semantic Scope and Non-Prescriptive Clause |
| Document Class | SPEC |
| Issuance ID | v05 |
| Version | 1.1.0 |
| Release Status | ISSUED |
| SHA-256 | `75f01d22731a476a133f8c566d916fd642eafd9a1f3b09b75cf70f733ab21daf` |
| Repository Path | `specs/canonical/SC-SCOPE-000001.md` |

**Abstract:** Defines the jurisdictional boundary of SC-AS, canonical set membership (4 documents, closed), certificate tier architecture (3 tiers), and constitutional bundle composition.

---

## Tier 2 — Certificates (Reflexive Closure Certificates)

Each RCC attests that its target canonical document satisfies schema completeness, dependency acyclicity, primitive closure, and binding vocabulary discipline. All RCCs in this release were built from mechanical verification of the target artifacts.

### RCC-SC-CORE-000001

| Field | Value |
|---|---|
| Canonical Name | Reflexive Closure Certificate — SC-CORE-000001 |
| Document Class | RCC |
| Issuance ID | v03 |
| Version | 1.0.2 |
| Release Status | ISSUED |
| Target | SC-CORE-000001 (v39d) |
| Target SHA-256 | `3a9b7ac0b9f2c896e7206d6892e9992ebaedab6054e83b97885ad1c55ade93d9` |
| RCC SHA-256 | `8d0ce684d36364463aec78c7833172b416a76d2c8f0e91523571b541626e0343` |
| Repository Path | `specs/certificates/rcc__SC-CORE-000001__v39d__v03.md` |

---

### RCC-SC-AXIOM-000001

| Field | Value |
|---|---|
| Canonical Name | Reflexive Closure Certificate — SC-AXIOM-000001 |
| Document Class | RCC |
| Issuance ID | v03 |
| Version | 1.0.2 |
| Release Status | ISSUED |
| Target | SC-AXIOM-000001 (v11l) |
| Target SHA-256 | `05369abb763240e0a5689cd387706784c55fce98c0b9bc29338172b86ed891cc` |
| RCC SHA-256 | `3b6ed3e18452938809243c2a7ecc058d08b5ab0581fdeebbe1997d8280e033d0` |
| Repository Path | `specs/certificates/rcc__SC-AXIOM-000001__v11l__v03.md` |

---

### RCC-SC-HDR-000001

| Field | Value |
|---|---|
| Canonical Name | Reflexive Closure Certificate — SC-HDR-000001 |
| Document Class | RCC |
| Issuance ID | v02 |
| Version | 1.0.1 |
| Release Status | ISSUED |
| Target | SC-HDR-000001 (v11) |
| Target SHA-256 | `7ae85cc4eba408ba7602434be7daaacb24223a7075c97dba296d682f6c74f54d` |
| RCC SHA-256 | `01bfc8e7cf0b7188bf62bfa5660f3707d190918ef4588607d5f92a53b0a30188` |
| Repository Path | `specs/certificates/rcc__SC-HDR-000001__v11__v02.md` |

---

### RCC-SC-SCOPE-000001

| Field | Value |
|---|---|
| Canonical Name | Reflexive Closure Certificate — SC-SCOPE-000001 |
| Document Class | RCC |
| Issuance ID | v02 |
| Version | 1.0.1 |
| Release Status | ISSUED |
| Target | SC-SCOPE-000001 (v05) |
| Target SHA-256 | `75f01d22731a476a133f8c566d916fd642eafd9a1f3b09b75cf70f733ab21daf` |
| RCC SHA-256 | `2fe253c01c4cfe9717147f986c94fb80525a7a67835ebde8b26d1d5f9eb9fba8` |
| Repository Path | `specs/certificates/rcc__SC-SCOPE-000001__v05__v02.md` |

---

## Tier 3 — Stewardship

Documents that define operational governance, policy, licensing, naming, trademark, and authorship. Non-normative relative to SC-AS derivation but binding within their stewardship scope.

### SC-GOV-000001

| Field | Value |
|---|---|
| Canonical Name | Governance and Versioning |
| Document Class | FRAMEWORK |
| Issuance ID | v08 |
| Version | 0.5.1 |
| Release Status | ISSUED |
| SHA-256 | `ea8c9f11c2a53e68a0ce90e8abce6bc5fec2b2c657bac69433b208f80fc1f2de` |
| Repository Path | `specs/stewardship/SC-GOV-000001.md` |

**Abstract:** Defines release governance, conformance validation procedure (9 phases), constitutional bundle composition, and versioning model for SC-AS artifacts.

---

### SC-LICENSE-000001

| Field | Value |
|---|---|
| Canonical Name | Structural Coherence Text License (CC BY-ND 4.0) |
| Document Class | POLICY |
| Issuance ID | v05 |
| Version | 0.3.1 |
| Release Status | ISSUED |
| SHA-256 | `34be6964da031247fe27b86ece16bce2f1ba23a75f0d953cf9e6666ec67a35e2` |
| Repository Path | `specs/stewardship/SC-LICENSE-000001.md` |

**Abstract:** Defines CC BY-ND 4.0 licensing terms and distribution rights for SC-AS artifacts.

---

### SC-NAME-000001

| Field | Value |
|---|---|
| Canonical Name | Structural Coherence Naming and Layering Policy |
| Document Class | POLICY |
| Issuance ID | v04 |
| Version | 0.2.2 |
| Release Status | ISSUED |
| SHA-256 | `556fc017f10df27eef641918a2072fd2a93ac8f59e13fbfd0c470b61e58f6dac` |
| Repository Path | `specs/stewardship/SC-NAME-000001.md` |

**Abstract:** Defines naming conventions, layering policy, and allowed claims for SC-AS artifacts and implementations.

---

### SC-TM-000001

| Field | Value |
|---|---|
| Canonical Name | Structural Coherence Trademark Policy |
| Document Class | POLICY |
| Issuance ID | v04 |
| Version | 0.2.2 |
| Release Status | ISSUED |
| SHA-256 | `2ef6b8f9659251e25cac25e14901cc4d1b55110ac201a2767f0858b6ea413d51` |
| Repository Path | `specs/stewardship/SC-TM-000001.md` |

**Abstract:** Governs use of SC and SC-AS names, marks, and certification designations.

---

### SC-AUTHORSHIP-000001

| Field | Value |
|---|---|
| Canonical Name | Structural Coherence Authorship Declaration |
| Document Class | POLICY |
| Issuance ID | v04 |
| Version | 0.2.2 |
| Release Status | ISSUED |
| SHA-256 | `2955b8159f7dc22f9b5bfafca7f3b6606221f308bcc9ee5f9c2f8edd7491c6a0` |
| Repository Path | `specs/stewardship/SC-AUTHORSHIP-000001.md` |

**Abstract:** Records authorship, PGP key fingerprints, and provenance chain for the SC-AS specification suite.

---

## Maintenance

This file is updated whenever a document is issued, superseded, or its metadata changes. The authoritative living ledger is SC-REGISTRY-000001. This file is the repo-committed snapshot for the Constitutional Release v1.0 bundle.

*Coherence Research — https://coherenceresearch.com*
