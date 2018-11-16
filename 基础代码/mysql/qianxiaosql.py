import pymysql

class Qianxiaosql():
    def __init__(self,host,user,passwd,dbName):
        self.host =host
        self.user =user
        self.passwd = passwd
        self.dbName = dbName

    def connet(self):
        self.db = pymysql.connect(self.host,self.user,self.passwd,self.dbName)
        self.cursor =  self.db.cursor()
    def close(self):
        self.cursor.close()
        self.db.close()
    def get_one(self,sql):
        res= None
        try:
            self.connet()
            self.cursor.execute(sql)
            res= self.cursor.fetchone()
            self.close()
        except:
            print('查询失败')

        return res
    def get_all(self,sql):
        res=()
        try:
            self.connet()
            self.cursor.execute(sql)
            res= self.cursor.fetchall()
            self.close()
        except:
            print('查询失败')
        return res

    def insert(self,sql):
        return self.edit(sql)
    def update(self,sql):
        return self.edit(sql)
    def delete(self,sql):
        return self.edit(sql)
    def edit(self,sql):
        count =0
        try:
            self.connet()
            count=self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print('提交失败')
            self.db.rollback()

        return count