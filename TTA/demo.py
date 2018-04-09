# coding=utf-8

import xlrd
import pymssql
import time
from TTA.GUID import GUID

def read_excel():
    conn=pymssql.connect(host='127.0.0.1',user='sa',password='123456',database='NJBXTTA')
    cur = conn.cursor()

    ExcelFile=xlrd.open_workbook(r'G:\BaoSlight\insert.xlsx')
    sheet=ExcelFile.sheet_by_name('Sheet1')
    print (sheet.name, sheet.nrows, sheet.ncols )  # 名称 行数 列数

    insert_arr = []

    for i in range(1, sheet.nrows):
        rows = sheet.row_values(i)
        # print(rows)
        insert_arr.append(
            ("徐浪", time.strftime("%Y%m%d%H%M%S"), '', '', '', "GT01",  GUID.new_uuid(upper_=False)  , rows[1], rows[2], '0', rows[4], rows[5], '', '', '', '', '', '')
        )

        # print(rows)

    for i, value in enumerate(insert_arr):
        print(value)

    # cur.executemany(
    #     "INSERT INTO "
    #     "TTADI00([REC_CREATOR],[REC_CREATE_TIME],[TRADE_ENAME],[ITEM_SEQ],[ITEM_ENAME],[ITEM_CNAME],[ITEM_GRADE],[ITEM_TYPE],[ITEM_LEN]) "
    #     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
    #     insert_arr)
    #
    cur.executemany(
        "INSERT INTO "
        "TTADI00 "
        "VALUES (%s, %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        insert_arr)


    conn.commit()

    cur.close()
    conn.close()
read_excel()