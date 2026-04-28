import pandas as pd

def load_data():
    ethiopia = pd.read_csv("/home/samri/climate-challenge-week0/data/ethiopia_clean.csv")
    kenya = pd.read_csv("/home/samri/climate-challenge-week0/data/kenya_clean.csv")
    nigeria = pd.read_csv("/home/samri/climate-challenge-week0/data/nigeria_clean.csv")
    sudan = pd.read_csv("/home/samri/climate-challenge-week0/data/sudan_clean.csv")
    tanzania = pd.read_csv("/home/samri/climate-challenge-week0/data/Tanzania_clean.csv")

    df = pd.concat([ethiopia, kenya, nigeria, sudan, tanzania], ignore_index=True)

    return df