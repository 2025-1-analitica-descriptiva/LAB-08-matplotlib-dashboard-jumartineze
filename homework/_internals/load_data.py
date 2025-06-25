import pandas as pd


def load_data():
    df = pd.read_csv("files/input/shipping-data.csv")
    return df