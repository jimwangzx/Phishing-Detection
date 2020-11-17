import pandas as pd

DATASET = "data/data_featured.csv"


data = pd.read_csv(DATASET, index_col = 0)
data = data.drop("URL", axis = 1)
data = data.sample(frac = .5)
data.to_csv("data/data_feature_no_URL.csv")