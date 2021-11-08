import requests
from urllib import parse
import sys
import xml.etree.ElementTree as ET
import pandas as pd

key = 'OeC48XV7KHpbnMFj%2Bh810Ka9eigFZjZlXhQstMj9Mu15UDTaFQ3yw%2Bc90MuTWIGcENNWUGmo7h1GeJtuh7o1%2FA%3D%3D'
url_slight = 'http://openapi.jeonju.go.kr/rest/saftylight/getSaftylight'

for cnt in range(100):
    queryParams_n = f'?{parse.quote_plus("ServiceKey")}={key}&' + parse.urlencode({
        parse.quote_plus('startPage') : cnt, 
        parse.quote_plus('pageSize'): 150,
    })
    
    res = requests.get(url_slight + queryParams_n)
    root = ET.fromstring(res.text) 
    list1 = root.find('body/data')
   
    result= []
    try:
        for item in list1:
            BDong=item.find('BDong').text 
            detailAddr=item.find('detailAddr').text
            estaType=item.find('estaType').text
            flashType=item.find('flashType').text
            HDong=item.find('HDong').text
            lampCap1=item.find('lampCap1').text
            lampLife=item.find('lampLife').text
            lampType1=item.find('lampType1').text
            lightCnt=item.find('lightCnt').text
            lineNum=item.find('lineNum').text
            lotNumber=item.find('lotNumber').text
            manageNo=item.find('manageNo').text
            lon=item.find('posx').text 
            lat=item.find('posy').text 
            #print()
            msg=[manageNo]+[lon]+[lat]+[BDong]+[detailAddr]+[estaType]+[flashType]+[HDong]+[lampCap1]+[lampLife]+[lampType1]+[lightCnt]+[lineNum]+[lotNumber] 
            result.append(msg)
    except Exception as ex:
        print('에러발생 ', ex)
        print(cnt)
        break
        
    try:
        frame=pd.DataFrame(result, columns=['manageNo','lon','lat','BDong','detailAddr','estaType','flashType','HDong','lampCap1','lampLife','lampType1','lightCnt','lineNum','lotNumber'])
        if cnt==0:
            frame.to_csv('./data/jcity_slight_test1.csv' , encoding='utf-8', mode='w', index=False)  
            print('./data/jcity_slight_test1.csv  파일저장처리중... ')
        else:
            frame.to_csv('./data/jcity_slight_test1.csv' , encoding='utf-8', mode='a', index=False)        
    except Exception as ex:
        print('./data/jcity_slight_test1.csv저장에러 ', ex)


print('./data/jcity_slight_test1.csv저장완료')