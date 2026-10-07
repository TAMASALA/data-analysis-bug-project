import pandas as pd


def create_summary(df):
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "average_age": float(df["age"].mean()),
    }


def filter_adults(df):
    return df[df["age"] >= 18].copy()