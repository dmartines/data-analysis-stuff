import csv
import nltk
from nltk.corpus import stopwords

stops = set(stopwords.words('english'))
stops = stops.union(['rt', "i'm",''])

path = "C:/Users/Trader/Google Drive/A-Lab/Social Media Data/New/"
in_filename = "social_media_consolidated.csv"
post_by_date_file = "post_by_date.csv"

post_by_date_count = {}
key = ""

with open(path + in_filename, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[9].strip():
            date = row[5].split("-")
            if len(date) > 1:
                day_txt = date[0]
                month_txt = date[1]
                year_text = date[2][:4]
                if "twitter" in row[9]:
                    key = "twitter|"
                elif "facebook" in row[9]:
                    key = "facebook|"
                else:
                    key = "other|"
                key += year_text + "|" + month_txt + "|" + day_txt
                if key in post_by_date_count:
                    post_by_date_count[key] += 1
                else:
                    post_by_date_count[key] = 1

writer = csv.writer(open(path + post_by_date_file, 'wb'))
for key, value in post_by_date_count.items():
    writer.writerow([key, value])
        