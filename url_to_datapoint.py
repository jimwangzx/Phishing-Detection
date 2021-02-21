import pandas as pd
import numpy as np
import os

dirname = os.path.dirname(__file__)

links = pd.read_csv(os.path.join(dirname,"./data/commonString.csv"), engine= 'python') 
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


def url_to_datapoint(url):
    
    # Feature: Length of string
        length = len(url)

        # Feature: Vocabulary addition
        vocab = VocabCheck(url)

        # Feature: counts '/'
        slashes = url.count('/')

        # Feature: Double slash
        doubSlash = url.count('//')
        
        # Feature: at symbol
        atSymbol = url.count('@')

        # Feature: Period count
        periodCount = url.count('.')

        # Feature: infrequent Letters
        wLetter = url.count('w')
        vLetter = url.count('v')
        xLetter = url.count('x')
        zLetter = url.count('z')
        jLetter = url.count('j')
        qLetter = url.count('q')

        # Feature: vowels
        vowelLetter = ['a', 'e', 'i', 'o', 'u']
        vowels = 0
        for z in range(0,5,1):
            vowels += url.count(vowelLetter[z])

        # Feature: .edu or .org
        dotService = url.count('.edu') + url.count('.org')

        final = np.array([length, vocab, slashes, doubSlash, atSymbol, periodCount, wLetter, vLetter, xLetter, zLetter, jLetter, qLetter, vowels, dotService])
        return final

