class Account:
    def __init__(self, name):
        self.name= name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []

    def deposit(self, amount):
        if amount > 0:
            self.deposits.append(amount)
            balance = self.balance + sum(self.deposits)
            return f"Confirmed, you have received {amount} new balance is {balance} " 


    def withdraw(self, amount):
        self.withdrawals.append(amount)
        # total_deposits = sum(self.deposits)
        if amount <= self.balance:
            new_balance = sum(self.deposits) - sum(self.withdrawals)
            return f"You have withdrawn {amount} amount new balance is {new_balance}"
            
    def get_balance(self):
        balance = sum(self.deposits) - sum(self.withdrawals)
        return  balance