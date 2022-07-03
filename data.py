import pandas as pd

def get_data():
    df = pd.read_excel("data/main_data.xlsx")
    df["Year"] = df["Date"].dt.year
    return df