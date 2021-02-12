import pandas as pd
import string, os
from itertools import permutations

dirname = os.path.dirname(__file__)

# Read Dataset
data = pd.read_csv(os.path.join(dirname,"../data/phishing_site_urls.csv")) 
f1 = data['URL']
f2 = data['Label']
dataSize = len(f1)

# Read Common Words List
links = pd.read_csv(os.path.join(dirname,"../data/commonString.csv"), engine= 'python') 
commonWord = links['String']
g1 = links['Good']
t1 = links['Word Count']
peri = links['Percent Indication']

# Lists
vowelLetter = ['a', 'e', 'i', 'o', 'u']
numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def VocabCheck(url):
    # define variables
    goodWordsFound = 0
    badWordsFound = 0
    avgPeri = 0
    # Run through the list of common words
    for i in range (0,len(commonWord),1):
        if url.find(commonWord[i]) >= 0:
            # if found state whether word is good or bad
            if g1[i] > t1[i] - g1[i]:
                goodWordsFound += 1
                avgPeri = (avgPeri*(goodWordsFound-1)+peri[i]/100)/goodWordsFound
            else:
                badWordsFound += 1
                avgPeri = (avgPeri*(badWordsFound-1)+peri[i]/100)/badWordsFound

    #Determine the final result
    if badWordsFound > 0 and goodWordsFound > 0:
        return 0
    else:
        return avgPeri

def main():

    # Define features list
    length = [0]*(dataSize)
    vocab = [0]*(dataSize)
    slashes = [0]*(dataSize)
    periodCount = [0]*(dataSize)
    letter = [0]*(dataSize)
    symbols = [0]*(dataSize)
    numbers = [0]*(dataSize)

    target = [0]*(dataSize)

    # Run loop for all variables
    for i in range(0,dataSize,1):
        # Print Progress
        if i % int(dataSize/100) == 0:
            print('Loading...', int(i*100/dataSize), '%')

        # Feature: Length of string
        if len(f1[i]) < 60:
            length[i] = 0
        else:
            length[i] = len(f1[i])
        
        # Feature: Vocab Check
        vocab[i] = VocabCheck(f1[i])

        # Feature: counts '/'
        slashes[i] = f1[i].count('/') + 2*f1[i].count('//')

        # Feature: Period count
        periodCount[i] = f1[i].count('.')

        # Feature: Infrequent Letters
        letter[i] = f1[i].count('w') + f1[i].count('v') + f1[i].count('x') + f1[i].count('z') + f1[i].count('j') + f1[i].count('q')

        # Feature: symbols
        symbols[i] = f1[i].count('@') + f1[i].count('?') + f1[i].count('-') + f1[i].count(';')

        # Feature: symbols
        for digit in numList:
            numbers[i] += f1[i].count(digit)

        # Change Label to integer
        if f2[i] == 'good':
            target[i] = 1

    print('Loading... 100 %')
    # Create final dataframe

    final = {'URL': f1, 'Length': length, 'Vocab': vocab, 'Slashes': slashes, 'PeriodCount': periodCount, 'Letter': letter, 'Symbol': symbols, 'Target': target}

    df = pd.DataFrame(final)

    df.to_csv(os.path.join(dirname, '../data/Model_1.4Dataset.csv'))

main()