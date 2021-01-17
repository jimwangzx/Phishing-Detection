import numpy as np
import pandas as pd
import csv, os
from csv import writer
import pathlib
from sklearn.model_selection import train_test_split

dirname = os.path.dirname(__file__)

# import dataset
data = pd.read_csv(os.path.join(dirname,"../data/phishing_site_urls.csv"))
url = data['URL']
label = data['Label']

pastCS = pd.read_csv(os.path.join(dirname,"../data/commonString.csv"))
length = pastCS['Bad']
print(len(pastCS))


# user input: Type words here
words = ['login', 'bio']

def wordStats(word):
    count = 0
    goodCount = 0   
    for i in range(0,len(url),1):
        if url[i].count(word) > 0:
            count += 1
            if label[i] == 'good':
                goodCount += 1
    
    return count, goodCount

def appendCommonString(word, total, good, index):
    
    percentIndication = 100*good/total

    if percentIndication < 50:
        percentIndication = 100 - percentIndication

    #dataPoint = {'String': word, 'Word Count': total, 'Good': good, 'Bad': total-good, 'Percent Indication': percentIndication}
    dataPoint = [index, word, total, good, total-good, percentIndication]

    with open(os.path.join(dirname,"../data/commonString.csv"), 'a+', newline='') as write_obj:

        csv_writer = writer(write_obj)

        csv_writer.writerow(dataPoint)
    #print(dataPoint)

    #pd.DataFrame([dataPoint]).to_csv('data/commonString2.csv',)

def main():
    
    for z in range(0,len(words),1):
        tot, g = wordStats(words[z])
        appendCommonString(words[z], tot, g, len(length)-1+z)

    print("\n\ndone\n\n")
main()