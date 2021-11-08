# File handling 

import os
import time

print(os.getcwd())
# print('-' * 20)
# time.sleep(2)
# print('+' * 20)
# #print(help(open))
# help(open)

path='./Day2/data/ftest.txt'

ftest = open(path, mode='r', encoding='utf-8')
data = ftest.read()
print(data)
ftest.close()

# WITH OPEN does not need CLOSE 
with open(path, mode='w', encoding='utf-8') as fdata:
    fdata.write('TESTESSETSE \n')
    fdata.write('asdf a sdfsadf  \n')
print(path, 'Saved Successfully')