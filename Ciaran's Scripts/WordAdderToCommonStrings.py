import numpy as np
import pandas as pd
import csv, os
import pathlib
from sklearn.model_selection import train_test_split

dirname = os.path.dirname(__file__)

# import dataset
data = pd.read_csv(os.path.join(dirname,"../data/phishing_site_urls.csv"), index_col="Unnamed: 0")
url = data['URL']

# user input
words = ['login']

def appendCommonString(word, total, good):
    
    percentIndication = 100*good/total

    if percentIndication < 50:
        percentIndication = 100 - percentIndication

    dataPoint = {'String': word, 'Word Count': total, 'Good': good, 'Bad': total-good, 'Percent Indication': percentIndication}

    #df = pd.DataFrame(dataPoint)
    #df.to_csv('my_csv.csv', mode='a', header=False)

def main():
    
    appendCommonString(words[0], )

print("/n/n", url[1])