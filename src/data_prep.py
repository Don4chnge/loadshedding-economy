"""Data cleaning helpers for the load shedding / economy project.

Cleaning logic lives here (rather than only in notebook cells) so it is
testable and reusable. The notebook imports these functions.
"""
import pandas as pd


def build_monthly_retail(path: str) -> pd.DataFrame:
    """Reshape the Stats SA P6242.1 time-series Excel export to one row per month.

    The Stats SA export is wide: each row is one series (identified by the
    code in column H03), and monthly values sit in columns named MOmmYYYY
    (e.g. MO012002 = January 2002). We extract the two total-sales series
    at constant 2019 prices:
        con_act  -> actual values
        con_seas -> seasonally adjusted values

    Returns columns:
        month                  : Timestamp (month start)
        retail_sales_const     : total sales, constant 2019 prices, R million
        retail_sales_const_sa  : same, seasonally adjusted
        retail_yoy_pct         : year-on-year % change of the actual series
                                 (matches Stats SA's published unadjusted YoY)

    Validated: computed YoY for Feb 2026 (1.6%) matches the published
    P6242.1 statistical release.
    """
    raw = pd.read_excel(path, header=0)
    month_cols = [c for c in raw.columns if str(c).startswith("MO")]

    def series(code: str) -> pd.Series:
        row = raw.loc[raw["H03"] == code, month_cols].iloc[0]
        s = pd.to_numeric(row, errors="coerce")
        s.index = pd.to_datetime([f"{c[4:]}-{c[2:4]}-01" for c in s.index])
        return s

    out = pd.DataFrame(
        {
            "retail_sales_const": series("con_act"),
            "retail_sales_const_sa": series("con_seas"),
        }
    )
    out.index.name = "month"
    out = out.dropna(how="all")
    out["retail_yoy_pct"] = out["retail_sales_const"].pct_change(12) * 100
    return out.reset_index()


def build_monthly_loadshedding(raw: pd.DataFrame) -> pd.DataFrame:
    """Aggregate the Eskom Data Portal export to one row per month.

    Expected output columns:
        month           : Timestamp (month start)
        ls_intensity    : monthly load shedding intensity — GWh shed
                          (from 'Manual Load_Reduction(MLR)')

    NOTE: finalised once the Eskom export arrives. Eskom timestamps use
    AM/PM format; parse explicitly rather than relying on pandas inference.
    """
    raise NotImplementedError("Finalise once the Eskom export is in data/raw/")
