import numpy as np
import pandas as pd
import csv
import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split

data = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\model_1.1\Model_1.1Dataset.csv", engine= 'python')

train, test = train_test_split(data, test_size=0.2, random_state=30, shuffle=True)

train.to_csv(r'model_1.1\datasets\trainSet.csv')
test.to_csv(r'model_1.1\datasets\testSet.csv')


