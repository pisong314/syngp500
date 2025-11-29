# Stylometric Analysis

Comprehensive stylometric analysis confirms the dataset exhibits realistic variation and diversity characteristic of genuine clinical documentation.

## Analysis Metrics

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

## Interpretation

**MATTR (Moving-Average Type-Token Ratio)** normalizes vocabulary richness across different note lengths. The high values (0.858-0.946) indicate genuine lexical diversity rather than repetitive, template-driven language.

**High CV values** in style metrics (article density 0.84, copula density 1.19) indicate genuine diversity in clinician writing patterns. This suggests the notes were not generated from rigid templates, but exhibit natural variation in documentation style.

**Natural imperfections** such as the 0.83% typo rate (2,032 typos across 245,271 words) reflect realistic clinical documentation practices where minor errors occur during time-pressured consultations.

**Length variation** with a coefficient of variation of 0.42-0.47 demonstrates that notes vary substantially in length (average 606 ± 257 words), reflecting the reality that different clinical encounters require different levels of documentation detail.

---

[← Back to main README](../../README.md)
