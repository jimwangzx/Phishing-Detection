import pandas as pd
import string, os
from itertools import permutations

dirname = os.path.dirname(__file__)

#To change files change the string in main and the label title

dataSet1 = pd.read_csv(os.path.join(dirname, "../data/phishin_site_urls.csv"))
feature1 = dataSet1['URL']
feature2 = dataSet1['Label']
size = 549346

requiredWordLength = 0
threshold = 0.0005

commonWordsList = []
wordListPercent = []

goodl = []
badl = []
wc = []
pi = []

def trunc(x):
    x = x*10000
    x = int(x)
    x = x/10000
    return x

def printToFile(word):

    wordCount = 0
    wordGood = 0

    for i in range(0,size,1):
        if feature1[i].find(word) >= 0:
            wordCount += 1 
            if feature2[i] == "good":
                wordGood += 1

    percentIndication = wordGood/wordCount*100

    if percentIndication < 50:
        percentIndication = 100 - percentIndication

    #append to appropriate lists
    wc.append(wordCount)
    goodl.append(wordGood)
    badl.append(wordCount-wordGood)
    pi.append(percentIndication)

    #add to file
    line = word + "\tWord Count: " + str(wordCount) + "\tGood Samples: " + str(wordGood) + "\tBad Samples: " + str(wordCount-wordGood) + "\tPercent Indication: " + str(trunc(percentIndication)) + "\n"

    fi = open("2020\commonWords3.txt", "a")
    fi.write(line)
    fi.close()

    return percentIndication

def findIndex(perc):
    x = 0
    if perc >= wordListPercent[len(wordListPercent)-1]:
        wordListPercent.append(perc)
        return len(wordListPercent)-1

    while 1 == 1:
        if perc >= wordListPercent[x]:
            x += 1
        else:
            wordListPercent.insert(x, perc)
            return x

def sortWords(word):
    wordCount = 0
    wordGood = 0

    for i in range(0,size,1):
        if feature1[i].find(word) >= 0:
            wordCount += 1 
            if feature2[i] == "good":
                wordGood += 1

    if wordCount == 0:
        return

    percentIndication = wordGood/wordCount*100

    if percentIndication < 50:
        percentIndication = 100 - percentIndication

    #check if over threshold
    if wordCount/size >= threshold:
        print(word, "is over the threshold")
    else: 
        return -1
    
    if len(commonWordsList) == 0:
        commonWordsList.append(word)
        wordListPercent.append(percentIndication)
    else: 
        commonWordsList.insert(findIndex(percentIndication), word)

def main():
    f = open("2020\commonWords3.txt", "w")
    f.write("")
    f.close()

    dictionary = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\Dictionary\top-34k.csv", engine= 'python') 
    word = ['@']
    index = dictionary['1']

    englishWords = len(word)
    print(englishWords)

    for i in range(0,englishWords,1):
        if len(word[i]) > requiredWordLength:
            sortWords(word[i])
            if index[i] % 1000 == 0:
                print("\nThe counter has reached: ", i, "\n")

    commonWordsList.reverse()

    for i in range(0,len(commonWordsList),1):
        printToFile(commonWordsList[i])

    final = {'String': commonWordsList, 'Word Count': wc, 'Good': goodl, 'Bad': badl, 'Percent Indication': pi,}

    df = pd.DataFrame(final)

    df.to_csv('2020\commonLinks3.csv')

main()