import pymysql

#连接数据库
#参数1：mysql服务器所在主机的ip
#参数2：用户名
#参数3：密码
#参数4：要连接的数据库名
db= pymysql.connect("localhost",'root','root','security')

#创建一个cursor对象
cursor  = db.cursor()

sql = "select database()"

#执行sql语句
cursor.execute(sql)

#获取返回的信息
data = cursor.fetchone()
print(data)



sql="insert into bandcard values(0,100000)"
try:
    cursor.execute(sql)
    db.commit()
except:
    #如果提交失败，回滚到上一次的数据
    db.rollback()
#断开
cursor.close()
db.close()