# NER Performance Validation

To validate the realism and utility of the synthetic notes, we evaluated Named Entity Recognition (NER) performance using MedCAT loaded with the SNOMED-AU lexicon plus the author's curated list of common Australian medical acronyms mapped to SNOMED concepts, then self-supervised trained on this 500-note corpus. 

**The model achieved a Grouped Type F1 score of 0.6951 (+14.7% improvement over baseline)**, demonstrating that even this small synthetic dataset exhibits sufficient clinical complexity and linguistic variation to support meaningful machine learning model training.

## Clinical Relevance Note

While strict SNOMED CUI matching is commonly reported in NER research, **Grouped Type matching** is more clinically meaningful for medical NLP applications. In real clinical practice, semantic distinctions like "rash (morphology)" versus "rash (finding)" are functionally equivalent—both refer to the same clinical entity. Grouped Type matching (which consolidates such SNOMED type variants) better reflects how clinical concepts are actually used in healthcare settings and provides a more realistic assessment of model utility.

## Training Performance Across Evaluation Strategies

![NER Training Performance](../../images/ner_performance.svg)

### Overall F1 Scores - Full Training Progression

| Strategy     | Untrained | 1 Epoch | 2 Epochs | 3 Epochs | 4 Epochs | BEST    | Peak Improvement |
|--------------|-----------|---------|----------|----------|----------|---------|------------------|
| Strict       | 0.5882    | 0.6340  | 0.6187   | 0.6222   | 0.6258   | 1-epoch | +7.8% ⭐          |
| Grouped Type | 0.6059    | 0.6928  | 0.6951   | 0.6951   | 0.6951   | 2/3/4   | +14.7% ⭐⭐        |
| Type Match   | 0.5980    | 0.6625  | 0.6489   | 0.6542   | 0.6560   | 1-epoch | +10.8% ⭐         |
| Span Match   | 0.6196    | 0.7266  | 0.7289   | 0.7289   | 0.7289   | 2/3/4   | +17.6% ⭐⭐        |

### Evaluation Strategy Definitions

- **Strict:** Exact span boundaries (start==start, end==end) + exact CUI match — most stringent, requires perfect concept identification
- **Grouped Type:** Exact span boundaries + clinically equivalent semantic type (e.g., 'disorder' ≈ 'morphologic abnormality') — most clinically relevant, consolidates functionally equivalent SNOMED types
- **Type Match:** Exact span boundaries + semantic type match (ignores specific CUI) — allows different concepts within same semantic category
- **Span Match:** Exact span boundaries only (ignores CUI and semantic type) — measures entity detection quality regardless of concept mapping

## Key Findings

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

## Evaluation Methodology

- **Model:** MedCAT (Medical Concept Annotation Tool)
- **Lexicon:** SNOMED CT-AU (Australian extension) + author's curated list of common Australian medical acronyms mapped to SNOMED concepts
- **Evaluation strategies:** Strict CUI matching, Grouped Type matching (consolidates semantic type variants), Span matching (entity boundary detection), Type matching
- **Training:** 0–4 epoch progression to assess learning dynamics and overfitting

## Conclusion

These results provide evidence that SynGP500's synthetic medical notes contain realistic clinical language patterns and sufficient complexity to support NER model training, validating the dataset's utility for machine learning research in Australian general practice contexts.

---

[← Back to main README](../../README.md)
