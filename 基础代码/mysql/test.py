from qianxiaosql import Qianxiaosql


s= Qianxiaosql("127.0.0.1",'root','root','security')
res= s.get_all("select *from bandcard where money>300")
for row in res:
    print("%d--%d" % (row[0], row[1]))