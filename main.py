#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import os
import time
from datetime import datetime

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from Connection.connection import Connection

from ht50_revenues import Revenues

start_time = None
# config_time = int(os.environ["CONFIG_TIME_1578790800"])
config_time = 1578790800
#
# delay_time = int(os.environ["DELAY_TIME"])
# delay_time = 1
# int(os.environ["DELAY_TIME"])

# db_url_extract = str(os.environ["DB_URL_EXTRACT"])
db_url_extract = 'mysql://crm18246_thangvm:thangui0011@112.78.2.53:3306/crm18246_DATA?charset=utf8&use_unicode=True'

# db_url_load = str(os.environ["DB_URL_LOAD"])
db_url_load = 'mssql+pyodbc://sa:j^d0Okem8BXfz%2MI$sWHWAk@192.168.1.241/HTAUTO?driver=SQL Server Native Client 11.0?trusted_connection=yes?UID'

# delay_scheduel = int(os.environ["DELAY_SCHEDUEL"])
# delay_scheduel = 6400

time_report = datetime.now()

extractConnection = Connection.connection(db_url_extract)
loadConnection = Connection.connection(db_url_load)


# 'SET @row_number := 0; ' + \

def extractLoad(db_url, list_data, var):
    if var == 0:
        loadConnection.execute(text('TRUNCATE teacher_rating_300;'))
    Session = sessionmaker(bind=loadConnection)
    session = Session()
    i = 0
    updated_time = str(time_report)
    for line in list_data:
        d = Connection.dict2Object(line, Revenues())
        d.updated_time = updated_time
        session.add(d)
        i += 1
    if i > 0:
        session.commit()
    session.close()
    loadConnection.close()


def checkLevel(revenue):
    if revenue >= 2000000000:
        return "Platinum"
    elif revenue >= 1000000000:
        return "Gold"
    elif revenue >= 500000000:
        return "Titan"
    elif revenue >= 200000000:
        return "Silver"
    else:
        return "Member"


def y2021(row):
    return row.t1 + row.t2 + row.t3 + row.t4 + \
           row.t5 + row.t6 + row.t7 + row.t8 + \
           row.t9 + row.t10 + row.t11 + row.t12


# while True:
#     if start_time is None:
#         start_time = (int((int(
#             datetime.now().timestamp()) - 1578790800) / delay_scheduel)) * delay_scheduel + 1578790800 + config_time
#     else:
#         if start_time > int(datetime.now().timestamp()):
#             time.sleep(delay_time)
#         continue

sql = text("select * from ht50_revenues")

sqlMonth = text(
    "select r.CustomerCode as code,r.Role_PT as role_pt,r.Role_CS as role_cs,SUM(r.payment) as sums from dbo.Receivables r where r.DocDate>='2021-04-01' and r.DocDate<'2021-05-01' group by r.CustomerCode,r.Role_PT,r.Role_CS order by sums")
data = extractConnection.execute(sql)
mapObject = {}
for line in data:
    d = Connection.dict2Object(line, Revenues())
    d.updated_time = time_report
    mapObject[d.code] = d
monthResult = loadConnection.execute(sqlMonth)
for month in monthResult:
    if month.code in mapObject:
        object = mapObject[month.code]
        object.t4 = month.sums
        object.coin = object.coin + month.sums / 200000
        if object.total > y2021(object):
            object.level = checkLevel(object.total)
        else:
            object.level = checkLevel(y2021(object))
        object.updated_at = time_report
        object.role_pt = month.role_pt
        object.role_cs = month.role_cs
        mapObject[month.code] = object
    else:
        revenue = Revenues()
        revenue.t4 = month.sums
        revenue.coin = month.sums / 200000
        revenue.level = checkLevel(month.sums)
        revenue.created_at = time_report
        revenue.updated_at = time_report
        revenue.role_pt = month.role_pt
        revenue.role_cs = month.role_cs
        mapObject[month.code] = revenue
Session = sessionmaker(bind=extractConnection)
session = Session()
i = 0
for d in mapObject.values():
    print(d)
    session.add(d)
    i += 1
    if i > 0 & (i % 500 == 0):
        print(i)
        session.commit()
if i % 500 != 0: session.commit()

session.close()
loadConnection.close()
extractConnection.close()
