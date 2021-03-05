import pandas as pd
import string, os
from itertools import permutations

dirname = os.path.dirname(__file__)

# Read Dataset
data = pd.read_csv(os.path.join(dirname,"../data/phishing_site_urls.csv")) 
f1 = data['URL']
f2 = data['Label']
dataSize = 549346

# Read Common Words List
links = pd.read_csv(os.path.join(dirname,"../data/commonString3.csv"), engine= 'python') 
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
    
    # Run through the list of common words
    for i in range (0,len(commonWord),1):
        if url.find(str(commonWord[i])) >= 0:
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
    paypal = [0]*(dataSize)
    semicolon = [0]*(dataSize)
    dash = [0]*(dataSize)
    qmark = [0]*(dataSize)
    firstPartNumbers = [0]*(dataSize)


    target = [0]*(dataSize)

    # Run loop for all variables
    for i in range(0,dataSize,1):
        if i % int(dataSize/100) == 0:
            print('Loading...', int(i*100/dataSize), '%')

        # Feature: Length of string
        if len(f1[i]) < 60:
            length[i] = 0
        elif len(f1[i]) < 120:
            length[i] = 1
        elif len(f1[i]) < 225:
            length[i] = 2
        else:
            length[i] = 3

        # Feature: Vocabulary addition
        vocab[i] = VocabCheck(f1[i])

        # Feature: Paypal finder
        paypal[i] = f1[i].count('paypal')
        
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

        # Feature: Question Mark
        qmark[i] = f1[i].count('?')

        # Feature: - and ;
        dash[i] = f1[i].count('-')
        semicolon[i] = f1[i].count(';')

        # Feature: Numbers in first section
        titleURL = f1[i]
        firstPartNumbersCount = 0
        if f1[i].count('/') == 0:
            URLlength = len(f1[i])
        else:
            URLlength = f1[i].index('/')

        titleURL = titleURL[0:URLlength]

        for n in range (0,len(numList),1):
            firstPartNumbersCount += titleURL.count(numList[n])

        firstPartNumbers[i] = firstPartNumbersCount

        # Change Label to integer
        if f2[i] == 'good':
            target[i] = 1

    print('Loading... 100 %')
    # Create final dataframe

    final = {'URL': f1, 'Length': length, 'CommonWords': vocab, 'Paypal': paypal, 'Slashes': slashes, 'DoubleSlash': doubSlash, 'AtSymbol': atSymbol, 'QuestionMark': qmark, 'Dash': dash, 'Semicolon': semicolon, 'PeriodCount': periodCount, 'WLetter': wLetter, 'VLetter': vLetter, 'XLetter': xLetter, 'ZLetter': zLetter, 'JLetter': jLetter, 'QLetter': qLetter, 'Vowels': vowels, 'FirstPartNumbers': firstPartNumbers, 'Target': target}

    df = pd.DataFrame(final)

    df.to_csv(os.path.join(dirname, '../data/Model_1.3Dataset.csv'))

main()