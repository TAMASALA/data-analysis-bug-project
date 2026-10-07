import numpy as np

from data_processor import clean_data, calculate_average, normalize


def test_clean_data():
    data = {
        "name": ["Alice", "Bob", None],
        "age": [25, 30, 40],
    }

    result = clean_data(data)

    assert len(result) == 2
    assert result["name"].tolist() == ["Alice", "Bob"]


def test_calculate_average():
    values = [10, 20, 30]

    assert calculate_average(values) == 20


def test_normalize():
    values = [10, 20, 30]

    result = normalize(values)

    expected = np.array([0.0, 0.5, 1.0])

    assert np.allclose(result, expected)