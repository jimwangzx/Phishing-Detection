import pandas as pd
import string

commonWordsList = ['Hi', 'Jeff']
wc = [1, 2]

final = {'String': commonWordsList, 'Word Count': wc}

df = pd.DataFrame(final)

df.to_csv('commonLinks1.csv')