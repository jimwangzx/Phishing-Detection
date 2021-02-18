import numpy as np
import csv
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

ds = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\lengthData.csv") 

train, test = train_test_split(ds, test_size=0.3, random_state=30, shuffle=True)

train.to_csv('trainSet.csv')
test.to_csv('testSet.csv')