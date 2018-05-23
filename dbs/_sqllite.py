#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'LY'

import sqlite3
import os

conn = None
cursor = None
try:
    conn = sqlite3.connect('test1.db')
    cursor = conn.cursor()
    cursor.execute('DROP table STUDENT')
    cursor.execute('CREATE TABLE  STUDENT ('
                   'ID VARCHAR(20) PRIMARY KEY,'
                   'NAME VARCHAR(20))')
    cursor.execute("INSERT INTO STUDENT (ID,NAME) VALUES ('1','Ly')")
    print(cursor.rowcount)
    cursor.execute("select * from STUDENT where NAME='Ly'")
    rs = cursor.fetchall()
    print(rs)
    conn.commit()
except IOError as io_err:
    print('出错....')
finally:
    if cursor is None:
        try:
            cursor.close()
        except ConnectionError:
            pass
    if conn is None:
        try:
            conn.close()
        except ConnectionError:
            pass
# 作业
db_file = os.path.join(os.path.dirname(__file__), 'test2.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    conn1 = None
    cursor1 = None
    result = []
    try:
        conn1 = sqlite3.connect(db_file)
        cursor1 = conn1.cursor()
        cursor1.execute('select name from user where score between %d and %d order by score asc ' % (low, high))
        rs = cursor1.fetchall()
        for k in rs:
            result.append(k[0])
        print(result)
        conn1.commit()
    except IOError as io_err:
        print('出错....')
    finally:
        if cursor1 is None:
            try:
                cursor1.close()
            except ConnectionError:
                pass
        if conn1 is None:
            try:
                conn1.close()
            except ConnectionError:
                pass
    return result
# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')