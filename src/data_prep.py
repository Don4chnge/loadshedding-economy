"""Data cleaning helpers for the load shedding / economy project.

Functions here get finalised once the real raw files land in data/raw/.
Keeping cleaning logic in a module (rather than only in notebook cells)
makes it testable and reusable.
"""
import pandas as pd


def build_monthly_loadshedding(raw: pd.DataFrame) -> pd.DataFrame:
    """Aggregate the Eskom Data Portal export to one row per month.

    Expected output columns:
        month           : period start (Timestamp, month start)
        ls_intensity    : monthly load shedding intensity — GWh shed
                          (from 'Manual Load Reduction') or stage-hours,
                          depending on which columns the export contains.

    NOTE: exact column names depend on the Eskom export — finalise after
    inspecting the real file. Eskom timestamps use AM/PM format; parse
    explicitly rather than relying on pandas inference.
    """
    raise NotImplementedError("Finalise once the Eskom export is in data/raw/")


def build_monthly_retail(raw: pd.DataFrame) -> pd.DataFrame:
    """Reshape the Stats SA P6242.1 time-series export to one row per month.

    Expected output columns:
        month                   : Timestamp, month start
        retail_sales            : sales at constant 2019 prices
        retail_yoy_pct          : year-on-year % change, unadjusted

    NOTE: Stats SA Excel time-series files carry metadata header rows and
    series codes — inspect before parsing.
    """
    raise NotImplementedError("Finalise once the Stats SA file is in data/raw/")
