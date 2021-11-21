import time
import datetime
from typing import ClassVar
import pandas as pd
import pymysql 

print('-' * 100)

url='http://apis.data.go.kr/B551182/pubReliefHospService'
# access_key='BbZDsZoEIp%2B%2B%2Bu%2FJGYYIQa2dtgpUlN4B3Zi844czOx17ntS%2B0HmIN2Iwb%2F96Kf6jKQeuHgzSqBPIj2uh%2FObfnA%3D%3D'
# service_key=??

# Data field=row 가져와서 행단위, 열필드 저장 ClassVar