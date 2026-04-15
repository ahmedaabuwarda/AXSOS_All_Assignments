class User:
    def __init__(self,name, email, balance):
        self.name = name
        self.email = email
        self.balance = 0
    
    def make_deposit(self, amount):
        self.balance = amount
        return self

    def make_withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            return "Can't withdraw!"

    def display_user_balance(self):
        return "User: " + self.name + " - balance: " + str(self.balance)
    
    def transfere_money(self, other_user, amount):
        self.make_withdrawal(amount=amount)
        other_user.make_deposit(amount)
        return self



roussom = User("Roussom", "test2@gmail.com", 0)
gudo = User("Gudo", "test@gmail.com", 0)
soob = User("Soob", "test3@gmail.com", 0)

roussom.make_deposit(120).make_deposit(20).make_deposit(11).make_withdrawal(45)

print(roussom.display_user_balance())

gudo.make_deposit(5).make_deposit(34).make_withdrawal(24).make_withdrawal(3)

print(gudo.display_user_balance())

soob.make_deposit(302).make_withdrawal(12).make_withdrawal(53).make_withdrawal(77)

print(soob.display_user_balance())

roussom.transfere_money(soob, 50)

print(roussom.display_user_balance())
print(soob.display_user_balance())