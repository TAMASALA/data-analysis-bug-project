import numpy as np
import pandas as pd


def clean_data(data):
    df = pd.DataFrame(data)

    df = df.dropna()

    return df


def calculate_average(values):
    values = np.array(values)

    return np.sum(values) / len(values)


def normalize(values):
    values = np.array(values, dtype=float)

    minimum = values.min()
    maximum = values.max()

    return (values - minimum) / (maximum - minimum if maximum != minimum else 1.0)