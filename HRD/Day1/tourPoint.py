import urllib.request
import datetime
import time
import math
import json
from config import *
import pandas as pd

def get_request_url(url, enc='utf-8'):        
    req = urllib.request.Request(url)
    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc,'replace')
            return ret
    except Exception as e:
        print(e) 
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None


def getTourPointVisitor(yyyymm, sido, gugu, nPangeNum, nItems):
    url = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
    parameter =  '?_type=json&serviceKey='+serviceKey
    parameter += '&YM='+yyyymm
    parameter += '&SIDO='+ urllib.parse.quote(sido)
    parameter += '&GUNGU='+ urllib.parse.quote(gugu)
    parameter += '&RES_NM=&pangeNo='+ str(nPangeNum)
    parameter += '&numOfRows=' + str(nItems)
    url = url + parameter
    retData = get_request_url(url)

    if retData != None:
        json_data = json.loads(retData)
    return json_data


#########################################################################################################  
result = []  
print()
print('-' * 70)
print('tourpoint.csv 파일저장중입니다 ...잠시 기다려 주세요')

for year in range(2012,2013):
    for month in range(1,13):
        yyyymm = "{0}{1:0>2}".format(str(year), str(month))
        nPagenum =1
        while True :
            jsonData = getTourPointVisitor(yyyymm, '서울특별시','',nPagenum, 100)
            if( jsonData['response']['header']['resultMsg'] =='OK'):
                totalCount = jsonData['response']['body']['totalCount']
                if totalCount == 0: break
                
                for item in jsonData['response']['body']['items']['item']:
                    sido ='' if 'sido' not in item.keys() else item['sido']
                    gungu ='' if 'gungu' not in item.keys() else item['gungu']
                    resNm = '' if 'resNm' not in item.keys() else item['resNm']
                    rnum = 0 if 'rnum' not in item.keys() else item['rnum']
                    addrCd =0 if 'addrCd' not in item.keys() else item['addrCd']
                    csForCnt =0 if 'csForCnt' not in item.keys() else item['csForCnt']
                    csNatCnt =0 if 'csNatCnt' not in item.keys() else item['csNatCnt']
                    if 'csNatCnt' in item.keys():
                        result.append([yyyymm]+[sido]+[gungu]+[resNm]+[addrCd]+[csForCnt]+[csNatCnt])
                nPage = math.ceil(totalCount/100)    
                if(nPagenum == nPage):                    
                    break
                nPagenum = nPagenum +1        
            else:
                break

#########################################################################################################  
# with open("tourpoint.json",'w', encoding='UTF-8-sig') as f:
#    f.write(json.dumps(json_data, ensure_ascii=False))

pd.DataFrame(result).to_csv('tourpoint.csv', encoding='cp949', header=None, index=False)
print('tourpoint.csv 파일저장처리작업이 완료 되었습니다')