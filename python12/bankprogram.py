# BLUEPRINT (Class)
class BankAccount:
    """A class representing a bank account"""

    # Constructor - runs when object is created
    def __init__(self, owner_name, initial_balance):
        """Initialize account with owner and balance"""
        self.owner = owner_name  # Attribute
        self.balance = initial_balance  # Attribute
        self.transaction_count = 0  # Attribute

    # METHOD to deposit money
    def deposit(self, amount):
        """Add money to account"""
        if amount > 0:
            self.balance += amount
            self.transaction_count += 1
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount!")

    # METHOD to withdraw money
    def withdraw(self, amount):
        """Remove money from account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_count += 1
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount or insufficient funds!")

    # METHOD to check balance
    def check_balance(self):
        """Display current balance"""
        print(f"{self.owner}'s balance: ${self.balance}")
        return self.balance

    # METHOD to get account info
    def get_info(self):
        """Display all account information"""
        print(f"Account Owner: {self.owner}")
        print(f"Balance: ${self.balance}")
        print(f"Transactions: {self.transaction_count}")


# Now let's USE this class!

# Creating OBJECTS (actual bank accounts)
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print("=== Alice's Account ===")
account1.check_balance()  # Alice's balance: $1000
account1.deposit(500)  # Deposited $500. New balance: $1500
account1.withdraw(200)  # Withdrew $200. New balance: $1300
account1.get_info()
# Output:
# Account Owner: Alice
# Balance: $1300
# Transactions: 2

print("\n=== Bob's Account ===")
account2.check_balance()  # Bob's balance: $500
account2.deposit(100)  # Deposited $100. New balance: $600
account2.withdraw(50)  # Withdrew $50. New balance: $550
account2.get_info()
# Output:
# Account Owner: Bob
# Balance: $550
# Transactions: 2

# Notice: Each account is INDEPENDENT!
# Alice's transactions don't affect Bob's account