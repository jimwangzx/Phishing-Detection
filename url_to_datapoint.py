import pandas as pd
import numpy as np
import tldextract
import re

links = pd.read_csv("data/commonString.csv") 
commonWord = links['String']
g1 = links['Good']
t1 = links['Word Count']

def extract(url):
  extraction_data = {}
  extraction = tldextract.extract(url)

  extraction_data['subdomain'] = extraction.subdomain
  extraction_data['domain'] = extraction.domain
  extraction_data['suffix'] = extraction.suffix
  extraction_data['domain_name'] = extraction.domain + "." + extraction.suffix

  path_regex = re.compile(r'(\w+://){,1}/((/|.)+)')
  try:
    path = path_regex.search(url).group(0)
    extraction_data['path'] = path
  except AttributeError:
    extraction_data['path'] = ''
  return extraction_data
    
def VocabCheck(url, commonWord, g1, t1):
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
    return -1
  elif badWordsFound > 0:
    return 1
  else:
    return 0

def substring_has_domain(substring):
  count = substring.count('.com')
  count += substring.count('.net')
  count += substring.count('.ca')
  count += substring.count('.php')
  count += substring.count('.www')
  return count

def url_to_data(url):
  global commonWord
  global t1
  global g1
  data = []
  data.append(url.count('.'))
  data.append(url.count('/'))
  data.append(url.count('//'))
  data.append(url.count('@'))
  data.append(len(url))
  data.append(sum(c.isdigit() for c in url))
  data.append(int(url[0].isdigit()))

  data.append(url.count('w'))
  data.append(url.count('v'))
  data.append(url.count('x'))
  data.append(url.count('z'))
  data.append(url.count('j'))
  data.append(url.count('q'))

  data.append(substring_has_domain(extract(url)['path']))

  data.append(int(re.search('(?:\d{1,3}\.){3}\d{1,3}', url) is not None))
  data.append(url.count(';'))

  domains = ['.com', '.net', '.ca', '.html', '.exe', '.xyz', '.php', '.rar']
  data.append(sum(substring in url for substring in domains))

  vowelLetter = ['a', 'e', 'i', 'o', 'u']
  data.append(sum(letter in vowelLetter for letter in url))
  data.append(url.count('.edu') + url.count('.org'))

  data.append(int(re.search('[0-9a-f]{64}|[0-9a-f]{32}', url) is not None))

  data.append(VocabCheck(url, commonWord, g1, t1))
  return data
