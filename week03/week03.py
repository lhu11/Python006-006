    
# -*- coding: utf-8 -*-
'''
2. 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:
用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
将 ORM、插入、查询语句作为作业内容提交
'''
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String,DateTime,Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker


dburl = "mysql+pymysql://test:123456@192.168.43.102:3306/db"
engine = create_engine(dburl, echo=True, encoding="utf-8")
Base = declarative_base()
class User_table(Base):
    __tablename__ = 'userinfo'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), index=True)
    age = Column(Integer())
    birthday = Column(Date(), nullable=False)
    gender = Column(String(10))
    degree = Column(String(50))
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print("create error {e}")

#插入数据
db= pymysql.connect(host="192.168.43.102",user="test", password="123456",db="db",port=3306)

try:
    with db.cursor() as cursor:
        sql = '''INSERT INTO userinfo (name, age,birthday, gender, degree, created_time) VALUES (%s, %s, %s, %s, %s, %s)'''
        value = (
            ('lhu', 22, datetime(2001, 5, 1),'male', 'ben', datetime.now()),
            ('yhy', 23, datetime(2002, 8, 4),'male', 'ben', datetime.now()),
            ('lyt', 32, datetime(1988, 1, 12),'male', 'ben' ,datetime.now())
        )
        cursor.executemany(sql, value)
    db.commit()

except Exception as e:
    print(f"fetch_error: {e}")

finally:
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)
#查询
try:
    with db.cursor() as cursor:
        sql = '''SELECT * FROM userinfo'''
        cursor.execute(sql)
        users = cursor.fetchall()
        for user in users:
            print(user)
    db.commit()

except Exception as e:
    print(f"fetch_error: {e}")

finally:
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)
