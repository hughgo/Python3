from card import Card
from user import User
import random
class ATM(object):
    def __init__(self,allUser):
        self.allUser=allUser #卡号对应的数字
    #开户
    def createUser(self):
        name=input('请输入您的姓名：')
        idCard= input('请输入身份证号码：')
        phone = input('请输入电话号码：')

        prestoreMoney=int(input('请输入预存款金额：'))
        if prestoreMoney<0:
            print('预存款输入有误，开户失败。。。')
            return -1
        onePasswd = input('请设置密码：')
        #验证密码
        if not self.checkPasswd(onePasswd):
            print('密码输入错误，开户失败。。。')
            return -1
        #所有需要的信息就全了
        cardStr= self.randomCardid()
        card= Card(cardStr,onePasswd,prestoreMoney)
        user =User(name,idCard,phone,card)
        #存到字典
        self.allUser[cardStr]=user
        print("开户成功！！请牢记卡号：%s" % cardStr)
    #查询
    def searchUserInfo(self):
        cardNum = input('请输入您的卡号：')
        #验证是否存在该卡号
        user= self.allUser.get(cardNum)
        if not user:
            print("该卡号不存在，查询失败！")
            return -1
        #判断是否被锁定
        if user.card.cardLock:
            print('该卡已被锁定，请解锁后使用！')
            return -1
        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误。该卡已被锁定，请解锁后使用。。。")
            user.card.cardLock=True
            return -1
        print("账号：%s  余额：%d "% (user.card.cardId,user.card.cardMoney))

    #取款
    def getMoney(self):
        cardNum = input('请输入您的卡号：')
        # 验证是否存在该卡号
        user = self.allUser.get(cardNum)
        if not user:
            print("该卡号不存在，取款失败！")
            return -1
        # 判断是否被锁定
        if user.card.cardLock:
            print('该卡已被锁定，请解锁后使用！')
            return -1
        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误。该卡已被锁定，请解锁后使用。。。")
            user.card.cardLock = True
            return -1

        money = int(input('请输入取款金额：'))
        if money>user.card.cardMoney:
            print('余额不足，取款失败！')
            return -1
        if money<= 0:
            print('输入错误！')
            return  -1
        #取款
        user.card.cardMoney-=money
        print('取款成功！余额：%d'%(user.card.cardMoney))

    #存款
    def saveMoney(self):
        cardNum = input('请输入您的卡号：')
        # 验证是否存在该卡号
        user = self.allUser.get(cardNum)
        if not user:
            print("该卡号不存在，取款失败！")
            return -1
        # 判断是否被锁定
        if user.card.cardLock:
            print('该卡已被锁定，请解锁后使用！')
            return -1
        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误。该卡已被锁定，请解锁后使用。。。")
            user.card.cardLock = True
            return -1
        money = int(input('请输入存款金额：'))
        # 存款
        user.card.cardMoney += money
        print('存款成功！余额：%d' % (user.card.cardMoney))
    #转账
    def transferMoney(self):
        pass
    #改密
    def changePasswd(self):
        pass
    #锁定
    def lockUser(self):
        cardNum = input('请输入您的卡号：')
        # 验证是否存在该卡号
        user = self.allUser.get(cardNum)
        if not user:
            print("该卡号不存在，查询失败！")
            return -1
        if user.card.cardLock:
            print('该卡已被锁定！请解锁后再使用！')
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误。锁定失败。。。")
            return -1
        tempIdCard = input('请输入您的身份证号码：')
        if tempIdCard != user.idCard:
            print("身份证号输入错误。锁定失败。。。")
            return -1
        #锁定
        user.card.cardLock=True
        print('该卡已被锁定！')
    #解锁
    def unlockUser(self):
        cardNum = input('请输入您的卡号：')
        # 验证是否存在该卡号
        user = self.allUser.get(cardNum)
        if not user:
            print("该卡号不存在，解锁失败！")
            return -1
        if not user.card.cardLock:
            print('此卡没有锁定！无需解锁！')
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误。解锁失败。。。")
            return -1
        tempIdCard = input('请输入您的身份证号码：')
        if tempIdCard != user.idCard:
            print("身份证号输入错误。解锁失败。。。")
            return -1
        #解锁
        user.card.cardLock=False
        print('解锁成功！')

    #补卡
    def newCard(self):
        pass
    #销户
    def kilUser(self):
        pass

    #验证密码
    def checkPasswd(self,realPasswd):
        for i in range(3):
            tempPasswd =input('请输入密码：')
            if tempPasswd == realPasswd:
                return True
        return False

    #生成卡号
    def randomCardid(self):
        while True:
            str =""
            for i in range(6):
                ch = chr(random.randrange(ord('0'),ord('9')+1))
                str+=ch
            #判断是否重复
            if not self.allUser.get(str):
                return str
