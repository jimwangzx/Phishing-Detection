import numpy as np
import csv
import pandas as pd

dataSet1 = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\ciarandataset.csv") 
feature1 = dataSet1['URL']
feature2 = dataSet1['Label']

strLengthList = []
bgI = []

for i in range(0,549346,1):
    strLengthList.append(len(feature1[i]))
    if feature2[i] == 'bad':
        bgI.append(0)
    if feature2[i] == 'good':
        bgI.append(1)

for i in range(0,549346,1):
    strLengthList[i] = strLengthList[i]/max(strLengthList)

dataSet1['Length'] = strLengthList
dataSet1['GoodBadInteger'] = bgI
print(dataSet1.head(10))

dataSet1 = dataSet1.sample(frac=1)

dataSet1.to_csv('lengthData.csv')