# Dataset Limitations

Users should be aware of the following limitations when working with SynGP500:

## 1. No Pediatric Cases

This release does not include pediatric consultations. Adult and elderly patients are well-represented. Pediatric cases will be included in future versions.

**Impact:** Researchers working on pediatric NLP should use other datasets or wait for future SynGP500 releases.

## 2. Synthetic Generation Artifacts

While designed to be realistic, these notes may contain patterns or inconsistencies not present in genuine clinical documentation.

**Impact:** Some linguistic patterns may be artifacts of LLM generation rather than authentic clinical practice. Users should validate findings against real clinical notes where possible.

## 3. Limited Validation

No large-scale clinical expert validation has been performed. While the author (a qualified GP) reviewed flagged cases, comprehensive multi-clinician validation has not been conducted.

**Impact:** Clinical inaccuracies may be present. Users should not assume all medical content is factually correct.

## 4. Temporal Currency

Guidelines and best practices evolve; notes reflect knowledge current at time of generation (November 2025).

**Impact:** Some management recommendations may become outdated as clinical guidelines change. Users should verify current best practices independently.

## 5. Australian Context

Notes are specific to Australian general practice; terminology, medications, and guidelines may not transfer to other healthcare systems.

**Impact:**
- PBS (Pharmaceutical Benefits Scheme) references are Australia-specific
- RACF (Residential Aged Care Facility), BEACH study, RACGP curriculum are Australian contexts
- Medication names, dosing, and availability reflect Australian practice
- Not suitable for training systems for other healthcare jurisdictions without adaptation

## 6. Scope Limitations

500 cases cannot capture the full spectrum of presentations seen in general practice.

**Impact:**
- Rare conditions may be underrepresented
- Some clinical scenarios may not be covered
- Diversity of patient populations may be limited
- Cannot replace comprehensive real-world clinical datasets for all applications

## 7. No Multi-Modal Data

Notes contain text only—no images, pathology results, ECGs, or other clinical data types.

**Impact:** Cannot support research requiring integration of text with imaging, laboratory data, or other clinical modalities.

## 8. Annotation Limitations

While notes include SNOMED-CT-AU coding, no other structured annotations (entities, relationships, temporal markers) are provided.

**Impact:** Researchers requiring pre-annotated NER training data will need to create annotations themselves.

---

[← Back to main README](../../README.md)
