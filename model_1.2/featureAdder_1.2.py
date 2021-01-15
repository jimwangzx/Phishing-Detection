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

# Vowel list
vowelLetter = ['a', 'e', 'i', 'o', 'u']

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

def main():

    # Define features list
    length = [0]*(dataSize)
    vocab = [0]*(dataSize)
    slashes = [0]*(dataSize)
    doubSlash = [0]*(dataSize)
    atSymbol = [0]*(dataSize)
    periodCount = [0]*(dataSize)
    wLetter = [0]*(dataSize)
    vLetter = [0]*(dataSize)
    xLetter = [0]*(dataSize)
    zLetter = [0]*(dataSize)
    jLetter = [0]*(dataSize)
    qLetter = [0]*(dataSize)
    vowels = [0]*(dataSize)
    dotService = [0]*(dataSize)

    target = [0]*(dataSize)

    # Run loop for all variables
    for i in range(0,dataSize,1):
        # Print Progress
        if i % 10000 == 0:
            print('Loading...', int(i*100/dataSize), '%')

        # Feature: Length of string
        length[i] = len(f1[i])

        # Feature: Vocabulary addition
        vocab[i] = VocabCheck(f1[i])

        # Feature: counts '/'
        slashes[i] = f1[i].count('/')

        # Feature: Double slash
        doubSlash[i] = f1[i].count('//')
        
        # Feature: at symbol
        atSymbol[i] = f1[i].count('@')

        # Feature: Period count
        periodCount[i] = f1[i].count('.')

        # Feature: infrequent Letters
        wLetter[i] = f1[i].count('w')
        vLetter[i] = f1[i].count('v')
        xLetter[i] = f1[i].count('x')
        zLetter[i] = f1[i].count('z')
        jLetter[i] = f1[i].count('j')
        qLetter[i] = f1[i].count('q')

        # Feature: vowels
        for z in range(0,5,1):
            vowels[i] += f1[i].count(vowelLetter[z])

        # Feature: .edu or .org
        dotService[i] = f1[i].count('.edu') + f1[i].count('.org')

        # Change Label to integer
        if f2[i] == 'good':
            target[i] = 1

    print('Loading... 100 %')
    # Create final dataframe

    final = {'URL': f1, 'Length': length, 'CommonWords': vocab, 'Slashes': slashes, 'DoubleSlash': doubSlash, 'AtSymbol': atSymbol, 'PeriodCount': periodCount, 'WLetter': wLetter, 'VLetter': vLetter, 'XLetter': xLetter, 'ZLetter': zLetter, 'JLetter': jLetter, 'QLetter': qLetter, 'Vowels': vowels, 'DotService': dotService, 'Label': f2, 'Target': target}

    df = pd.DataFrame(final)

    df.to_csv('model_1.2/Model_1.2Dataset.csv')

main()