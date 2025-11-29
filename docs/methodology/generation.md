# Generation Methodology

This dataset was created using a multi-stage synthetic data generation pipeline designed to ensure clinical realism, diversity, and accuracy.

## Core Generation Process

- **LLM-based generation** using contemporary frontier LLMs as the primary generation engine
- **Synthetic clinician personas database** incorporating diverse GP writing styles and documentation patterns (all synthetically created)

## Clinical Grounding and Validity

- **RACGP curriculum alignment:** Medical conditions selected from the RACGP curriculum for general practice registrar training
- **SNOMED-AU ontological mapping:** Conditions mapped to SNOMED-AU codes for systematic ontological expansion and coverage
- **BEACH study epidemiological distribution:** Case distribution of presenting complaints matches patterns from the BEACH (Bettering the Evaluation and Care of Health) epidemiological study of Australian general practice
- **Clinician-curated guidelines:** Clinical features, investigations, and management plans grounded in a curated set of Australian clinical guidelines and evidence-based resources

## Complexity and Realism Features

- **Multi-complaint presentations:** Cases include patients presenting with multiple simultaneous health concerns
- **Family and multi-patient consultations:** Notes documenting presentations involving multiple family members
- **Diverse practice settings:** Notes represent nine different consultation contexts (standard GP clinic, bulk billing, RACF, telehealth, home visits, after-hours, community health, Aboriginal health services, and mobile outreach), each with appropriate constraints, documentation patterns, and time pressures
- **Geographic variation in management:** Clinical management appropriately varies by remoteness classification (e.g., STEMI management in MM1 metropolitan areas differs from MM5 very remote locations, reflecting real-world resource availability and care pathways)
- **Psychosocial context:** Integration of psychosocial factors that influence clinical decision-making and patient management

## Quality Assurance

- **Dual-LLM validation pipeline:** A second LLM model flags potential factual inaccuracies and clinical inconsistencies
- **Human-in-the-loop review:** Flagged cases undergo manual clinical review by the author (qualified GP) for validation and correction

This architecture ensures that the synthetic notes capture not only the linguistic patterns of clinical documentation but also the medical complexity, contextual variations, and real-world constraints that characterize Australian general practice.

---

[← Back to main README](../../README.md)
