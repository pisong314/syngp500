# SynGP500: Synthetic Australian General Practice Medical Notes

---

> **⚠️ IMPORTANT: ALL DATA IS SYNTHETIC**
>
> This dataset contains **entirely synthetic medical notes** generated using large language models. **No real patient data was used.** These notes are created for research and educational purposes only. While grounded in clinical guidelines and reviewed by a qualified GP, they may contain inaccuracies and should not be used for clinical decision-making.

---

## Overview

SynGP500 is a clinician-curated collection of 500 synthetic Australian general practice medical notes created to support machine learning and natural language processing research in primary care.

**The Problem:** Access to clinical text data is a significant challenge for healthcare NLP research due to privacy regulations and ethical constraints. Publicly available datasets for Australian general practice are particularly limited.

**The Solution:** SynGP500 addresses these limitations through systematic multi-dimensional grounding:

- **Condition selection:** Drawn from the RACGP curriculum for GP registrar training, ensuring educationally and clinically relevant presentations
- **Case distribution:** Matched to BEACH study data, reflecting realistic prevalence patterns in Australian general practice
- **Clinical reasoning:** Grounded in curated Australian medical guidelines for valid, evidence-based management
- **Contextual diversity:** Nine encounter settings (standard clinic, telehealth, after-hours, RACF, home visits, bulk billing, Aboriginal health services, community health, mobile outreach) across seven remoteness classifications (MM1–MM7), with management appropriately adapted to resource constraints and care pathways
- **Psychosocial complexity:** Integration of social determinants of health—treatment reluctance, housing instability, cultural factors, family dynamics—that shape real-world clinical decision-making
- **Stylistic authenticity:** Multiple documentation patterns reflecting writing styles observed across clinicians during years of medical practice, capturing natural variation in verbosity, abbreviation use, note structure, and reasoning documentation

**The Result:** A dataset exhibiting realistic linguistic variation—typos, abbreviations, diverse clinician voices—alongside the clinical complexity and contextual constraints of genuine general practice. These synthetic notes provide researchers and educators with a resource for developing and evaluating clinical NLP methods while inherently protecting patient privacy.

---

## Key Features

- **500 synthetic consultation notes** (average 606 words, range 241–1,538)
- **Adult and elderly focus (18+ years)** - pediatric cases not included in this pre-release version
- **Epidemiologically validated:** Case distribution closely matches BEACH study data (within ±1-2% for most presenting complaint categories)
- **Demonstrated realism:** Natural typo rate (0.83%), high stylometric diversity (MATTR 0.858–0.946), realistic length variation (CV 0.42-0.47)
- **SNOMED-CT-AU coded** for systematic ontological coverage

---

## Quick Start

To access the dataset:

```bash
# Clone the repository
git clone https://github.com/pisong314/syngp500.git
cd syngp500

# Browse the notes
ls notes/

# View a sample note
cat notes/14669001_0093_Acute_kidney_injury.txt
```

All 500 synthetic medical notes are located in the `/notes` directory as plain text files (UTF-8 encoded). Each filename follows the pattern: `{SNOMED_code}_{ID}_{condition_name}.txt`

---

## Realism of GP Consults

GP consultations are rarely the neat, single-problem encounters depicted in medical dramas. Real patients juggle work pressures, financial stress, childcare, and multiple health issues—all competing for attention in a 15-minute appointment. These synthetic notes authentically reflect this messy reality, capturing not just medical facts but the human complexity that shapes every consultation.

<details>
<summary><b>Click to expand: Annotated examples demonstrating realistic complexity of real consultations</b></summary>

### Example 1: Multiple Competing Demands

**File:** `notes/17059001_0012_Prepatellar_bursitis.txt` (60 lines)

**Context:** Tiler with knee pain, uncontrolled diabetes, and Centrelink forms—three problems in one brief visit.

**Key realistic features:**
- Line 5: `"bloody knee keeps blowing up"` — colloquial Australian language
- Line 13-14: `Multiple DNAs... Admits poor adherence, ran out "a few weeks ago"` — frank non-adherence documentation
- Line 16: `casual tiler, variable income. Applying public housing` — socioeconomic barriers shaping care
- Line 46: `Pathology done on-site today to minimise DNA` — GP adapting strategy to patient behavior patterns
- Lines 49-52: GP completing Centrelink/housing forms during clinical consultation—realistic administrative burden

**Commentary:** Real GP consultations rarely address single problems—they involve competing demands, social complexity, and time constraints requiring pragmatic compromises.

---

### Example 2: When Patient and Doctor Disagree

**File:** `notes/44465007_0024_Ankle_sprain.txt` (68 lines)

**Context:** Retail worker with ankle sprain wants MRI and "strong painkillers"—but evidence-based guidelines don't support either.

**Key realistic features:**
- Line 11: `"Just need the strong ones again, my usual doc would just give it, no questions"` — patient comparing doctors, wanting previous treatment repeated
- Line 13: `"Why can't we just scan it and fix it faster?"` — common misunderstanding that scans "fix" problems
- Line 12: `"No time for physio, can't afford days off"` — work and money barriers to recommended treatment
- Line 52: `Pt not happy but accepts "better than nothing" plan` — honest documentation that patient left dissatisfied
- Line 60: Declines medical certificate — `"boss will just cut my shifts"` — job insecurity preventing proper recovery

**Commentary:** Not all consultations end happily. GPs regularly navigate disagreements, balancing patient expectations with evidence-based practice, while maintaining the relationship even when patients are frustrated with the care plan.

---

**Why This Matters:**

These examples show what's often missing from sanitized medical datasets—the human reality of healthcare:
- **How people actually talk** ("bloody knee," "when I'm not wrecked after work")
- **Work and money stress** shaping what treatment people can actually do
- **Patients disagreeing with doctors** and consultations ending with both sides frustrated but moving forward
- **Non-adherence** documented honestly (missing appointments, running out of medications, not doing exercises)

Medical AI trained only on neat, textbook-style notes won't understand the real complexity of healthcare delivery. These authentic notes capture the chaos, compromise, and human messiness that define actual general practice.

</details>

---
## Generation Architecture

<details>
<summary><b>Click to expand: Detailed generation methodology</b></summary>

This dataset was created using a multi-stage synthetic data generation pipeline designed to ensure clinical realism, diversity, and accuracy:

### Core Generation Process
- **LLM-based generation** using contemporary frontier LLMs as the primary generation engine
- **Synthetic clinician personas database** incorporating diverse GP writing styles and documentation patterns (all synthetically created)

### Clinical Grounding and Validity
- **RACGP curriculum alignment:** Medical conditions selected from the RACGP curriculum for general practice registrar training
- **SNOMED-AU ontological mapping:** Conditions mapped to SNOMED-AU codes for systematic ontological expansion and coverage
- **BEACH study epidemiological distribution:** Case distribution of presenting complaints matches patterns from the BEACH (Bettering the Evaluation and Care of Health) epidemiological study of Australian general practice
- **Clinician-curated guidelines:** Clinical features, investigations, and management plans grounded in a curated set of Australian clinical guidelines and evidence-based resources

### Complexity and Realism Features
- **Multi-complaint presentations:** Cases include patients presenting with multiple simultaneous health concerns
- **Family and multi-patient consultations:** Notes documenting presentations involving multiple family members
- **Diverse practice settings:** Notes represent nine different consultation contexts (standard GP clinic, bulk billing, RACF, telehealth, home visits, after-hours, community health, Aboriginal health services, and mobile outreach), each with appropriate constraints, documentation patterns, and time pressures
- **Geographic variation in management:** Clinical management appropriately varies by remoteness classification (e.g., STEMI management in MM1 metropolitan areas differs from MM5 very remote locations, reflecting real-world resource availability and care pathways)
- **Psychosocial context:** Integration of psychosocial factors that influence clinical decision-making and patient management

### Quality Assurance
- **Dual-LLM validation pipeline:** A second LLM model flags potential factual inaccuracies and clinical inconsistencies
- **Human-in-the-loop review:** Flagged cases undergo manual clinical review by the author (qualified GP) for validation and correction

This architecture ensures that the synthetic notes capture not only the linguistic patterns of clinical documentation but also the medical complexity, contextual variations, and real-world constraints that characterize Australian general practice.

</details>

---

## Dataset Contents

The repository contains:
- **`/notes`**: 500 synthetic medical notes in plain text format
- Each file is named with the pattern: `{SNOMED_code}_{ID}_{condition_name}.txt`

---

## CRITICAL Disclaimers

**Please read this section carefully before using this dataset:**

⚠️ **SYNTHETIC DATA ONLY**
These notes are entirely synthetic and are NOT derived from real patients. No actual patient information was used in their creation.

⚠️ **LIMITED CLINICAL VALIDATION**
Cases underwent LLM-assisted screening to identify potentially problematic cases, followed by manual review of a subset by the author (a qualified general practitioner). However, this does NOT constitute comprehensive clinical validation by multiple independent clinicians. Clinical inaccuracies may be present despite best curation efforts.

⚠️ **NOT ENDORSED BY RACGP**
This is an independent research project and is NOT endorsed, sponsored, or affiliated with the Royal Australian College of General Practitioners (RACGP).

⚠️ **MAY CONTAIN CLINICAL INACCURACIES**
While created with medical knowledge and grounded in evidence-based guidelines, synthetic generation may introduce errors in clinical reasoning, medication dosing, investigation ordering, or management plans.

⚠️ **PRIMARY USE: ML/NLP RESEARCH**
This dataset is primarily intended for machine learning and natural language processing research purposes.

⚠️ **MEDICAL EDUCATION USE REQUIRES INDIVIDUAL CASE REVIEW**
If you are an educator considering using these cases for teaching:
- **You MUST review each case individually** before using it with students
- Verify clinical accuracy, appropriateness of management, and alignment with current guidelines
- Annotate or correct any identified errors before teaching use
- Do not assume clinical correctness without expert review

⚠️ **REPORTING INACCURACIES**
If you identify clinical inaccuracies or have concerns about specific cases, please report them via email to piyawoot.song@gmail.com. This helps improve the quality and utility of the dataset for the community.

---

## Use Cases

### Primary Use Case
**Machine Learning and NLP Research:**
- Clinical named entity recognition (NER)
- Information extraction and structuring
- Clinical text classification
- Documentation quality analysis
- Medical language model training and evaluation
- Stylometric analysis of clinical writing

### Secondary Use Case
**Medical Education (with precautions):**
- Examples of GP documentation formats
- Teaching clinical reasoning and differential diagnosis
- Demonstrating consultation structure and time management
- **REQUIRES:** Individual case review by qualified educators before teaching use

### Additional Applications
- Clinical documentation training for medical students and registrars
- Health informatics education
- Development of clinical decision support tools (research prototypes)

---

## License

This dataset is released under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**.

### Plain English Summary:
- ✅ **Free for research and education** (non-commercial use)
- ✅ **Share and adapt** with appropriate attribution
- ✅ **Must use the same license** for derivative works
- 📧 **Contact for commercial use** or larger synthetic datasets

For full license details, see the [LICENSE](LICENSE) file or visit:
https://creativecommons.org/licenses/by-nc-sa/4.0/

---

## Citation

If you use this dataset in your research or educational materials, please cite:

```bibtex
@dataset{songsiritat2025syngp500,
  author = {Songsiritat, Piyawoot},
  title = {SynGP500: Synthetic Australian General Practice Medical Notes},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/pisong314/syngp500}
}
```

---

## Dataset Statistics

### Overview
- **Total notes:** 500
- **Clinical presentations:** Aligned with RACGP registrar curriculum and BEACH study prevalence
- **Consultation settings:** Nine different contexts represented (standard GP clinic, bulk billing, RACF, telehealth, home visits, after-hours, community health, Aboriginal health services, mobile outreach)
- **Geographic locations:** Metropolitan, regional, rural, and remote locations (MM1-MM7 remoteness classifications)
- **Documentation styles:** Multiple synthetic clinician personas with varying documentation patterns

### Epidemiological Validation Against BEACH Study

<details>
<summary><b>Click to expand: BEACH study comparison table</b></summary>

To ensure realistic case distribution, the presenting complaints in this synthetic dataset were calibrated against the BEACH (Bettering the Evaluation and Care of Health) study—Australia's most comprehensive epidemiological study of general practice activity. The comparison below demonstrates strong alignment between this synthetic dataset and real-world Australian GP consultations:

| Category | BEACH % | Generated % | Difference |
|----------|---------|-------------|------------|
| Prescription | 8.8% | 7.2% | -1.6% |
| Check-up | 8.1% | 6.4% | -1.7% |
| Test results | 6.7% | 7.0% | +0.3% |
| Cough | 4.1% | 3.6% | -0.5% |
| Immunisation/vaccination | 3.3% | 3.8% | +0.5% |
| Administrative procedure | 2.5% | 3.2% | +0.7% |
| Back complaint | 2.0% | 2.6% | +0.6% |
| Rash | 1.8% | 2.6% | +0.8% |
| Throat symptom/complaint | 1.8% | 1.4% | -0.4% |
| Blood test | 1.5% | 2.2% | +0.7% |
| Fever | 1.4% | 2.4% | +1.0% |
| Depression | 1.3% | 2.6% | +1.3% |
| Abdominal pain | 1.2% | 2.2% | +1.0% |
| Upper respiratory tract infection | 1.1% | 1.0% | -0.1% |
| Headache | 1.1% | 2.0% | +0.9% |
| Skin symptom/complaint, other | 1.1% | 3.4% | +2.3% |
| Sneezing/nasal congestion | 1.0% | 1.6% | +0.6% |
| Hypertension/high blood pressure | 1.0% | 0.6% | -0.4% |
| Anxiety | 1.0% | 1.2% | +0.2% |
| Other referrals NEC | 0.9% | 1.4% | +0.5% |
| Weakness/tiredness | 0.9% | 2.2% | +1.3% |
| Knee symptom/complaint | 0.9% | 1.2% | +0.3% |
| Observation/health education/advice/diet | 0.9% | 1.6% | +0.7% |
| Ear pain/earache | 0.8% | 1.4% | +0.6% |
| Diabetes – all | 0.8% | 1.0% | +0.2% |
| Shoulder symptom/complaint | 0.8% | 1.6% | +0.8% |
| Foot/toe symptom/complaint | 0.7% | 1.2% | +0.5% |
| Diarrhoea | 0.7% | 0.4% | -0.3% |
| Sleep disturbance | 0.7% | 1.2% | +0.5% |
| Swelling | 0.7% | 1.8% | +1.1% |
| Other | 40.4% | 28.1% | -12.3% |
| **TOTAL** | **100.0%** | **100.0%** | **0.0%** |

**Key Observations:**

- **Strong overall alignment:** Most presenting complaint categories match BEACH study prevalence within ±1-2%, demonstrating realistic case distribution
- **Enhanced educational focus:** The lower "Other" category (-12.3%) reflects intentional emphasis on RACGP curriculum-relevant conditions, providing enhanced educational and research utility while maintaining epidemiological realism
- **Appropriate variation:** Minor differences (e.g., Depression +1.3%, Skin symptoms +2.3%) reflect both curriculum priorities and natural sampling variation
- **Common presentations well-represented:** High-frequency presentations closely mirror real-world frequencies

This comparison indicates that SynGP500's case distribution is broadly consistent with epidemiological patterns in Australian general practice, within the expected variation for a 500-case synthetic dataset.

</details>

### Stylometric Validation

<details>
<summary><b>Click to expand: Stylometric analysis metrics</b></summary>

Comprehensive stylometric analysis confirms the dataset exhibits realistic variation and diversity characteristic of genuine clinical documentation:

| Category | Metric | Value | Interpretation |
|----------|--------|-------|----------------|
| **Lexical Diversity** | MATTR₂₅ (25-word window) | 0.946 | High vocabulary richness |
| | MATTR₅₀ (50-word window) | 0.909 | |
| | MATTR₁₀₀ (100-word window) | 0.858 | |
| **Length Variation** | Average word count | 606 ± 257 | Substantial diversity |
| | Coefficient of Variation (CV) | 0.42-0.47 | Realistic note length variability |
| **Realistic Imperfections** | Overall typo rate | 0.83% (2,032/245,271 words) | Natural documentation errors |
| **Style Variability** | Article density CV | 0.84 | High inter-note variation |
| | Copula density CV | 1.19 | Diverse writing styles (not template-driven) |
| **Medical Authenticity** | Medical term density | 48.3% | Appropriate clinical content |

**Note:** MATTR (Moving-Average Type-Token Ratio) normalizes vocabulary richness across different note lengths. High CV values in style metrics indicate genuine diversity in clinician writing patterns rather than template-driven uniformity.

</details>

---

## NER Performance Validation

To validate the realism and utility of the synthetic notes, we evaluated Named Entity Recognition (NER) performance using MedCAT loaded with the SNOMED-AU lexicon plus the author's curated list of common Australian medical acronyms mapped to SNOMED concepts, then self-supervised trained on this 500-note corpus. **The model achieved a Grouped Type F1 score of 0.6951 (+14.7% improvement over baseline)**, demonstrating that even this small synthetic dataset exhibits sufficient clinical complexity and linguistic variation to support meaningful machine learning model training.

> **Clinical Relevance Note:**
>
> While strict SNOMED CUI matching is commonly reported in NER research, **Grouped Type matching** is more clinically meaningful for medical NLP applications. In real clinical practice, semantic distinctions like "rash (morphology)" versus "rash (finding)" are functionally equivalent—both refer to the same clinical entity. Grouped Type matching (which consolidates such SNOMED type variants) better reflects how clinical concepts are actually used in healthcare settings and provides a more realistic assessment of model utility.

### Training Performance Across Evaluation Strategies

![NER Training Performance](images/ner_performance.svg)

<details>
<summary><b>Click to expand: Detailed findings and methodology</b></summary>

### Key Findings

**Primary Result (Clinically Relevant Matching):**
- **Grouped Type F1: 0.6951** — Achieves strong performance with semantic type consolidation, plateaus at 2+ epochs
- **Span Match F1: 0.7289** — Best entity boundary detection, stable from epoch 2 onward

**Reference Results (Strict Matching):**
- **Strict F1: 0.6340** — Peaks at 1 epoch, then shows clear overfitting behavior
- **Training insight:** Model demonstrates classic overfitting pattern—performance peaks early (epoch 1) for CUI-based matching, then degrades as the model memorizes training examples rather than learning generalizable patterns

**Dataset Validation:**
- ✅ Untrained model achieves 58.8% F1, confirming baseline medical concept recognition
- ✅ Training on synthetic notes yields +14.7% improvement (Grouped Type), demonstrating realistic learning signal
- ✅ Performance plateau at 2+ epochs indicates dataset contains sufficient complexity for model convergence
- ✅ Results validate that synthetic notes exhibit clinical linguistic patterns suitable for NER training

### Evaluation Methodology

- **Model:** MedCAT (Medical Concept Annotation Tool)
- **Lexicon:** SNOMED CT-AU (Australian extension) + author's curated list of common Australian medical acronyms mapped to SNOMED concepts
- **Evaluation strategies:** Strict CUI matching, Grouped Type matching (consolidates semantic type variants), Span matching (entity boundary detection), Type matching, Relaxed matching, Partial IOU
- **Training:** 0–4 epoch progression to assess learning dynamics and overfitting

These results provide evidence that SynGP500's synthetic medical notes contain realistic clinical language patterns and sufficient complexity to support NER model training, validating the dataset's utility for machine learning research in Australian general practice contexts.

</details>

---

## Limitations

<details>
<summary><b>Click to expand: Dataset limitations</b></summary>

Users should be aware of the following limitations:

1. **No pediatric cases:** This release does not include pediatric consultations. Adult and elderly patients are well-represented. Pediatric cases will be included in future versions.
2. **Synthetic generation artifacts:** While designed to be realistic, these notes may contain patterns or inconsistencies not present in genuine clinical documentation
3. **Limited validation:** No large-scale clinical expert validation has been performed
4. **Temporal currency:** Guidelines and best practices evolve; notes reflect knowledge current at time of generation
5. **Australian context:** Notes are specific to Australian general practice; terminology, medications, and guidelines may not transfer to other healthcare systems
6. **Scope limitations:** 500 cases cannot capture the full spectrum of presentations seen in general practice

</details>

---

## Contributing

Contributions to improve the dataset quality are welcome:

- **Report clinical inaccuracies** via email to piyawoot.song@gmail.com
- **Suggest improvements** to documentation or metadata
- **Share your research findings** using this dataset

---

## Contact

**Dr Piyawoot Songsiritat**<br>
MBBS, FRACGP<br>
Clinical NLP Researcher

📧 Email: piyawoot.song@gmail.com

For inquiries about:
- Collaboration opportunities
- Larger synthetic datasets
- Technical questions about dataset generation

---

## Acknowledgments

The author acknowledges Aboriginal and Torres Strait Islander peoples as the Traditional Custodians of Australia and pays respect to Elders past, present, and emerging. This dataset includes synthetic cases that represent the diversity of patients seen in Australian general practice, including Aboriginal and Torres Strait Islander peoples. While these are entirely synthetic cases, they reflect the importance of culturally safe healthcare delivery and recognition of health disparities affecting Indigenous Australians.

This dataset was created to support the clinical NLP research community and medical education. The author acknowledges the importance of evidence-based guidelines from RACGP, Therapeutic Guidelines, and other Australian clinical resources that informed the synthetic note generation process.

---

## References

<details>
<summary><b>Click to expand: Full reference list</b></summary>

1. **Australian Digital Health Agency.** SNOMED CT-AU (Australian extension of SNOMED CT). Available from: https://www.healthterminologies.gov.au

2. **Britt H.** BEACH--bettering the evaluation and care of health: a continuous national study of general practice activity. *Commun Dis Intell Q Rep.* 2003;27(3):391-393. doi:10.33321/cdi.2003.27.68

3. **Rajotte JF, Bergen R, Buckeridge DL, El Emam K, Ng R, Strome E.** Synthetic data as an enabler for machine learning applications in medicine. *iScience.* 2022;25(11):105331. doi:10.1016/j.isci.2022.105331

4. **Kraljevic Z, Searle T, Shek A, Roguski L, Noor K, Bean D, Mascio A, Zhu L, Folarin AA, Roberts A, Bendayan R, Richardson MP, Stewart R, Shah AD, Wong WK, Ibrahim Z, Teo JT, Dobson RJB.** Multi-domain clinical natural language processing with MedCAT: The Medical Concept Annotation Toolkit. *Artif Intell Med.* 2021;117:102083. doi:10.1016/j.artmed.2021.102083

5. **Royal Australian College of General Practitioners.** 2022 RACGP curriculum and syllabus for Australian general practice (6th ed.). 2022. Available from: https://www.racgp.org.au/education/education-providers/curriculum/curriculum-and-syllabus/home

</details>

---

## Changelog

### Version 0.91 (Pre-release)
- NER validation added: MedCAT evaluation on clinician-authored fictional notes with clinician annotations

### Version 0.9 (Pre-release)
- Initial release: 500 synthetic GP notes
---

**Last Updated:** November 2025
