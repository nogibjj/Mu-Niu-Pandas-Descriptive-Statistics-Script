import pytest
import pandas as pd
from hello import calc_mean, calc_median, calc_sd, draw


df = None
try:
    df = pd.read_csv("student_performance.csv")
except FileNotFoundError:
    pass


def test_df_exists():
    assert (
        df is not None
    ), "DataFrame was not loaded. Check if 'student_performance.csv' exists."


def test_calc_mean():
    if df is not None:
        for colname in df.select_dtypes(include=["number"]).columns:
            assert calc_mean(df, colname) == df[colname].mean()
        for colname in df.select_dtypes(include=["object"]).columns:
            assert calc_mean(df, colname) == "Mean not available for string"


def test_calc_median():
    if df is not None:
        for colname in df.select_dtypes(include=["number"]).columns:
            assert calc_median(df, colname) == df[colname].median()
        for colname in df.select_dtypes(include=["object"]).columns:
            assert calc_median(df, colname) == "Median not available for string"


def test_calc_sd():
    if df is not None:
        for colname in df.select_dtypes(include=["number"]).columns:
            assert calc_sd(df, colname) == df[colname].std()
        for colname in df.select_dtypes(include=["object"]).columns:
            assert calc_sd(df, colname) == "Standard Deviation not available for string"


def test_draw():
    if df is not None:
        for colname in df.select_dtypes(include=["object"]).columns:
            assert draw(df, colname) == "Plot not available for string"


if __name__ == "__main__":
    test_calc_mean()
    test_calc_median()
    test_calc_sd()
    test_df_exists()
    test_draw()
