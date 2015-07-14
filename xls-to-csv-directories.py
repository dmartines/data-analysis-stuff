import xlrd
import csv
import codecs
import os, sys

#path        = "D:/GoogleDrive/A-Lab/Data Analysis/Data_MIT_Team/AA_Social_Media/"
#filename    = "17th nov verbatim list.xls"

subfolders = ["June 14","July 14","Aug 14","Sep 14","Oct 14","Nov 14"]
subfolders = ["June 14"]
server_path = "D:/Data_MIT_Team/AA_Social_Mentions_Data/New/"
server_path = "C:/Users/Trader/Google Drive/A-Lab/Social Media Data/New/"

row_count = 0
row = []

for sub in subfolders:
    new_path = server_path + sub + "/"
    file_list = os.listdir(new_path)

    for filename in file_list:
        full_filename = new_path + filename
        if filename[-3:] <> "xls":
            pass
        else:
            print "Opening ", full_filename
            try:
                with xlrd.open_workbook(full_filename) as wb:
                    sh = wb.sheet_by_index(0)  # or wb.sheet_by_name('name_of_the_sheet_here')
                    with open(server_path + 'social_media_consolidated.csv', 'a') as f:
                        c = csv.writer(f)
                        for r in range(sh.nrows):
                            try:
                                row_line = []
                                row = ["1 " + sub] + [filename] + sh.row_values(r)
                                for row_content in row:
                                    try:
                                        row_line += [row_content.encode("utf-8")]                                        
                                    except:
                                        row_line += [row_content.decode("utf-8", errors="ignore")]
                                c.writerow(row_line)
                                row_count += 1
                            except AttributeError:
                                row_line = []
                                row = ["1 " + sub] + [filename] + sh.row_values(r)
                                for row_content in row:
                                    try:
                                        row_line += [row_content.encode("utf-8")]                                        
                                    except:
                                        row_line += [row_content.decode("utf-8", errors="ignore")]
                                c.writerow(row_line)
                                row_count += 1
                            except:
                                print "Error: ", sys.exc_info()[0]
                                pass
            except:
                pass
                            
print row_count