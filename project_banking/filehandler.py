import csv
import os
from customers import Customer


class FileHandler:

    def __init__(self):

        # ---------- Go to Desktop ----------

        os.chdir("C:\\Users\\user\\Desktop")

        # ---------- Create Folder ----------

        if not os.path.exists("Banking_Project"):

            os.mkdir("Banking_Project")

        # ---------- Change Directory ----------

        os.chdir("Banking_Project")

        # ---------- Create users.csv ----------

        if not os.path.exists("users.csv"):

            with open("users.csv", "w", newline="") as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=["Name","Age","Username","Email","Password","Balance"]
                )

                writer.writeheader()

        # ---------- Create transactions.csv ----------

        if not os.path.exists("transactions.csv"):

            with open("transactions.csv", "w", newline="") as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=["Username","Type","Amount","Balance"]
                )

                writer.writeheader()

    # ---------- Load Users ----------

    def load_users(self):

        customers = []

        with open("users.csv", "r", newline="") as file:

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

        with open("users.csv", "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["Name","Age","Username","Email","Password","Balance"]
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

    # ---------- Save Transactions ----------

    def save_transaction(self, username, transaction_type, amount, balance):

        with open("transactions.csv", "a", newline="") as file:

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