import csv
with open('tt.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:
    print (row)

name = input('請輸入你的名稱：')
