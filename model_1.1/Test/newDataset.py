import pandas as pd
import string

data = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\model_1.1\Model_1.1Dataset.csv", engine= 'python') 
#Features include ,URL,Length,Length225,CommonWords,Slash10,PeriodCount,DoubleSlash,AtSymbol,Label,Target
f1 = data['URL']
f2 = data['Label']
f3 = data['Length']
f4 = data['Length225']
f5 = data['CommonWords']
f6 = data['Slash10']
f7 = data['PeriodCount']
f8 = data['DoubleSlash']
f9 = data['AtSymbol']
f10 = data['Target']
dataSize = len(f1)

x = 0

# Run loop for all variables
for i in range(0,dataSize,1):
    if f4[i] != 0 or f5[i] != 0 or f6[i] != 0 or f7[i] != 0 or f8[i] != 0 or f9[i] !=0:
        
        x += 1

print("x = ", x, "\nPercentage = ", x*100/dataSize)

y = 0

indexes = [0]*x
for i in range(0,dataSize,1):
    if f4[i] != 0 or f5[i] != 0 or f6[i] != 0 or f7[i] != 0 or f8[i] != 0 or f9[i] !=0:
        indexes[y] = i
        y += 1

print("\n\ndone indexing\n\n")

dataSize = x 
url = [0]*(dataSize) 
lab = [0]*(dataSize)
len225 = [0]*(dataSize) 
vocab = [0]*(dataSize)
slashes = [0]*(dataSize)
periodCount = [0]*(dataSize)
doubSlash = [0]*(dataSize)
atSymbol = [0]*(dataSize)
length = [0]*(dataSize)
target = [0]*(dataSize)

y = 0


for j in indexes:
    url[y] = f1[j]
    length[y] = f3[j]
    len225[y] = f4[j]
    vocab[y] = f5[j]
    slashes[y] = f6[j]
    periodCount[y] = f7[j]
    doubSlash[y] = f8[j]
    atSymbol[y] = f9[j]
    lab[y] = f2[j]
    target[y] = f10[j]

    y += 1

# Create final dataframe

final = {'URL': url, 'Length': length, 'Length225': len225, 'CommonWords': vocab, 'Slash10': slashes, 'PeriodCount': periodCount, 'DoubleSlash': doubSlash, 'AtSymbol': atSymbol, 'Label': lab, 'Target': target}

df = pd.DataFrame(final)

df.to_csv('model_1.1/Test/FixedModel_1.1Dataset.csv')