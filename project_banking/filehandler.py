import csv
import os
from customers import Customer


class FileHandler:

    def __init__(self):

        self.folder = "C:\\Users\\user\\Desktop\\Banking_Project"

        if not os.path.exists(self.folder):

            os.makedirs(self.folder)

        self.user_file = self.folder + "\\users.csv"

        self.transaction_file = self.folder + "\\transactions.csv"

        if not os.path.exists(self.user_file):

            with open(self.user_file, "w", newline="") as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=["Name","Age","Username","Email","Password","Balance"]
                )

                writer.writeheader()

        if not os.path.exists(self.transaction_file):

            with open(self.transaction_file, "w", newline="") as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=["Username","Type","Amount","Balance"]
                )

                writer.writeheader()

    # ---------- Load Users ----------

    def load_users(self):

        customers = []

        with open(self.user_file, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                user = Customer(

                    row["Name"],
                    int(row["Age"]),
                    row["Username"],
                    row["Email"],
                    row["Password"],
                    int(row["Balance"])

                )

                customers.append(user)

        return customers

    # ---------- Save Users ----------

    def save_users(self, customers):

        with open(self.user_file, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["Name", "Age","Username","Email","Password","Balance"]
            )

            writer.writeheader()

            for user in customers:

                writer.writerow({

                    "Name": user.get_name(),
                    "Age": user.get_age(),
                    "Username": user.get_username(),
                    "Email": user.get_email(),
                    "Password": user.get_password(),
                    "Balance": user.get_balance()

                })

    # ---------- Save Transaction ----------

    def save_transaction(self, username, transaction_type, amount, balance):

        with open(self.transaction_file, "a", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["Username","Type","Amount","Balance"]
            )

            writer.writerow({

                "Username": username,
                "Type": transaction_type,
                "Amount": amount,
                "Balance": balance

            })