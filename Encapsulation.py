#
# Python Ver:   3.12.6
#
# Author:       Prince M. Macaldo
#
# Purpose:      Encapsulation Submission Assignment from the Tech Academy 
#  


class BankAccount:  
    def __init__(self, owner, balance=0.0):  
        self.owner = owner  
        # Private attribute: account balance  
        self.__balance = balance  

    def deposit(self, amount):  
        """Deposit money into the account."""  
        if amount > 0:  
            self.__balance += amount  # Modify private balance directly  
            print(f"Deposited: {amount}. New balance: {self.__balance}")  
    
    def withdraw(self, amount):  
        """Withdraw money from the account."""  
        if 0 < amount <= self.__balance:  
            self.__balance -= amount  # Modify private balance directly  
            print(f"Withdrew: {amount}. New balance: {self.__balance}")  

    def check_balance(self):  
        """Public method to check the balance."""  
        return self.__balance  # Return private balance  


# Create an object of BankAccount  
account = BankAccount("John Doe", 1000.0)  

# Use public methods to interact with the account  
account.deposit(500)  
account.withdraw(200)  

# Check the balance  
print(f"Current balance: {account.check_balance()}")  

