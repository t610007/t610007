import csv  
with open('tt.csv','rb') as myFile:  
    lines=csv.reader(myFile)  
    for line in lines:  
        print line

name = input('請輸入你的名稱：')
