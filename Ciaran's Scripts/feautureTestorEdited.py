import pandas as pd
import os
import string

dirname = os.path.dirname(__file__)

data = pd.read_csv(os.path.join(dirname,"../data/phishing_site_urls.csv"), engine= 'python') 
f1 = data['URL']
f2 = data['Label']
dataSize = len(f1)

percentCompletion = 0
bad = 0
good = 0

# Change these variables
numList = ['.de']
minimum = 1

print("The minimum is: ", minimum)

for i in range(0,dataSize,1):
    # State Completion Rate
    if i %(int(dataSize/10)) == 0:
        print('At', percentCompletion, '%')
        percentCompletion += 10
    elif i == dataSize-1:
        print("Done... Preparing results\n")
    
    # Each individual string determining
    count = 0

    titleURL = f1[i]
    if f1[i].count('/') == 0:
        URLlength = len(f1[i])
    else:
        URLlength = f1[i].index('/')

    titleURL = titleURL[0:URLlength]

    for x in range (0,len(numList),1):
        count += titleURL.count(numList[x])

    if count >= minimum:
        if f2[i] == 'good':
            good += 1
        else:
            bad += 1

# print to console
print('Good = ', good, '\nBad = ', bad, '\nTotal = ', bad + good, '\nPercent Indication = ', good*100/(bad+good))

#print to file

#add to file
#line = str(numList) + "\tMinimum: " + str(minimum) + "\tTotal Links: " + str(good+bad) + "\tGood Samples: " + str(good) + "\tBad Samples: " + str(bad) + "\tPercent Indication: " + str(int(good*10000/(good+bad))/100) + "\n"

#fi = open("General\StringResults.txt", "a")
#fi.write(line)
#fi.close()