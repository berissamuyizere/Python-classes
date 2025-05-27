class Account:
    def __init__(self, name, account_number):
        self.name= name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.account_number = account_number
        self.loan = 0
        self.loan_status = "inactive"
        self.is_frozen = False
        self.minimum_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.deposits.append(amount)
            self.balance = self.get_balance()
            return f"Confirmed, you have received {amount} new balance is {self.balance} " 


    def withdraw(self, amount):
        # total_deposits = sum(self.deposits)
        if amount <= sum(self.deposits):
            self.withdrawals.append(amount)
            new_balance = sum(self.deposits) - sum(self.withdrawals)
            return f"You have withdrawn {amount} amount new balance is {new_balance}"
        else:
            return "Insuficient balance"  
 
        
    def get_balance(self):
        balance = sum(self.deposits) - sum(self.withdrawals)
        return  balance

    def transfer_funds(self, recipient, amount):
        #   if sender.account_number == recipient.account_number:
        #     print("Cannot transfer funds to the same account")
        if  amount <= self.get_balance():
            self.withdraw(amount)
            recipient.deposit(amount)
            return f"you have transfered  {amount} to {recipient.name}"
      
    def request_loan(self, amount):
        if self.loan_status == "inactive":
            self.loan = amount
            # self.loan_status = "pending" 
            self.deposit(amount)  
            print("Loan request is being processed")
        elif self.loan_status == "pending":
            print("Another loan request is still in process")
        else:
            print("You still have an active loan")       

    def repay_loan(self, amount):
        if amount <= 0:
            print("Invalid repayment amount.")
            return

        if amount <= self.balance:
            self.balance -= amount
            self.loan -= amount
            print(f"Successfully repaid ${amount}. Remaining loan balance: ${self.loan}")
        else:
            print("Insufficient funds to repay the specified amount.")

    def change_account_ownership(self, new_owner):
        self.name = new_owner
        return f"Account ownership shifted  to {new_owner}"

    def interest_rate(self):
        interest = self.balance * 0.05
        new_balance = self.balance + interest
        return f"interest rate is {interest} and your new balance is {new_balance}"

    def freez_account(self):
        if not self.is_frozen:
            self.is_frozen = True
            return "account have been frozen"
        else:
            return "account already frozen"

    def unfreez_account(self):
        if self.is_frozen:
            self.is_frozen = False
            print(f"account {self.account_number} has been frozen")
        else:
            print(f"account {self.account_number} is not frozen") 

    def account_statement(self):
        print("Account Statement:")
        for i, deposit in enumerate(self.deposits):
            print(f"Deposit {i+1}: {deposit}")
        for i, withdrawal in enumerate(self.withdrawals):
            print(f"Withdrawal {i+1}: {withdrawal}")

    def set_minmum_balance(self, amount):
        if amount >=0:
            self.minimum_balance = amount
        else:
            return "balance cannot be negative"    
            

     def clear_account(self):
        



        