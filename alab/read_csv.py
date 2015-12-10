import csv
import nltk
from nltk.corpus import stopwords

stops = set(stopwords.words('english'))
stops = stops.union(['rt', "i'm",''])

path = "C:/Users/Trader/Google Drive/A-Lab/Social Media Data/New/"
in_filename = "social_media_consolidated.csv"
tw_wc_filename = "twitter_word_count.csv"
tw_users_filename = "twitter_users.csv"
fb_wc_filename = "facebook_word_count.csv"
fb_users_filename = "facebook_users.csv"

twitter_word_count = {}
twitter_users = {}
facebook_word_count = {}
facebook_users = {}

with open(path + in_filename, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if "twitter" in row[9]:
            handle = row[16][19:]
            if handle not in stops:
                if handle in twitter_users:
                    twitter_users[handle] += 1
                else:
                    twitter_users[handle] = 1
            text_content = row[11].strip().split(" ")
            for text in text_content:
                text = text.lower().replace('&quot;','').replace("\n"," ").strip()
                if text[:4] == 'http':
                    text = text.translate(None,',!.?-|').strip()
                else:
                    text = text.translate(None,',!.:?-/|').strip()
                if text not in stops:
                    if text in twitter_word_count:
                        twitter_word_count[text] += 1
                    else:
                        twitter_word_count[text] = 1
        if "facebook" in row[9]:
            handle = row[15].strip()
            if handle not in stops:
                if handle in facebook_users:
                    facebook_users[handle] += 1
                else:
                    facebook_users[handle] = 1
            text_content = row[11].strip().split(" ")
            for text in text_content:
                text = text.lower().replace('&quot;','').replace("\n"," ").strip()
                if text[:4] == 'http':
                    text = text.translate(None,',!.?-|').strip()
                else:
                    text = text.translate(None,',!.:?-/|').strip()
                if text not in stops:
                    if text in facebook_word_count:
                        facebook_word_count[text] += 1
                    else:
                        facebook_word_count[text] = 1

# Twitter csv file
writer = csv.writer(open(path + tw_wc_filename, 'wb'))
for key, value in twitter_word_count.items():
    writer.writerow([key, value])
        
writer = csv.writer(open(path + tw_users_filename, 'wb'))
for key, value in twitter_users.items():
    writer.writerow([key, value])
        
# Facebook csv file
writer = csv.writer(open(path + fb_wc_filename, 'wb'))
for key, value in facebook_word_count.items():
    writer.writerow([key, value])
        
writer = csv.writer(open(path + fb_users_filename, 'wb'))
for key, value in facebook_users.items():
    writer.writerow([key, value])
        