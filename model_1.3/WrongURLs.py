import numpy as np
import pandas as pd
import csv, os
import pathlib
import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt
from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

dirname = os.path.dirname(__file__)

data = pd.read_csv(os.path.join(dirname,"../data/Model_1.2Dataset.csv")) 
f1 = data['URL']
f2 = data['Label']
length = data['Length']
dataSize = len(f1)

#npArray = data.to_numpy()

model = keras.models.load_model(os.path.join(dirname,'../model_1.3/model'), compile=True)



#x = model.predict(npArray[1])
x = model.predict(np.array(data))

print(x)