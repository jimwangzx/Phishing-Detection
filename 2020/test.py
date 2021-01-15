import pandas as pd
import string

dictionary = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\Dictionary\top-34k.csv", engine= 'python') 
word = dictionary['google.com']

dictionary.tail()