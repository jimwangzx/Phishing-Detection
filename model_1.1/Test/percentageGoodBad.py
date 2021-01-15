import pandas as pd
import string

data = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\model_1.1\Model_1.1Dataset.csv", engine= 'python') 
#Features include ,URL,Length,Length225,CommonWords,Slash10,PeriodCount,DoubleSlash,AtSymbol,Label,Target
f1 = data['URL']
f2 = data['Target']
dataSize = len(f2)

good = 0

for y in range(0,dataSize,1):
    if f2[y] == 1:
        good += 1

print("\nGood = ", good, "\nPercentage = ", good*100/dataSize)
print("\nBad = ", dataSize-good, "\nPercentage = ", 100-good*100/dataSize, "\n\n")
