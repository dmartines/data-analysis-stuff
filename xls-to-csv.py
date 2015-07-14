import xlrd
import csv
import codecs
import os

path        = "C:/Users/Trader/Google Drive/A-Lab/Data Analysis/Data_MIT_Team/AA_Social_Media/"
path        = "C:/Users/Trader/Google Drive/A-Lab/Data Analysis/Data_MIT_Team/AA_Txn_Data/Output/Product Adoption Curves/Patterns/Blockbusters/"
#filename    = "17th nov verbatim list.xls"

file_list = os.listdir(path)

for filename in file_list:
    with xlrd.open_workbook(path + filename) as wb:
        sh = wb.sheet_by_index(0)  # or wb.sheet_by_name('name_of_the_sheet_here')
        with open(path + 'social_media_consolidated.csv', 'a') as f:
            c = csv.writer(f)
            for r in range(sh.nrows):
                try:
                    r = r.encode('ascii', 'ignore').decode('ascii')
                    c.writerow(sh.row_values(r))
                except AttributeError:
                    try:
                        c.writerow(sh.row_values(r))
                    except UnicodeEncodeError:
                        print "error"