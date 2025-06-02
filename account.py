import datetime
class Transaction:
    def __init__(self, amount, narration, transaction_type):
        self.amount = amount
        self.narration = narration
        self.transaction_type = transaction_type
        self.date_time = datetime.datetime.now()
    def __str__(self):
        return f"{self.date_time} - {self.transaction_type.upper()}: {self.narration} | Amount: {self.amount}"

