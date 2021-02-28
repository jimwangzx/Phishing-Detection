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

# import dataset
data = pd.read_csv(os.path.join(dirname,"../data/Model_1.4Dataset.csv"), index_col="Unnamed: 0")

# split dataset
train, test = train_test_split(data, test_size=0.2)
train, val = train_test_split(train, test_size=0.2)

# create dataset
def df_to_dataset(dataframe, shuffle=True, batch_size=32):
  dataframe = dataframe.copy()
  labels = dataframe.pop('Target')
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  return ds

batch_size = 32
train_ds = df_to_dataset(train, batch_size=batch_size)
val_ds = df_to_dataset(val, shuffle=True, batch_size=batch_size)
test_ds = df_to_dataset(test, shuffle=True, batch_size=batch_size)

# create feauture list
feature = []

# insert numeric labels
for header in ['Length', 'CommonWords', 'Paypal', 'Slashes', 'DoubleSlash', 'AtSymbol', 'QuestionMark', 'Dash', 'Semicolon', 'PeriodCount', 'WLetter', 'VLetter', 'XLetter', 'ZLetter', 'JLetter', 'QLetter', 'Vowels', 'FirstPartNumbers']:
  feature.append(feature_column.numeric_column(header))

feature_layer = tf.keras.layers.DenseFeatures(feature)

    #feature_layer,

model = tf.keras.Sequential([
    feature_layer,
    layers.Dense(64, activation="tanh"),
    layers.Dense(64, activation="sigmoid"),
    layers.Dense(128),
    layers.Dense(128),
    layers.Dense(128),
    layers.Dense(1)
])

model.compile(loss = tf.losses.MeanSquaredError(), optimizer = tf.optimizers.Adam(), metrics=['accuracy'])

model.fit(train_ds, validation_data=val_ds, epochs=40)

loss, accuracy = model.evaluate(test_ds)
print("Accuracy", accuracy)

model.summary()

#model.save(os.path.join(dirname,'../model_1.4/model'))