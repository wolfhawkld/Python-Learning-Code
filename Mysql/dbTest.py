import pymysql
# 校验 用户输入的用户名和密码是否正确
# 去数据库里取数据做判断
# 1.连上数据库,获得的conn是连接
conn = pymysql.connect(host="localhost", port=3306, database="damon_test", user="root", password="123456", charset="utf8")
# 只有连接还不行,还需要获取光标,让我能够输入sql语句并执行
cursor=conn.cursor()    #cursor是光标
# 2.执行sql语句
sql="select * from test;"    #要执行的sql语句写出来
ret = cursor.execute(sql)   #execute是执行的意思,执行sql语句
# 3.关闭光标和连接
data = cursor.fetchall()
cursor.close()
conn.close()

print("%s row in set (0.00 sec)" % ret)
for row in data:
    print(type(row))
    print(row)

