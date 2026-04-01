# Release Notes — SC-DOC-000001 v1.0.0 (Issuance ID: v01)

**Released:** 2026-04-01  
**Publisher:** Coherence Research  
**Status:** First issuance  
**Supersedes:** SC-AUTH-000001 (v03, SUPERSEDED)

---

## Summary

First issuance of SC-DOC-000001, the Structural Coherence Document Authoring Specification. This specification defines the complete authoring surface for all SC-AS documents and supersedes SC-AUTH-000001.

---

## What This Specification Covers

SC-DOC-000001 governs all nine cells of the document surface:

- **8 block types:** prose paragraph, heading, unordered list, ordered list, display math, code block, table, horizontal rule
- **4 inline types:** inline math, inline code, bold, italic
- **7 semantic containers:** definition, theorem, lemma/corollary, proof, scope, negative scope, invariants
- **8 document classes:** SPEC, FRAMEWORK, PAPER, MODULE, RCC, LEDGER, POLICY, NOTE — each with content requirements and section templates
- **44-cell format compatibility matrix:** every pairwise combination of format primitives declared as SAFE, CAUTION, PROHIBITED, or PROMOTE
- **Pipeline interface:** rendering chain declaration, L2-L3 contract, pipeline limitations
- **Pipeline compatibility checklist:** 22 mechanically enforceable items, 7 human review items

---

## Relation to SC-AUTH-000001

SC-AUTH-000001 (v2.1) governed the authoring layer only — expression principles and format primitives (cells PF and partial CF of the document surface). SC-DOC-000001 extends governance to the complete surface: content requirements per document class, structural composition rules, semantic containers, section templates, content ordering, and the pipeline interface.

All rules from SC-AUTH v2.1 are incorporated into SC-DOC with extensions. The supersession is non-destructive.

---

## Conformance

Reflexive Closure Certificate: `rcc__SC-DOC-000001__v01__v01.md`  
RCC Result: **PASS** (7/7 checks)  
Self-application: SC-DOC-000001 conforms to its own declared grammar.

---

## Known Gaps (Non-Blocking)

- 13 of 22 [P] preflight items declared in Section 12 are not yet implemented in `preflight.sh`. SC-DOC passes all items on its own content. Implementation is a follow-up tooling task before v1.1.
- SC-PIPE (the rendering contract specification) is not yet authored. Section 11 of this specification serves as the interim pipeline interface declaration.

---

## File Integrity

SHA-256 of specification source: `1ce85a1af47f243c7888867dd9210123a21729d93acd01a114377fd9ded6ecc4`  
*(Hash is computed on the source file with the SHA-256 field blanked, per SC-HDR-000001 section 3.2 Rule 7.)*
