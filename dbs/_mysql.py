#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'LY'

import mysql.connector as connector

conn = None
cursor = None
try:
    conn = connector.connect(user='ytj', password='5391848', database='ytj')
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