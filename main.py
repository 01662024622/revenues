#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from datetime import datetime

from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from Connection.connection import Connection

from Entity.ht50_revenues import Revenues
from Util.calculationUtil import Calculation, sumOfMonth, checkLevel
from Env.env import Env

start_time = None
# config_time = int(os.environ["CONFIG_TIME_1578790800"])
config_time = 1578790800
#
# delay_time = int(os.environ["DELAY_TIME"])
# delay_time = 1
# int(os.environ["DELAY_TIME"])

# db_url_extract = str(os.environ["DB_URL_EXTRACT"])
db_url_extract = 'mysql://crm18246_thangvm:thangui0011@112.78.2.53:3306/crm18246_Test?charset=utf8&use_unicode=True'

# db_url_load = str(os.environ["DB_URL_LOAD"])
db_url_load = 'mssql+pyodbc://sa:j^d0Okem8BXfz%2MI$sWHWAk@192.168.1.241:1444/HTAUTO?driver=SQL Server Native Client 11.0?trusted_connection=yes?UID'

# delay_scheduel = int(os.environ["DELAY_SCHEDUEL"])
# delay_scheduel = 6400


extractConnection = Connection.connection(db_url_extract)
loadConnection = Connection.connection(db_url_load)
MONTH = 3
env = Env(MONTH)
Calculation = Calculation(MONTH)

# Need change month on env anh month on object revenues

# 'SET @row_number := 0; ' + \


# while True:
#     if start_time is None:
#         start_time = (int((int(
#             datetime.now().timestamp()) - 1578790800) / delay_scheduel)) * delay_scheduel + 1578790800 + config_time
#     else:
#         if start_time > int(datetime.now().timestamp()):
#             time.sleep(delay_time)
#         continue
time_report = datetime.now()
sql = text("select * from ht50_revenues")

sqlMonth = text(
    "select r.CustomerCode as code,c.[NV phụ tùng] role_pt,c.[NV dầu]  role_cs,SUM(r.payment) as sums from "
    "dbo.Receivables r  INNER JOIN Customer_list c ON r.CustomerCode=c.[Mã khách hàng] "
    "where " + env.getRangeMoth() + " group by r.CustomerCode,c.[NV phụ tùng],c.[NV dầu] order by sums")
data = extractConnection.execute(sql)
mapObject = {}
mapObjectCreate = {}
newMember = []
# olderMember = []
# // import revenus to array update
for line in data:
    d = Connection.dict2Object(line, Revenues())
    d.updated_time = time_report
    # olderMember.append(d.code)
    mapObject[d.code] = d

# set revenues this month to object or add new object to array check
monthResult = loadConnection.execute(sqlMonth)
for month in monthResult:
    if month.code in mapObject:
        older = mapObject[month.code]
        older = Calculation.setValue(older, month.sums)
        total = sumOfMonth(older)
        older.total = total
        older.coin = math.floor(total / 200000) + older.plus
        if total > older.period_pre:
            older.level = checkLevel(total)
        older.updated_at = time_report
        older.role_pt = month.role_pt
        older.role_cs = month.role_cs
        mapObject[month.code] = older
    else:
        newMember.append(month.code)
        revenue = Revenues()
        revenue.code = month.code
        revenue.setValueMonth(month.sums, MONTH)
        revenue.coin = math.floor(month.sums / 200000)
        revenue.level = checkLevel(month.sums)
        revenue.total = month.sums
        revenue.created_at = time_report
        revenue.updated_at = time_report
        revenue.role_pt = month.role_pt
        revenue.role_cs = month.role_cs
        mapObjectCreate[month.code] = revenue

# create new object with revenues 2020
# if (len(mapObject) > 0):
#     list = "','".join(olderMember)
#     print(len(olderMember))
#     print(list)
#     sqlTotal = text(
#         "select r.CustomerCode as code, SUM(r.payment) as period_pre from dbo.Receivables r "
#         "where r.DocDate>='2021-01-01' and r.DocDate<'2022-01-01' and r.CustomerCode IN ('" + list + "') group by r.CustomerCode")
#     resultTotal = loadConnection.execute(sqlTotal)
#     for d in resultTotal:
#         k = mapObject[d.code]
#         period_pre = d.period_pre
#         k.period_pre = period_pre
#         k.period_real = period_pre
#         k.level = checkLevel(period_pre)
#         mapObject[d.code] = k

if (len(mapObjectCreate) > 0):
    list = "','".join(newMember)
    sqlTotal = text(
        "select r.CustomerCode as code, SUM(r.payment) as period_pre from dbo.Receivables r "
        "where r.DocDate>='2021-01-01' and r.DocDate<'2022-01-01' and r.CustomerCode IN ('" + list + "') group by r.CustomerCode")
    resultTotal = loadConnection.execute(sqlTotal)
    for d in resultTotal:
        newObject = mapObjectCreate[d.code]
        period_pre = d.period_pre
        newObject.period_pre = period_pre
        newObject.period_real = period_pre
        if period_pre >= newObject.total:
            newObject.level = checkLevel(period_pre)
        else:
            newObject.level = checkLevel(newObject.total)
        mapObjectCreate[d.code] = newObject
Session = sessionmaker(bind=extractConnection)
session = Session()
i = 0

# update revenues
for d in mapObject.values():
    # session.query(Revenues).filter_by(code=d.code).update(
    #     {"period_real": d.period_real, "period_pre": d.period_pre, "total": d.total, "t1": d.t1, "t2": d.t2, "t3": d.t3,
    #      "t4": d.t4, "t5": d.t5, "t6": d.t6,
    #      "t7": d.t7, "t8": d.t8, "t9": d.t9, "t10": d.t10, "t11": d.t11, "t12": d.t12, "role_pt": d.role_pt,
    #      "role_cs": d.role_cs, "updated_at": d.updated_at, "level": d.level, "coin": d.coin})
    session.query(Revenues).filter_by(code=d.code).update(
        {"total": d.total, "t1": d.t1, "t2": d.t2, "t3": d.t3,
         "t4": d.t4, "t5": d.t5, "t6": d.t6,
         "t7": d.t7, "t8": d.t8, "t9": d.t9, "t10": d.t10, "t11": d.t11, "t12": d.t12, "role_pt": d.role_pt,
         "role_cs": d.role_cs, "updated_at": d.updated_at, "level": d.level, "coin": d.coin})
    i += 1
    if i % 500 == 0:
        print(i)
        session.commit()
if i % 500 != 0: session.commit()

for d in mapObjectCreate.values():
    session.add(d)
session.commit()

session.close()
loadConnection.close()
extractConnection.close()
