d1={1:'a', 2:'b', 3:'c'}
d1[4]='d'
if 'b' in d1:
    print("b is in d1")
else:
    print("b is not in d1")
if 4 not in d1:
    print("4 is not in d1")
else:
    print("4 is in d1")

# "b is not in d1"
# 4 is in d1

class BankAccount():
    def __init__(self, acct_num, balance=0.0):
        self.acct_num=acct_num
        self.balance=0.0
    def withdraw(self, amount):
        self.balance-=amount
    def deposit(self, amount):
        self.balance+=amount
    def get_balance(self):
        return self.balance
def main():
    acct1 = BankAccount("1234")
    print(acct1.get_balance())
    acct1.deposit(100.50)
    print(acct1.get_balance())
    acct1.withdraw(50)
    print(acct1.get_balance())


