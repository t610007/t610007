from numpy import genfromtxt, savetxt
 
dataset = genfromtxt('tt.csv', delimiter = ',')
  for row in dataset:
    print (row)

name = input('請輸入你的名稱：')
