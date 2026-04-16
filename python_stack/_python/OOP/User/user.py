class User:
    def __init__(self,name, email, balance=0):
        self.name = name
        self.email = email
        self.balance = balance
    
    def make_deposit(self, amount):
        self.balance = amount

    def make_withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            return "Can't withdraw!"

    def display_user_balance(self):
        return "User: " + self.name + " - balance: " + str(self.balance)
    
    def transfere_money(self, other_user, amount):
        self.make_withdrawal(amount=amount)
        other_user.make_deposit(amount)



roussom = User("Roussom", "test2@gmail.com", 0)
gudo = User("Gudo", "test@gmail.com", 0)
soob = User("Soob", "test3@gmail.com", 0)

roussom.make_deposit(120)
roussom.make_deposit(20)
roussom.make_deposit(11)

roussom.make_withdrawal(45)

print(roussom.display_user_balance())

gudo.make_deposit(5)
gudo.make_deposit(34)

gudo.make_withdrawal(24)
gudo.make_withdrawal(3)

print(gudo.display_user_balance())

soob.make_deposit(302)

soob.make_withdrawal(12)
soob.make_withdrawal(53)
soob.make_withdrawal(77)

print(soob.display_user_balance())


roussom.transfere_money(soob, 50)

print(roussom.display_user_balance())
print(soob.display_user_balance())