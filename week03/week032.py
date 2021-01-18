#!/usr/bin/env python

'''
6. 张三给李四通过网银转账 100 极客币，现有数据库中三张表：
一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。
请合理设计三张表的字段类型和表结构；
请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。
'''

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, create_engine, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
class User(Base):
    uid = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=True, unique=True)

class asset(Base):
    uid = Column(Integer(), primary_key=True, nullable=True)
    asset = Column(DECIMAL(19, 4), nullable=True)

class Transaction(Base):
    id1 = Column(Integer(), primary_key=True)
    id2 = Column(Integer(), primary_key=True)
    num = Column(DECIMAL(19, 4), nullable=True)
    create_date = Column(DateTime(), nullable=True)


def deal(one, other, deal, session):
    id1 = session.query(User.uid).filter(Use.name == one).one()[0]
    id2 = session.query(User.uid).filter(User.name == other).one()[0]
    mon1 = session.query(Asset.asset).filter(Asset.uid==id1, Asset.asset>deal).one()[0]
    mon2 = session.query(Asset.asset).filter(Asset.uid==id2).one()[0]

    one_mon -= deal
    other_mon += deal
    session.query(Asset.asset).filter(Asset.uid==one_id).update({Asset.asset: one_mon})
    session.query(Asset.asset).filter(Asset.uid == other_id).update({Asset.asset: other_mon})

    transaction = Transaction_table(id1=id1,
                         id2=id2,
                         create_date=datetime.now(),
                         deal=deal)
    session.add(transaction)

if __name__ == '__main__':
    db_url = "mysql+pymysql://test:123456@192.168.43.102:3306/db?charset=utf8mb4"
    engine = create_engine(db_url, echo=True, encoding='utf-8')
    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()
    Base.metadata.create_all(engine)

    try:
        deal('张三','李四', 100, session)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()
