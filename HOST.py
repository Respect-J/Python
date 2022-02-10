from random import randint

a = "welcome to ATM simulator"
print("first register your account")
print("first register your account")

name = input('your name: ')
password = int(input('create password: '))
id_card = randint(8600000000000000, 8600999999999999)
balance = int(input('enter balance: '))
print("you registered")


class BANK:
    def __init__(self):
        self.name = name
        self.password = password
        self.id = id_card
        self.balance = balance

    def show_balance(self):
        show = self.balance
        print(show)

    def cash_out(self):
        minus = int(input('enter the amount: '))
        user_password = int(input('your password: '))
        while user_password != self.password:
            user_password = int(input('wrong password, please enter again: '))
        if user_password == self.password:
            self.balance -= minus
            print(f'your balance {self.balance}')
        elif user_password != self.password:
            print('wrong password')

    def top_up_balance(self):
        plus = int(input('enter the replenishment amount: '))
        self.balance += plus
        print(self.balance)

    def cash_transfer(self):
        user_transfer = int(input('Enter card id: '))
        if len(str(user_transfer)) == 16:
            transfer = int(input('sum of transfer'))
            self.balance -= transfer
        elif len(str(user_transfer)) != 16:
            print('not users')
        else:
            print('not users')


user = BANK()
while True:
    print("1.Balance | 2.cash out | 3.Top up balance | 4.cash transfer | 5.exit ")
    user_action = int(input('choose an action: '))
    if user_action == 1:
        user.show_balance()
    elif user_action == 2:
        user.cash_out()
    elif user_action == 3:
        user.top_up_balance()
    elif user_action == 4:
        user.cash_transfer()
    elif user_action == 5:
        break
#  elif user_action == 2:
