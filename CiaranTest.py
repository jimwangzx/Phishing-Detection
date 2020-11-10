import numpy as np
import csv
import pandas as pd

dataSet1 = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\ciarandataset.csv") 
feature1 = dataSet1['URL']



strLengthList = []

for i in range(0,549346,1):
    strLengthList.append(len(feature1[i]))

for i in range(0,549346,1):
    strLengthList[i] = strLengthList[i]/max(strLengthList)

dataSet1['Length'] = strLengthList
print(dataSet1.head(10))

dataSet1.to_csv('lengthData.csv')