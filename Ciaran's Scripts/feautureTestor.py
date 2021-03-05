import pandas as pd
import os
import string

dirname = os.path.dirname(__file__)

data = pd.read_csv(os.path.join(dirname,"../data/phishing_site_urls.csv"), engine= 'python') 
f1 = data['URL']
f2 = data['Label']
dataSize = 549346

bad = 0
good = 0

# Change these variables
numList = ['.com', '.net', '.org', '.co', '.uk', '.us', '.gov', '.edu', '.info', '.biz', '.me']
minimum = 3

print("The minimum is: ", minimum)
time = 0

for i in range(0,dataSize,1):
    if i % int(dataSize/20) == 0:
        print('At ', time, '%')
        time += 5
    elif i == 549345:
        print("Done... Preparing results\n\n")
    
    count = 0
    for x in range (0,len(numList),1):
        count += f1[i].count(numList[x])

    if count >= minimum:
        if f2[i] == 'good':
            good += 1
        else:
            bad += 1

# print to console
print('Good = ', good, '\nBad = ', bad, '\nTotal = ', bad + good, '\nPercent Indication = ', good*100/(bad+good))

#print to file

#add to file
line = str(numList) + "\tMinimum: " + str(minimum) + "\tTotal Links: " + str(good+bad) + "\tGood Samples: " + str(good) + "\tBad Samples: " + str(bad) + "\tPercent Indication: " + str(int(good*10000/(good+bad))/100) + "\n"

fi = open("General\StringResults.txt", "a")
fi.write(line)
fi.close()