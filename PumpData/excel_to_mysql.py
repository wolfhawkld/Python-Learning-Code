import pymysql
import xlrd
# 本地import
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import Mysql.dbTest
# Global Prams:
HOST = "127.0.0.1"
PORT = 3306
DB_NAME = "test"
DB_USER = "root"
DB_PWD = "QAws12"
DB_CHARSET = "utf8"
BASE_DIR = "C:\\Users\\M293906\\Documents\\Project\\MConnect\\Data\\"
OBJ_NAME = "Dup_Rep"
EXCEL_TYPE = ".xlsx"
FILE_NAME = BASE_DIR + OBJ_NAME + EXCEL_TYPE

# 1.从Msql的API创建Mysql连接
conn = Mysql.dbTest.Conn(HOST, PORT, DB_NAME, DB_USER, DB_PWD, DB_CHARSET)
cursor=conn.cursor()    

# 2.Excel to Mysql
wb = xlrd.open_workbook(FILE_NAME)
sh = wb.sheet_by_index(0)
dfun=[]
nrows = sh.nrows  
ncols = sh.ncols  
fo=[]

fo.append(sh.row_values(0))
for i in range(1,nrows):
      dfun.append(sh.row_values(i))
# 创建table
cursor.execute("create table " + OBJ_NAME +"("+fo[0][0]+" varchar(100));")
#创建table属性
for i in range(1,ncols):
    cursor.execute("alter table " + OBJ_NAME + " add "+fo[0][i]+" varchar(100);")
val=''
for i in range(0,ncols):
    val = val+'%s,'
# print(dfun)
cursor.executemany("insert into " + OBJ_NAME + " values("+val[:-1]+");" ,dfun)
conn.commit()


# 3.关闭光标和连接
sql="select * from " + OBJ_NAME + ";"  
ret = cursor.execute(sql)   
data = cursor.fetchmany(10)
cursor.close()
conn.close()

# 4.验证结果
# TO DO: 根据实际情况返回需要验证的数据量
# print("%s row in set (0.00 sec)" % ret)
for row in data:
    # print(type(row))
    print(row)

