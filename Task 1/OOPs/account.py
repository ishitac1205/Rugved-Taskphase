class account:
    def __init__(self,bal,no):
        self.bal=bal
        self.no=no
    
    def debit(self,amt):
        self.bal=self.bal-amt
    def credit(self,amt):
        self.bal=self.bal+amt
    def balance(self):
        print(self.bal)

acc= account(100000,1234)
acc.debit(80000)
acc.credit(40000)
acc.balance()