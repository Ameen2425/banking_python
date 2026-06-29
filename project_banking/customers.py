class Customer:

    def __init__(self, name, age, username, email, password, balance):

        self.__name = name
        self.__age = age
        self.__username = username
        self.__email = email
        self.__password = password
        self.__balance = balance

    # -------- Name --------

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # -------- Age --------

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # -------- Username --------

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    # -------- Email --------

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    # -------- Password --------

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    # -------- Balance --------

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance