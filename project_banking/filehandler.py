import csv
import os
from customers import Customer


class FileHandler:

    def __init__(self):

        self.user_file = "users.csv"
        self.transaction_file = "transactions.csv"

        if not os.path.exists(self.user_file):

            file = open(self.user_file, "w", newline="")

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Name",
                    "Age",
                    "Username",
                    "Email",
                    "Password",
                    "Balance"
                ]
            )

            writer.writeheader()

            file.close()

        if not os.path.exists(self.transaction_file):

            file = open(self.transaction_file, "w", newline="")

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Username",
                    "Type",
                    "Amount",
                    "Balance"
                ]
            )

            writer.writeheader()

            file.close()

    # ---------- Load Users ----------

    def load_users(self):

        customers = []

        file = open(self.user_file, "r", newline="")

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

        file.close()

        return customers

    # ---------- Save Users ----------

    def save_users(self, customers):

        file = open(self.user_file, "w", newline="")

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Name",
                "Age",
                "Username",
                "Email",
                "Password",
                "Balance"
            ]
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

        file.close()

    # ---------- Save Transaction ----------

    def save_transaction(self, username, transaction_type, amount, balance):

        file = open(self.transaction_file, "a", newline="")

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Username",
                "Type",
                "Amount",
                "Balance"
            ]
        )

        writer.writerow({

            "Username": username,
            "Type": transaction_type,
            "Amount": amount,
            "Balance": balance

        })

        file.close()