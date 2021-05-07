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
    level = Column('level', String)
    rate_avg = Column('rate_avg', DOUBLE)
    total = Column('total', BigInteger)
    coin = Column('coin', Integer)
    t1 = Column('t1', Integer)
    t2 = Column('t2', Integer)
    t3 = Column('t3', Integer)
    t4 = Column('t4', Integer)
    t5 = Column('t5', Integer)
    t6 = Column('t6', Integer)
    t7 = Column('t7', Integer)
    t8 = Column('t8', Integer)
    t9 = Column('t9', Integer)
    t10 = Column('t10', Integer)
    t11 = Column('t11', Integer)
    t12 = Column('t12', Integer)
    updated_time = Column('updated_time', TIMESTAMP)