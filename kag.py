from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt
 dataset = genfromtxt(open('tt.csv', 'r'), delimiter = ',', dtype = 'f8')[1:]
 target = [x[0] for x in dataset] # 第一列为label
 train = [x[1:] for x in dataset]

  for row in dataset:
    print (row)

name = input('請輸入你的名稱：')
