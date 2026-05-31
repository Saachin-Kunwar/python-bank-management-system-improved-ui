
from datetime import datetime


class Account:

    def __init__(self, name, pin, balance=0):

        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []
        self.is_active = True

    # ---------------- DEPOSIT ----------------

    def deposit(self, amount):

        self.balance += amount

        time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.history.append(
            f"Deposited Rs.{amount} at {time}"
        )

        return "Deposit successful"

    # ---------------- WITHDRAW ----------------

    def withdraw(self, amount):

        if amount > self.balance:
            return "Insufficient balance"

        self.balance -= amount

        time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.history.append(
            f"Withdrawn Rs.{amount} at {time}"
        )

        return "Withdraw successful"

    # ---------------- RECEIVE ----------------

    def add_money(self, amount, sender_name):

        self.balance += amount

        time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.history.append(
            f"Received Rs.{amount} from {sender_name} at {time}"
        )

    # ---------------- SEND ----------------

    def send_money(self, amount, receiver_name):

        self.balance -= amount

        time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.history.append(
            f"Sent Rs.{amount} to {receiver_name} at {time}"
        )

    # ---------------- BALANCE ----------------

    def get_balance(self):
        return self.balance

    # ---------------- HISTORY ----------------

    def get_history(self):
        return self.history

