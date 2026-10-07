import pandas as pd

from report import create_summary, filter_adults


def test_create_summary():
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Charlie"],
            "age": [20, 30, 40],
        }
    )

    result = create_summary(df)

    assert result["rows"] == 3
    assert result["columns"] == 2
    assert result["average_age"] == 30.0


def test_filter_adults():
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Charlie"],
            "age": [15, 20, 17],
        }
    )

    result = filter_adults(df)

    assert len(result) == 1
    assert result.iloc[0]["name"] == "Bob"