import pandas as pd
import string
from itertools import permutations

# Read Dataset
data = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\model_1.1\urls.csv", engine= 'python') 
f1 = data['URL']
f2 = data['Label']
dataSize = 549346

# Read Common Words List
links = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\model_1.1\commonString.csv", engine= 'python') 
commonWord = links['String']
g1 = links['Good']
t1 = links['Word Count']

def VocabCheck(url):
    # define variables
    goodWordsFound = 0
    badWordsFound = 0
    
    # Run through the list of common words
    for i in range (0,len(commonWord),1):
        if url.find(commonWord[i]) >= 0:
            # if found state whether word is good or bad
            if g1[i] > t1[i] - g1[i]:
                goodWordsFound += 1
            else:
                badWordsFound += 1

    #Determine the final result
    if badWordsFound > 0 and goodWordsFound > 0:
        return 0
    elif goodWordsFound > 0:
        return 1
    elif badWordsFound > 0:
        return -1
    else:
        return 0

def Slash10(url):
    if url.count('/') > 10:
        return 1
    else:
        return 0
def main():

    # Define features list
    len225 = [0]*(dataSize) 
    vocab = [0]*(dataSize)
    slashes = [0]*(dataSize)
    periodCount = [0]*(dataSize)
    doubSlash = [0]*(dataSize)
    atSymbol = [0]*(dataSize)
    length = [0]*(dataSize)
    target = [0]*(dataSize)

    # Run loop for all variables
    for i in range(0,dataSize,1):
        # Print Progress
        if i % 10000 == 0:
            print('Loading...', int(i*100/dataSize), '%')

        # Feature: Length of string
        length[i] = len(f1[i])

        # Feature: Lengths above 225
        if len(f1[i]) > 225:
            len225[i] = 1

        # Feature: Vocabulary addition
        vocab[i] = VocabCheck(f1[i])

        # Feature: above 10 '/'
        slashes[i] = Slash10(f1[i])

        # Feature: Double slash
        if f1[i].count('//') > 0:
            doubSlash[i] = 1
        
        # Feature: at symbol
        if f1[i].count('@') > 0:
            atSymbol[i] = 1

        # Feature: Period count
        if f1[i].count('.') > 8:
            periodCount[i] = 1

        # Change Label to integer
        if f2[i] == 'good':
            target[i] = 1


    print('Loading... 100 %')
    # Create final dataframe

    final = {'URL': f1, 'Length': length, 'Length225': len225, 'CommonWords': vocab, 'Slash10': slashes, 'PeriodCount': periodCount, 'DoubleSlash': doubSlash, 'AtSymbol': atSymbol, 'Label': f2, 'Target': target}

    df = pd.DataFrame(final)

    df.to_csv('model_1.1/Model_1.1Dataset.csv')

main()