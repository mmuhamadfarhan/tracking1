import csv
import os
with open('bursa_scraping.csv', newline='') as infile, open('beauty_bursa_scraping.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter=',')
    writer = csv.writer(outfile, delimiter='|')
    for row in reader:
        writer.writerow(row)
        
        

os.remove("bursa_scraping.csv")
os.rename('beauty_bursa_scraping.csv','bursa_scraping.csv')
print("Success")

