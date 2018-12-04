import  time
class Admin(object):
    admin="admin"
    passwd="admin"

    def printAdminView(self):
        print("*******************************************************")
        print("*                                                     *")
        print("*                                                     *")
        print("*                 欢迎登陆浅笑私人银行                *")
        print("*                                                     *")
        print("*                                                     *")
        print("*******************************************************")


    def printsysFunctionView(self):
        print("*******************************************************")
        print("*         开户（1）                 查询（2）          *")
        print("*         取款（3）                 存款（4）          *")
        print("*         转账（5）                 改密（6）          *")
        print("*         锁定（7）                 解锁（8）          *")
        print("*         补卡（9）                 销户（0）          *")
        print("*                       退出（Q）                      *")
        print("*******************************************************")
    def adminOption(self):
        inputAdmin = input('请输入管理员账号:')
        inputPasswd = input('请输入管理员密码:')
        if self.admin == inputAdmin:
            if self.passwd == inputPasswd:
                print('正在进行，请稍后。。。')
                time.sleep(3)
                return 0
        # 能执行到这里表示账号密码正确
        print('账号或密码错误')
        return -1
