from BankAccount import BankAccount

class User:
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account = {
            "savings": BankAccount(name="savings", balance=0, interest_rate=0), 
            "current": BankAccount(name="current", balance=0, interest_rate=0.02)
        }
    
    def make_deposit(self, amount):
        self.account["savings"].deposit(amount)
        # self.balance = amount
        return self

    def make_withdrawal(self, amount):
        if self.account["savings"].get_balance() >= amount:
            self.account["savings"].withdraw(amount)
            return self
        else:
            return "Can't withdraw!"

    def display_user_balance(self):
        return "User: " + self.name + " - balance: " + str(self.account["savings"].get_balance())
    
    def transfere_money(self, other_user, amount):
        self.make_withdrawal(amount=amount)
        other_user.make_deposit(amount)
        return self



roussom = User("Roussom", "test2@gmail.com")
gudo = User("Gudo", "test@gmail.com")
soob = User("Soob", "test3@gmail.com")

roussom.make_deposit(120)
roussom.make_deposit(20)
roussom.make_deposit(10)

roussom.make_withdrawal(40)

print(roussom.display_user_balance())

gudo.make_deposit(5)
gudo.make_deposit(35)

gudo.make_withdrawal(20)
gudo.make_withdrawal(5)

print(gudo.display_user_balance())

soob.make_deposit(302)

soob.make_withdrawal(12)
soob.make_withdrawal(53)
soob.make_withdrawal(77)

print(soob.display_user_balance())


roussom.transfere_money(soob, 50)

print(roussom.display_user_balance())
print(soob.display_user_balance())