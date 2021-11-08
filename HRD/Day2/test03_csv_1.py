# CSV File Handling 

import pandas as pd
path='./Day2/data/bmi.csv'

bmi_data = pd.read_csv(path, encoding='utf-8')
# print(bmi_data.head())
# print(bmi_data.tail())

h = bmi_data['height']
w = bmi_data.weight
print('height : ', sum(h), ' weight : ', sum(w))


# ftest = open(path, mode='r', encoding='utf-8')
# data = ftest.read()
# print(data)
# ftest.close()