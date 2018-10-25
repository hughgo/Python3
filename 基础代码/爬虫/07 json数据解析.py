#
#
# 概念：一种保存数据的格式
# 作用：可以保存本地的json文件，也可以将json串进行传输
# 通常将json称为轻量级的传输方式
#
# xml
#
# json文件组成
# {}  代表对象（字典）
# []  代表列表
# ： 代表键值对
# ，  分割两个部分
import json
# jsonStr =  '{"name":"kai","age":18}'
# #将json格式的字符串转为python数据类型的对象
# jsonData = json.loads(jsonStr)
# print(jsonData)
# print(type(jsonData))
# print(jsonData["name"])

#将python数据类型的对象转为json格式的字符串
jsonData2 =  '{"name":"kai","age":18}'
jsonStr2 = json.dumps(jsonData2)
print(jsonData2)
print(type(jsonData2))

#读取本地的json文件
# path1 = r"C:\fle\json.json"
# with open(path1,"rb") as f:
#     data = json.load(f)
#     print(data)
#     #字典类型
#     print(type(data))

