import pandas as pd
from statistics import mean

path='./Day2/data/sam_kospi.xlsx'
SM = pd.read_excel(path)
#print(SM.info())
print(SM.head())

high = SM['High']
low = SM['Low']
max = mean(high)
min = mean(low)
print('MAX : ', max)
print('MIN : ', min)
