import numpy as np
import pandas as pd
import csv, os
import pathlib
from sklearn.model_selection import train_test_split

dirname = os.path.dirname(__file__)

# import dataset
data = pd.read_csv(os.path.join(dirname,"../data/phishing_site_urls.csv"), index_col="Unnamed: 0")
url = data['URL']

print("/n/n", url[1])