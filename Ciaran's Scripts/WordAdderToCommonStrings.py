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
#print(len(pastCS))

newCS = pd.read_csv(os.path.join(dirname,"../data/CommonStringsv2021.csv")) #Changed this
# user input: Type words here
allwords = newCS['String'] #this is new
words = []
minimum = 100

def wordCriteria():
    per100Counter = 0
    perc = 0
    for w in allwords:
        numOfURLwStr = 0
        per100Counter += 1
        if per100Counter % int(len(allwords)/100) == 0:
            print(perc, '%')
            perc += 1

        for u in url:
            if u.count(str(w)) > 0:
                numOfURLwStr += 1
        if numOfURLwStr >= minimum:
            words.append(w)

    # make a FUCKING BACKUP SM FUCKING H, 2 DAYS OF PROCESSING POWER GONE!!!!!!!! FUCK
    backup = {'String': words}

    bdf = pd.DataFrame(backup)

    bdf.to_csv(os.path.join(dirname, '../Test/BackupStrings.csv'))

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

    with open(os.path.join(dirname,"../data/commonString3.csv"), 'a+', newline='') as write_obj:

        csv_writer = writer(write_obj)

        csv_writer.writerow(dataPoint)
    #print(dataPoint)

    #pd.DataFrame([dataPoint]).to_csv('data/commonString2.csv',)

def main():
    
    print('\nMain program started\n')
    wordCriteria()
    print('\nWordlist complete\nStarting second loop...\n')

    for z in range(0,len(words),1):
        if z % int(len(words)/100) == 0:
            print('Loading...', int(z/len(words)*100), '%')
        tot, g = wordStats(str(words[z]))
        appendCommonString(str(words[z]), tot, g, len(length)-1+z)

    print("\n\ndone\n\n")

main()