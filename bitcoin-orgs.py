'''
Created on Jul 5, 2015

@author: Martines Daniel
'''
import re
import csv
from nltk.corpus import stopwords

stops = set(stopwords.words('english'))
stops = stops.union(['allows','make','best','way','lets','everyone','making'])

bitcoin_words = ['bitcoin','blockchain','litecoin','dogecoin','peercoin','eris','smart contract','ethereum']

tag_count = {}
tag_list = []

exchange = {}

with open('bitcoin-organizations.csv',newline='', encoding='utf-8', errors='ignore') as csvfile:
    line = csv.reader(csvfile)
    counter = 0
    for l in line:
        title = l[15].strip().split(' ')
        for t in title:
            if t.lower() in bitcoin_words:
                counter += 1
                wordlist = title
                for word in wordlist:
                    word = word.lower().strip()
                    replaced = re.sub("[.!-,;/:&]","", word)
                    if replaced not in stops:
                        tag_list.append(replaced)
                        if replaced in tag_count:
                            tag_count[replaced] += 1
                        else:
                            tag_count[replaced] = 1
                        exchange[l[3]] = l[15]
                        '''if replaced in ['card','cards']:
                             exchange[l[3]] = l[15]'''
                break


counter = 0
for company in exchange:
    counter += 1
    print(counter,') ',company, ': ', exchange[company])
           
'''
for tag in tag_list:
    if tag not in bitcoin_words:
        print(tag)
'''
#print(tag_list)
#tag_sorted = ((k, tag_count[k]) for k in sorted(tag_count, key=tag_count.get, reverse=True))
#for k, v in tag_sorted:
    #print(k,' ', v)