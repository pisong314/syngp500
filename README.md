# SynGP500: Synthetic Australian General Practice Medical Notes

---

> **⚠️ IMPORTANT: ALL DATA IS SYNTHETIC**
>
> This dataset contains **entirely synthetic medical notes** generated using large language models. **No real patient data was used.** These notes are created for research and educational purposes only. While grounded in clinical guidelines and reviewed by a qualified GP, they may contain inaccuracies and should not be used for clinical decision-making.

---

## Overview

SynGP500 is a clinician-curated collection of 500 synthetic Australian general practice medical notes created to support machine learning and natural language processing research in primary care.

**The Problem:** Access to clinical text data is a significant challenge for healthcare NLP research due to privacy regulations and ethical constraints. Publicly available datasets for Australian general practice are particularly limited.

**The Solution:** SynGP500 provides privacy-preserving synthetic data that bypasses these constraints while maintaining clinical realism through systematic multi-dimensional grounding:

- **Condition selection:** Drawn from the RACGP curriculum for GP registrar training, ensuring educationally and clinically relevant presentations
- **Case distribution:** Matched to BEACH study data, reflecting realistic prevalence patterns in Australian general practice
- **Clinical reasoning:** Grounded in curated Australian medical guidelines for valid, evidence-based management
- **Contextual diversity:** Nine encounter settings (standard clinic, telehealth, after-hours, RACF, home visits, bulk billing, Aboriginal health services, community health, mobile outreach) across seven remoteness classifications (MM1–MM7), with management appropriately adapted to resource constraints and care pathways
- **Psychosocial complexity:** Integration of social determinants of health—treatment reluctance, housing instability, cultural factors, family dynamics—that shape real-world clinical decision-making
- **Stylistic authenticity:** Multiple documentation patterns reflecting writing styles observed across clinicians during years of medical practice, capturing natural variation in verbosity, abbreviation use, note structure, and reasoning documentation

**The Result:** A dataset exhibiting realistic linguistic variation—typos, abbreviations, diverse clinician voices—alongside the clinical complexity and contextual constraints of genuine general practice. These synthetic notes provide researchers and educators with a resource for developing and evaluating clinical NLP methods while inherently protecting patient privacy.

---

## Key Features

- **500 synthetic consultation notes** (average 606 ± 257 words, range 241–1,538)
- **Adult and elderly focus (18+ years)** - pediatric cases not included in this pre-release version
- **Clinical presentations:** Aligned with RACGP registrar curriculum and BEACH study prevalence patterns
- **Nine consultation settings:** Standard clinic, bulk billing, RACF, telehealth, home visits, after-hours, community health, Aboriginal health services, mobile outreach
- **Geographic diversity:** Metropolitan, regional, rural, and remote (MM1-MM7 remoteness classifications)
- **Documentation styles:** Multiple synthetic clinician personas with varying patterns
- **Epidemiologically validated:** Case distribution closely matches BEACH study data (within ±1-2% for most presenting complaint categories)
- **Demonstrated realism:** Natural typo rate (0.83%), high stylometric diversity (MATTR 0.858–0.946), realistic length variation (CV 0.42-0.47)
- **Medical authenticity:** 48.3% medical term density, SNOMED-CT-AU coded for systematic ontological coverage
- **NER validated:** Grouped Type F1 score of 0.6951 (+14.7% improvement over baseline) using MedCAT, validated against gold fictional clinician-authored notes

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

## 📚 Documentation

### Clinical Realism
- **[Realistic consult complexity](docs/REALISM.md)** - See actual examples how complexities of real consults are reflected in this dataset.
### Validation
- **[NER Performance](docs/validation/ner_performance.md)** - MedCAT evaluation results (Grouped Type F1: 0.6951, +14.7% improvement)
- **[BEACH Epidemiological Comparison](docs/statistics/beach_comparison.md)** - Case distribution validation against real Australian GP data
- **[Stylometric Analysis](docs/statistics/stylometric_analysis.md)** - Linguistic diversity metrics (MATTR, typo rates, style variation)

### Methodology
- **[Generation Architecture](docs/methodology/generation.md)** - How the synthetic notes were created, including LLM-based generation, clinical grounding, and quality assurance

### Reference
- **[Use Cases](docs/reference/use_cases.md)** - Recommended applications and precautions
- **[Limitations](docs/reference/limitations.md)** - Important constraints and scope
- **[Contributing](docs/reference/contributing.md)** - How to report issues and improve the dataset

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

1. **Australian Digital Health Agency.** SNOMED CT-AU (Australian extension of SNOMED CT). Available from: https://www.healthterminologies.gov.au

2. **Britt H.** BEACH--bettering the evaluation and care of health: a continuous national study of general practice activity. *Commun Dis Intell Q Rep.* 2003;27(3):391-393. doi:10.33321/cdi.2003.27.68

3. **Kraljevic Z, Searle T, Shek A, Roguski L, Noor K, Bean D, Mascio A, Zhu L, Folarin AA, Roberts A, Bendayan R, Richardson MP, Stewart R, Shah AD, Wong WK, Ibrahim Z, Teo JT, Dobson RJB.** Multi-domain clinical natural language processing with MedCAT: The Medical Concept Annotation Toolkit. *Artif Intell Med.* 2021;117:102083. doi:10.1016/j.artmed.2021.102083

4. **Rajotte JF, Bergen R, Buckeridge DL, El Emam K, Ng R, Strome E.** Synthetic data as an enabler for machine learning applications in medicine. *iScience.* 2022;25(11):105331. doi:10.1016/j.isci.2022.105331

5. **Royal Australian College of General Practitioners.** 2022 RACGP curriculum and syllabus for Australian general practice (6th ed.). 2022. Available from: https://www.racgp.org.au/education/education-providers/curriculum/curriculum-and-syllabus/home

---

## Changelog

### Version 0.91 (Pre-release)
- NER validation added: MedCAT evaluation on clinician-authored fictional notes with clinician annotations
- More organised README.md
### Version 0.9 (Pre-release)
- Initial release: 500 synthetic GP notes

---

**Last Updated:** November 2025
