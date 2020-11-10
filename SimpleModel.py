import numpy as np
import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt

train_ds = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\trainSet.csv")
test_ds = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\testSet.csv")

train_ds['Length'] = train_ds['Length'].astype(float)
test_ds['Length'] = test_ds['Length'].astype(float)

print("\n\n", train_ds.head(10), "\n\n")

def build_model(my_learning_rate):
  """Create and compile a simple linear regression model."""
  model = tf.keras.models.Sequential()

  model.add(tf.keras.layers.Dense(units=1, input_shape=(1,)))
 
  model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=my_learning_rate),
                loss="mean_squared_error",
                metrics=[tf.keras.metrics.RootMeanSquaredError()])

  return model               


def train_model(model, ds, feature, label, my_epochs, 
                my_batch_size=None, my_validation_split=0.1):
  """Feed a dataset into the model in order to train it."""

  history = model.fit(x=ds[feature],
                      y=ds[label],
                      batch_size=my_batch_size,
                      epochs=my_epochs,
                      validation_split=my_validation_split)


  epochs = history.epoch

  hist = pd.DataFrame(history.history)
  rmse = hist["root_mean_squared_error"]

  return epochs, rmse, history.history   

print("Defined the build_model and train_model functions.")

def plot_the_loss_curve(epochs, mae_training, mae_validation):
  """Plot a curve of loss vs. epoch."""

  plt.figure()
  plt.xlabel("Epoch")
  plt.ylabel("Root Mean Squared Error")

  plt.plot(epochs[1:], mae_training[1:], label="Training Loss")
  plt.plot(epochs[1:], mae_validation[1:], label="Validation Loss")
  plt.legend()
  
  merged_mae_lists = mae_training[1:] + mae_validation[1:]
  highest_loss = max(merged_mae_lists)
  lowest_loss = min(merged_mae_lists)
  delta = highest_loss - lowest_loss
  print(delta)

  top_of_y_axis = highest_loss + (delta * 0.05)
  bottom_of_y_axis = lowest_loss - (delta * 0.05)
   
  plt.ylim([bottom_of_y_axis, top_of_y_axis])
  plt.show()  

print("Defined the plot_the_loss_curve function.")




learning_rate = 0.08
epochs = 30
batch_size = 100

validation_split=0.2

my_feature="Length" 
my_label=""

my_model = None

my_model = build_model(learning_rate)
epochs, rmse, history = train_model(my_model, train_ds, my_feature, 
                                    my_label, epochs, batch_size, 
                                    validation_split)

plot_the_loss_curve(epochs, history["root_mean_squared_error"], 
                    history["val_root_mean_squared_error"])
                    