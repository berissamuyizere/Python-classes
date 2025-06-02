import datetime
class Transaction:
    def __init__(self, amount, narration, transaction_type):
        self.amount = amount
        self.narration = narration
        self.transaction_type = transaction_type
        self.date_time = datetime.datetime.now()
    def __str__(self):
        return f"{self.date_time} - {self.transaction_type.upper()}: {self.narration} | Amount: {self.amount}"

class Account:
    def __init__(self, name, account_number):
        self.name = name
        self.__balance = 0
        self.__account_number = account_number
        self.__transactions = []
        self.loan = 0
        self.loan_status = "inactive"
        self.is_frozen = False
        self.minimum_balance = 100  
        self.closed = False
        self.deposit_count = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(Transaction(amount, "Deposit", "deposit"))
            self.deposit_count += 1
            return f"Confirmed, you have deposited {amount}. New balance is {self.__balance}"
        return "Deposit amount must be greater than 0"

 