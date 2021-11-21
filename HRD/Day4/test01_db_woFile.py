from os import curdir
import time
import datetime
import pandas as pd
import pymysql 

print('-' * 150)
print('Current Time : ', datetime.datetime.now())
print('Maria DB Version : ', pymysql.version_info)  # version_info() 로 하면 오류
print('-' * 150)

bmi = pd.read_csv('../Data/data/bmi.csv')
print(bmi.info())
print(bmi.head())
print()

height = bmi['height']
weight = bmi['weight']
label = bmi['label']

try:
    config = {
        'host' : '127.0.0.1', 
        'user' : 'root',
        'password' : '8430',
        'database' : 'work',
        'port' : 3306,
        'charset' : 'utf8', 
        'use_unicode' : True
    }

    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = 'show tables'
    cursor.execute(sql)
    tables = cursor.fetchall()
    if tables:
        print(tables)
    else:
        print('Tables do not exist')
    print()

    sql = """
        create table if not exists goods (
            code int primary key, 
            name varchar(10) not null, 
            su int default 0
        );
    """

    cursor.execute(sql)
    print("Goods Table Created")
    dcode = 8889; dname = 'lee'; dsu = 5
    sql = f"insert into goods values({dcode},'{dname}',{dsu})"
    cursor.execute(sql)
    conn.commit()

except Exception as ex:
    print('DB Error : ', ex)