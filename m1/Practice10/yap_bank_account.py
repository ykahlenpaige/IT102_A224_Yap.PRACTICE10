from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(
        self,
        account_number,
        name,
        pin,
        starting_balance
    ):
        self.account_number = account_number
        self.account_name = name

        self._pin = pin
        self._balance = starting_balance

    def check_balance(self):
        return self._balance

    def deposit(self, amount):

        if amount <= 0:
            return False

        self._balance += amount

        return True

    def withdraw(self, amount):

        if amount <= 0:
            return False

        if amount > self._balance:
            return False

        self._balance -= amount

        return True

    def verify_pin(self, pin):

        return self._pin == pin

    def get_pin(self):

        return self._pin

    @abstractmethod
    def get_account_type(self):
        pass


class SavingsAccount(BankAccount):

    def get_account_type(self):

        return "Savings Account"

class StudentAccount(BankAccount):

    def get_account_type(self):

        return "Student Account"