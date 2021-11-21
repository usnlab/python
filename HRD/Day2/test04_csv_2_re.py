# CSV File Handling 

import pandas as pd
import re   # 정규식 

path='./Day2/data/spam_data.csv'
texts=''
target=''
try:
    #spam_data = pd.read_csv(path, encoding='utf-8')
    spam_data = pd.read_csv(path, encoding='ms949', header=None)
    print(spam_data.info())
except Exception as ex:
    print('Error : ', ex)

def clean_txt(txt_str):
    txt_re = re.sub('[,.?!:;]','', txt_str)
    txt_re = re.sub('[◆[@/#$%*^()]','', txt_re)
    txt_re = re.sub('[a-z]|[A-Z]','', txt_re)
    txt_re = ''.join(txt_re.split())    # 공백 제거 
    return txt_re

clean_txt_data = [clean_txt(t) for t in texts]