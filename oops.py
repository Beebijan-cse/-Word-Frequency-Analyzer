
from abc import ABC, abstractmethod


# Abstract Parent Class
class BankAccount(ABC):

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = balance

    # Encapsulation
    def get_balance(self):
        return self.__balance

    # Deposit Money
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount!")
        else:
            self.__balance += amount
            print("Deposit successful!")

    # Withdraw Money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")

        elif amount > self.__balance:
            print("Insufficient balance!")

        else:
            self.__balance -= amount
            print("Withdrawal successful!")

    # Abstraction
    @abstractmethod
    def calculate_interest(self):
        pass

    # Display Account Details
    def display_details(self):
        print("\nAccount Holder:", self.name)
        print("Account Number:", self.account_number)
        print(f"Balance: Rs. {self.__balance:.2f}")


# Inheritance
class SavingsAccount(BankAccount):

    def calculate_interest(self):
        return self.get_balance() * 0.05

    # Method Overriding
    def display_details(self):
        print("\n--- Savings Account ---")
        super().display_details()
        print(f"Interest: Rs. {self.calculate_interest():.2f}")


class CurrentAccount(BankAccount):

    def calculate_interest(self):
        return 0

    # Method Overriding
    def display_details(self):
        print("\n--- Current Account ---")
        super().display_details()
        print(f"Interest: Rs. {self.calculate_interest():.2f}")


# Bank Management Class
class Bank:

    def __init__(self):
        self.accounts = []

    # Create Account
    def create_account(self):

        name = input("Enter account holder name: ").strip()

        if not name:
            print("Name cannot be empty!")
            return

        account_number = input("Enter account number: ").strip()

        if not account_number:
            print("Account number cannot be empty!")
            return

        # Check Duplicate Account
        for account in self.accounts:
            if account.account_number == account_number:
                print("Account number already exists!")
                return

        try:
            balance = float(input("Enter initial balance: "))

            if balance < 0:
                print("Balance cannot be negative!")
                return

        except ValueError:
            print("Please enter a valid balance!")
            return

        print("\n1. Savings Account")
        print("2. Current Account")

        choice = input("Choose account type: ").strip()

        if choice == "1":
            account = SavingsAccount(
                name, account_number, balance
            )

        elif choice == "2":
            account = CurrentAccount(
                name, account_number, balance
            )

        else:
            print("Invalid account type!")
            return

        self.accounts.append(account)

        print("\nAccount created successfully!")

    # Find Account
    def find_account(self):

        account_number = input("Enter account number: ").strip()

        for account in self.accounts:
            if account.account_number == account_number:
                return account

        print("Account not found!")
        return None

    # Deposit Money
    def deposit_money(self):

        account = self.find_account()

        if account:
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

            except ValueError:
                print("Please enter a valid amount!")

    # Withdraw Money
    def withdraw_money(self):

        account = self.find_account()

        if account:
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

            except ValueError:
                print("Please enter a valid amount!")

    # Display One Account
    def display_account(self):

        account = self.find_account()

        if account:
            account.display_details()

    # Display All Accounts
    def display_all_accounts(self):

        if not self.accounts:
            print("No accounts available!")
            return

        for account in self.accounts:
            account.display_details()


# Main Program
def main():

    bank = Bank()

    while True:

        print("\n================================")
        print("       BANK MANAGEMENT SYSTEM")
        print("================================")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account")
        print("5. Display All Accounts")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            bank.deposit_money()

        elif choice == "3":
            bank.withdraw_money()

        elif choice == "4":
            bank.display_account()

        elif choice == "5":
            bank.display_all_accounts()

        elif choice == "6":
            print("Thank you for using Bank Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
