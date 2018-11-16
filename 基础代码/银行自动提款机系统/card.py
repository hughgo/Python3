class Card(object):
    def __init__(self,cardId,cardPasswd,cardMoney):
        self.cardId =cardId
        self.cardPasswd =cardPasswd
        self.cardMoney =cardMoney
        self.cardLock =False