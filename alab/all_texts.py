import csv

path = "C:/Users/Trader/Google Drive/A-Lab/Social Media Data/New/"
in_filename = "social_media_consolidated.csv"
all_txts_filename = "all_texts10.txt"

all_texts = [""]

with open(path + in_filename, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[11]:
            if all_texts:
                all_texts.extend([row[11] + "\r\n"])
            else:
                all_texts[row[11] + "\n"]

outfile = open(path + all_txts_filename, 'wb')
for text in all_texts:
    outfile.write(text)

#writer = csv.writer(open(path + all_txts_filename, 'wb'))
#writer.writerow(all_texts)
