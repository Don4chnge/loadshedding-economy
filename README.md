# Load Shedding's Economic Ripple Effect

> **Key finding:** _[TO BE COMPLETED after Phase 3 — state the headline result here first, e.g. "Each additional stage-day of load shedding per month is associated with an X% change in real retail trade sales, with a lag of N months (r = …, p = …, 95% CI […, …])."]_

A data-driven investigation into how Eskom load shedding stages correlate with — and potentially predict — shifts in South African economic indicators, primarily **retail trade sales**, over time.

**Core research question:** Does the severity and duration of load shedding measurably move South African economic activity, and by how much, with what time lag?

## Key visuals

_[3–5 exported PNGs embedded here after Phase 5 — e.g.]_

<!-- ![Load shedding vs retail sales](charts/01_timeseries_overlay.png) -->
<!-- ![Lag correlation](charts/02_lag_correlation.png) -->
<!-- ![Regression fit](charts/03_regression.png) -->

## Project structure

```
├── README.md
├── requirements.txt
├── notebooks/
│   └── 01_loadshedding_economy_analysis.ipynb   # main analysis
├── src/
│   └── data_prep.py                             # cleaning helpers
├── data/
│   ├── raw/                                     # untouched downloads (source + access date noted)
│   └── processed/                               # cleaned, merged datasets
├── charts/                                      # exported PNG visuals
└── reports/                                     # 3–5 page research-style report
```

## Data sources

| Dataset | Source | Access date |
| --- | --- | --- |
| Historical load shedding / manual load reduction | [Eskom Data Portal](https://www.eskom.co.za/dataportal/) | _[date]_ |
| Retail trade sales (P6242.1), constant 2019 prices | [Stats SA time series](https://www.statssa.gov.za/?page_id=1847) | _[date]_ |

## How to run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_loadshedding_economy_analysis.ipynb
```

Raw data files are included in `data/raw/` so results are reproducible without re-downloading.

## Methodology (summary)

1. **Collection** — official Eskom outage data + Stats SA retail trade sales
2. **Cleaning & alignment** — standardised to monthly granularity, merged into one dataframe
3. **Statistical analysis** — Pearson correlation with p-values and 95% confidence intervals; lag analysis (0–4 months)
4. **Modelling** — OLS regression quantifying impact; Prophet forecast using load shedding as a regressor
5. **Interpretation** — findings stated with limitations (correlation vs. causation, confounders such as COVID-19, interest rates, fuel prices)

## Limitations

_[Completed in Phase 6 — honest discussion of confounders, data gaps, and causal caveats.]_

---

*Portfolio project — final-year BSc IT (Data Science). Built July 2026.*
