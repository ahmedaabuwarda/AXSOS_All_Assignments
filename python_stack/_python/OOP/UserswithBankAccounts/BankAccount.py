class BankAccount:
    def __init__(self, name="", balance=0, interest_rate=0.01):
        self.name = name
        self.balance = balance
        self.interest_rate = interest_rate

    def get_balance(self):
        return self.balance
    
    def get_name(self):
        return self.name
    
    def get_interest_rate(self):
        return self.interest_rate
    
    def set_name(self, name):
        self.name = name
        return self
    
    def set_balance(self, balance):
        self.balance = balance
        return self
    
    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate
        return self

    def deposit(self, amount):
        # self.balance = self.balance + amount
        self.set_balance(self.get_balance() + amount)
        return self
    
    def withdraw(self, amount):
        if (self.get_balance() >= amount):
            self.set_balance(self.get_balance() - amount)
            return self
        else:
            print("Insufficient funds: Charging 5$ fee")
            self.set_balance(self.get_balance() - 5)
            return self
        
    def display_account_info(self):
        print(f"Balance: {self.get_balance()}$")
        # return self
    
    def yield_interest(self):
        if (self.get_balance() > 0):
            interest = self.get_balance() * self.get_interest_rate()
            self.set_balance(self.get_balance() + interest)
            return self
        else:
            print("Negative balance!")


ahmed_account = BankAccount("Ahmed", 20, 0.02)

ahmed_account.deposit(20).deposit(10).deposit(30).withdraw(30).yield_interest().display_account_info()

miqdad_account = BankAccount("Miqdad", 200, 0.03)

miqdad_account.deposit(60).deposit(10).withdraw(5).withdraw(10).withdraw(5).withdraw(10).yield_interest().display_account_info()