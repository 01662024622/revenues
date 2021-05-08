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
    created_at = Column('created_at', TIMESTAMP)
    updated_at = Column('updated_at', TIMESTAMP)

