from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt
 dataset = genfromtxt('tt.csv', delimiter = ',', dtype = 'none')


  for row in dataset:
    print (row)

name = input('請輸入你的名稱：')
