
import json
import os

from account import Account


class Bank:

    def __init__(self):

        self.accounts = {}

        self.base_dir = os.path.dirname(
            os.path.dirname(__file__)
        )

        self.data_file = os.path.join(
            self.base_dir,
            "data",
            "bank_data.json"
        )

        self.load_data()

    # ---------------- CREATE ACCOUNT ----------------

    def create_account(self, name, pin):

        if name in self.accounts:
            return False, "Account already exists"

        self.accounts[name] = Account(name, pin)

        self.save_data()

        return True, "Account created successfully"

    # ---------------- LOGIN ----------------

    def login(self, name, pin):

        acc = self.accounts.get(name)

        if not acc:
            return False, "Account not found"

        if acc.pin != pin:
            return False, "Invalid PIN"

        if not acc.is_active:
            return False, "Account is deactivated"

        return True, acc

    # ---------------- TRANSFER ----------------

    def transfer_money(
        self,
        sender,
        receiver_name,
        amount
    ):

        receiver = self.accounts.get(receiver_name)

        if not receiver:
            return False, "Receiver not found"

        if amount > sender.balance:
            return False, "Insufficient balance"

        sender.send_money(amount, receiver_name)

        receiver.add_money(amount, sender.name)

        self.save_data()

        return True, "Transfer successful"

    # ---------------- DEACTIVATE ----------------

    def deactivate_account(self, acc):

        acc.is_active = False

        self.save_data()

        return "Account deactivated"

    # ---------------- DELETE ----------------

    def delete_account(self, acc):

        del self.accounts[acc.name]

        self.save_data()

        return "Account deleted"

    # ---------------- REACTIVATE ----------------

    def reactivate_account(self, name, pin):

        acc = self.accounts.get(name)

        if not acc:
            return False, "Account not found"

        if acc.pin != pin:
            return False, "Invalid PIN"

        acc.is_active = True

        self.save_data()

        return True, "Account reactivated"

    # ---------------- SAVE DATA ----------------

    def save_data(self):

        data = {}

        for name, acc in self.accounts.items():

            data[name] = {
                "pin": acc.pin,
                "balance": acc.balance,
                "history": acc.history,
                "is_active": acc.is_active
            }

        os.makedirs(
            os.path.dirname(self.data_file),
            exist_ok=True
        )

        with open(self.data_file, "w") as f:

            json.dump(data, f, indent=4)

    # ---------------- LOAD DATA ----------------

    def load_data(self):

        try:

            with open(self.data_file, "r") as f:

                data = json.load(f)

                for name, info in data.items():

                    acc = Account(
                        name,
                        info["pin"],
                        info["balance"]
                    )

                    acc.history = info["history"]

                    acc.is_active = info.get(
                        "is_active",
                        True
                    )

                    self.accounts[name] = acc

        except FileNotFoundError:
            pass

