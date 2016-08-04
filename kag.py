import csv  
with open('test.csv','rb') as myFile:  
    lines=csv.reader(myFile)  
    for line in lines:  
        print line
print ('hello world')
name = input('請輸入你的名稱：')
print('歡迎 ', name)
