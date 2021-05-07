#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import os
import time
from datetime import datetime

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from ht50_revenues import Revenues
import xlrd
from xlrd import open_workbook, cellname

db_url_load = 'mysql://crm18246_thangvm:thangui0011@112.78.2.53:3306/crm18246_DATA?charset=utf8&use_unicode=True'




def dict2Revenues(d):
    v = Revenues()
    for k in d.keys():
        setattr(v, k, d[k])
    return v


def extractLoad(db_url, list_data):
    engine = create_engine(db_url, connect_args={'connect_timeout': 150}, echo=True)
    conn = engine.connect()

    Session = sessionmaker(bind=conn)
    session = Session()
    i = 0
    time_report = datetime.now()
    updated_time = str(time_report)
    for line in list_data:
        d = dict2Revenues(line)
        d.updated_time = updated_time
        session.add(d)
        i += 1
    if i > 0:
        session.commit()
    session.close()
    conn.close()

wb = open_workbook('1.xlsx')
sheet = wb.sheet_by_index(3)
print(sheet.cell_value(0, 0))

    extractLoad(db_url_load, data)
