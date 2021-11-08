import urllib.request
import datetime
import json
from config import *
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

def get_request_url(url, enc='utf-8'):        
    req = urllib.request.Request(url)
    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"% datetime.datetime.now())
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

def getNatVisitor(yyyymm, nat_cd, ed_cd):
    url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    parameter = '?_type=json&serviceKey='+serviceKey
    parameter += '&YM='+yyyymm
    parameter += '&NAT_CD='+nat_cd
    parameter += '&ED_CD='+ed_cd
    url = url + parameter
    #print(url)
    retData = get_request_url(url)
    if retData == None:
        None
    else:
        return json.loads(retData) 

result = []
for year in range(2015,2016):
    for month in range(1,13):
        yyyymm = '{0}{1:0>2}'.format(str(year), str(month))
        json_data= getNatVisitor(yyyymm, '275', 'E')
        if (json_data['response']['header']['resultMsg']=='OK'):
            natKorNm = json_data['response']['body']['items']['item']['natKorNm']
            natKorNm = natKorNm.replace(' ','')
            num = json_data['response']['body']['items']['item']['num']
            print("%s_%s : %s" %(natKorNm, yyyymm, num))
            result.append([yyyymm]+[natKorNm]+['275']+[num])


pd.DataFrame(result).to_csv('%s_해외방문자_%s' %(natKorNm, '2015')+'.csv',
      encoding='cp949', header=None, index=False)


cnVisit = []
visitYM = []
index = []
i = 0
for item in result:
    index.append(i)
    cnVisit.append(item[3])
    visitYM.append(item[0])
    i=i+1


font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

plt.figure(figsize=(12,6))   
plt.xticks(index, visitYM)
plt.plot(index, cnVisit)
plt.xlabel('방문월')
plt.ylabel('방문객수')
plt.grid(True)
plt.show()