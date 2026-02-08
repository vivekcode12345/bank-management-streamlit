import json
import random
import string
from pathlib import Path

class Bank:
    database = "data.json"

    def __init__(self):
        if Path(self.database).exists():
            with open(self.database, "r") as f:
                self.data = json.load(f)
        else:
            self.data = []

    def __update(self):
        with open(self.database, "w") as f:
            json.dump(self.data, f, indent=4)

    def __generate_account(self):
        chars = (
            random.choices(string.ascii_letters, k=3)
            + random.choices(string.digits, k=3)
            + random.choices("!@#$%^&*", k=1)
        )
        random.shuffle(chars)
        return "".join(chars)

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Age must be 18+ and PIN must be 4 digits"

        acc_no = self.__generate_account()
        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": acc_no,
            "balance": 0
        }

        self.data.append(user)
        self.__update()
        return True, acc_no

    def get_user(self, acc_no, pin):
        for user in self.data:
            if user["accountNo"] == acc_no and user["pin"] == pin:
                return user
        return None

    def deposit(self, acc_no, pin, amount):
        user = self.get_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"

        if amount <= 0 or amount > 10000:
            return False, "Invalid amount"

        user["balance"] += amount
        self.__update()
        return True, "Money deposited"

    def withdraw(self, acc_no, pin, amount):
        user = self.get_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"

        if amount <= 0 or amount > user["balance"]:
            return False, "Insufficient balance"

        user["balance"] -= amount
        self.__update()
        return True, "Money withdrawn"

    def delete_account(self, acc_no, pin):
        user = self.get_user(acc_no, pin)
        if not user:
            return False, "Invalid credentials"

        self.data.remove(user)
        self.__update()
        return True, "Account deleted"
