from os import curdir
import time
import datetime
import pandas as pd
import pymysql 

print('-' * 100)
# print('Current Time : ', datetime.datetime.now())
# print('Maria DB Version : ', pymysql.version_info)  # version_info() 로 하면 오류
# print('-' * 100)

bmi = pd.read_csv('../Data/data/bmi.csv')
# print(bmi.dtypes)
# print(bmi.head())
# print()
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

    sql = """
        create table if not exists bmi_table(
            height int not null, 
            weight int not null, 
            label varchar(12) not null
        )
    """
    cursor.execute(sql)

    sql = 'delete from bmi_table'
    cursor.execute(sql)
    conn.commit()
    
    for i in range(100):
        h = height[i]
        w = weight[i]
        l = label[i]

        sql = f"insert into bmi_table values({h},{w},'{l}')"
        cursor.execute(sql)
        conn.commit()

    sql = 'select * from bmi_table' 
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows: 
        print(row[0],'-', row[1], '-', row[2])

except Exception as ex:
    print('DB Error : ', ex)