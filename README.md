# Cross-Species Developmental Scaling — Power-Law Models

Statistical modeling of developmental timing translation across **mouse, rat, and human**, testing power-law (allometric) scaling models — including the quarter-power model — against alternative functional forms.

## Overview

This repository contains the analyses underlying the companion paper to the [Mouse-Rat-Human Development](https://github.com/Vazquez-Borsetti/mouse-rat-human-development) dataset. The search for a satisfactory model to translate developmental age between humans, mice, and rats proved sufficiently complex to require a separate modeling study. This repository contains the code and analyses used to fit, evaluate, and compare alternative models based on developmental age expressed as Days After Fertilization (DAF), with a particular focus on quarter-power scaling and models incorporating an additional correction term for early development.
The analysis evaluates a family of nested models — power, quarter-power, power-with-constant, and logarithmic forms, each with and without a species dummy variable — using weighted least squares (WLS) regression, leave-one-out cross-validation (LOOCV), and residual diagnostics (heteroscedasticity and functional-form misspecification tests).

---

## Repository Contents

```text
data/       → dataset (shared with paper1data) and data dictionary
src/        → shared configuration: model definitions, plotting utilities, color palette
tables/     → LaTeX tables generated for the manuscript
results/    → analysis outputs (model fits, statistics)
figures/    → generated figures
*.ipynb     → analysis notebooks (see below)
```

### Notebooks

| Notebook | Purpose |
| --- | --- |
| `panel1p_0.4.ipynb` | Main comparison panel: log–log regressions between species pairs (Human–Mouse, Human–Rat, Rat–Mouse), with diagnostic tests (Breusch–Pagan, RESET) and per-panel figures. |
| `panel2p_WLS_LOOCV.ipynb` | Fits the candidate models (`M1`–`M12`, see below) by weighted least squares and evaluates out-of-sample performance via leave-one-out cross-validation. |
| `table_dummy_loocv2.ipynb` | Builds species-dummy (grouped) model variants, runs LOOCV, and generates the significance/comparison tables used in the manuscript. |

---

## Models

Model definitions, equations, and initial parameters are centralized in [`src/config.py`](src/config.py). The candidate set includes:

| Model | Description | Equation |
| --- | --- | --- |
| M1 | Power | $y = b\,x^{a}$ |
| M2 | Quarter-power | $y = b\,x^{1/4}$ |
| M3 | Power + constant | $y = b\,x^{a} + c$ |
| M4 | Quarter-power + constant | $y = b\,x^{1/4} + c$ |
| M5 | Logarithmic | $y = b\ln(x) + c$ |
| M6–M9 | Logarithmic / power variants with species dummy ($D$) and constant | e.g. $y = (b_0+b_1D)x^{1/4}+(c_0+c_1D)$ |
| M10–M12 | Power variants with species dummy, no constant | e.g. $y = (b_0+b_1D)x^{a}$ |

The species dummy ($D$) allows slope/intercept/exponent to differ between rodent groups (e.g. mouse vs. rat), enabling formal tests of whether a single scaling law fits both species or whether species-specific parameters are required.

---

## Data

The dataset (`data/dataset_mrh_0.9.csv`) is the same curated mouse–rat–human developmental dataset described in the [Mouse-Rat-Human Development](https://github.com/Vazquez-Borsetti/mouse-rat-human-development) repository; see [`data/DATA_DICTIONARY.md`](data/DATA_DICTIONARY.md) for column definitions.
---

## Requirements

See [`requirements.txt`](requirements.txt):

```text
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.12
scipy>=1.10
statsmodels>=0.14
scikit-learn>=1.3
ipykernel>=6.25
```

Install with:

```bash
pip install -r requirements.txt
```

---

## Citation

If you use this code or its outputs, please cite the accompanying publication:

> **[Placeholder for companion paper citation]**

---

## License

This project is released under the **CC BY-NC-SA 4.0**. See [`LICENSE`](LICENSE) for the full license text.
