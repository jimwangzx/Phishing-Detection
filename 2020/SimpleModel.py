import numpy as np
import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt

#test_ds = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\testSet.csv")
dataset = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\lengthData.csv")

def build_model(learning_rate):
    model = tf.keras.models.Sequential()

    #add one layer
    model.add(tf.keras.layers.Dense(units=1, input_shape=(1,)))

    #Reduce mean square error
    model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=learning_rate),
            loss="mean_squared_error",
            metrics=[tf.keras.metrics.RootMeanSquaredError()])

    return model 

def train_model(model, df, feature, label, epochs, batch_size=None, validation_split=0.1):

    history = model.fit(x=df[feature],
                      y=df[label],
                      batch_size=batch_size,
                      epochs=epochs,
                      validation_split=validation_split)

    #obtain trained models weight and bias
    trained_weight = model.get_weights()[0]
    trained_bias = model.get_weights()[1]

    #epochs stored separately
    epochs = history.epoch

    hist = pd.DataFrame(history.history)
    rmse = hist["root_mean_squared_error"]
    return epochs, rmse, history.history

def plot_the_loss_curve(epochs, mae_training, mae_validation):
  """Plot a curve of loss vs. epoch."""

  plt.figure()
  plt.xlabel("Epoch")
  plt.ylabel("Root Mean Squared Error")

  plt.plot(epochs[1:], mae_training[1:], label="Training Loss")
  plt.plot(epochs[1:], mae_validation[1:], label="Validation Loss")
  plt.legend()
  
  # We're not going to plot the first epoch, since the loss on the first epoch
  # is often substantially greater than the loss for other epochs.
  merged_mae_lists = mae_training[1:] + mae_validation[1:]
  highest_loss = max(merged_mae_lists)
  lowest_loss = min(merged_mae_lists)
  delta = highest_loss - lowest_loss
  print(delta)

  top_of_y_axis = highest_loss + (delta * 0.05)
  bottom_of_y_axis = lowest_loss - (delta * 0.05)
   
  plt.ylim([bottom_of_y_axis, top_of_y_axis])
  plt.show()  

learning_rate = 0.1
epochs = 30
batch_size = 10
validation_split=0.2

feature="Length"
label="GoodBadInteger"

model = None

model = build_model(learning_rate)
epochs, rmse, history = train_model(model, dataset, feature, label, epochs, batch_size, validation_split)

plot_the_loss_curve(epochs, history["root_mean_squared_error"], 
                    history["val_root_mean_squared_error"])