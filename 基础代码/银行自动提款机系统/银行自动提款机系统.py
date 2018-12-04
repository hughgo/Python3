'''
人
类名：Person
属性：姓名  身份证号 电话号  卡
行为：

卡
类名：Card
属性：卡号 密码  余额
行为：

取款机
类名： ATM
属性：用户字典
行为：开户、查询、取款、存款、转账、改密、锁定、解锁、补卡、销户


管理员
类名：admin
属性：
行为：管理员界面 管理员验证  系统功能界面
'''
import time
from admin import Admin
from atm import ATM
import pickle
import os
from card import Card
from user import User

def main():
    # 管理员对象
    view = Admin()
    # 管理员开机
    view.printAdminView()

    if view.adminOption():
        return -1
    print("登陆成功!")
    time.sleep(1)

    #提款机对象
    filePath = os.path.join(os.getcwd(), "alluser.txt")
    f= open(filePath,"rb")
    allUser = pickle.load(f)

    atm=ATM(allUser)


    while True:
        view.printsysFunctionView()
        #等待用户操作
        option =input("请输入您的选择：")
        if option =="1":
            atm.createUser()
            time.sleep(1)
        elif option=="2":
            atm.searchUserInfo()
            time.sleep(1)
        elif option == "3":
            atm.getMoney()
        elif option == "4":
            atm.saveMoney()
        elif option == "5":
            atm.transferMoney()
        elif option == "6":
            print('改密')
        elif option == "7":
            atm.lockUser()
        elif option == "8":
            atm.unlockUser()
        elif option == "9":
            print('补卡')
        elif option == "0":
            print('销户')
        elif option == 'Q':
            if not view.adminOption():

                #将当前的用户信息保存到文件中

                f= open(filePath,"wb")
                pickle.dump(atm.allUser,f)
                f.close()
                print('退出成功！')
                return -1
        time.sleep(2)
if __name__=="__main__":
    main()