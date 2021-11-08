import requests
from urllib import parse
import sys
import xml.etree.ElementTree as ET
import pandas as pd

# Sample code from data.go.kr 

# import requests
# url = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList'
# params ={'serviceKey' : '서비스키', 'pageNo' : '1', 'numOfRows' : '10', 'spclAdmTyCd' : 'A0' }
# response = requests.get(url, params=params)
# print(response.content)

#serviceKey = 'BbZDsZoEIp+++u/JGYYIQa2dtgpUlN4B3Zi844czOx17ntS+0HmIN2Iwb/96Kf6jKQeuHgzSqBPIj2uh/ObfnA=='
serviceKey = '8z5o9xGOhxyngmxrnGripph9YNJNOwLezt%2BZg7N5TGElR0kCxny5TwyxNfqJ6cik8%2Fxa0rl52%2FH823b45CTQAw%3D%3D'
url = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList'

"""
params ={'serviceKey' : serviceKey, 'pageNo' : '1', 'numOfRows' : '10', 'spclAdmTyCd' : 'A0' }
response = requests.get(url, params=params)
#print(response.content)  >>> ERROR
print(response.text) 
"""

queryParam = f'?{parse.quote_plus("serviceKey")}={serviceKey}&' + parse.urlencode({
    parse.quote_plus('pageNo'):1, 
    parse.quote_plus('numOfRows'):10, 
    parse.quote_plus('spclAdmTyCd'):'A0'
})
#response = requests.get(url, params=queryParam) >>> ERROR
response = requests.get(url+queryParam)
print(response.text)
