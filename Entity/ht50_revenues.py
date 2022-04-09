#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, BigInteger, TIMESTAMP, String
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Revenues(Base):
    __tablename__ = 'ht50_revenues'
    id = Column('id', BigInteger, primary_key=True)
    code = Column('code', String)
    role_pt = Column('role_pt', String)
    role_cs = Column('role_cs', String)
    level = Column('level', String)
    total = Column('total', BigInteger, default=0)
    coin = Column('coin', Integer, default=0)
    period_pre = Column('period_pre', Integer, default=0)
    period_real = Column('period_real', Integer, default=0)
    t1 = Column('t1', Integer, default=0)
    t2 = Column('t2', Integer, default=0)
    t3 = Column('t3', Integer, default=0)
    t4 = Column('t4', Integer, default=0)
    t5 = Column('t5', Integer, default=0)
    t6 = Column('t6', Integer, default=0)
    t7 = Column('t7', Integer, default=0)
    t8 = Column('t8', Integer, default=0)
    t9 = Column('t9', Integer, default=0)
    t10 = Column('t10', Integer, default=0)
    t11 = Column('t11', Integer, default=0)
    t12 = Column('t12', Integer, default=0)
    plus = Column('plus', Integer, default=0)
    created_at = Column('created_at', TIMESTAMP)
    updated_at = Column('updated_at', TIMESTAMP)

    def getValueMonth(self, month):
        if month == 1:
            return self.t1
        if month == 2:
            return self.t2
        if month == 3:
            return self.t3
        if month == 4:
            return self.t4
        if month == 5:
            return self.t5
        if month == 6:
            return self.t6
        if month == 7:
            return self.t7
        if month == 8:
            return self.t8
        if month == 9:
            return self.t9
        if month == 10:
            return self.t10
        if month == 11:
            return self.t11
        if month == 12:
            return self.t12

    def setValueMonth(self, value, month):
        if month == 1:
            self.t1 = value
            return
        if month == 2:
            self.t2 = value
            return
        if month == 3:
            self.t3 = value
            return
        if month == 4:
            self.t4 = value
            return
        if month == 5:
            self.t5 = value
            return
        if month == 6:
            self.t6 = value
            return
        if month == 7:
            self.t7 = value
            return
        if month == 8:
            self.t8 = value
            return
        if month == 9:
            self.t9 = value
            return
        if month == 10:
            self.t10 = value
            return
        if month == 11:
            self.t11 = value
            return
        if month == 12:
            self.t12 = value
            return
