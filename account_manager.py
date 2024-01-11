import re

class AccountManager:
    def __init__(self):
        self.log_accounts = [] # a list to save logged in accounts

    # registers and logs persons in
    def register(self, email):
        # checking if email is not logged in and has valid format
        if self.is_valid(email) and email not in self.log_accounts:
            self.log_accounts.append(email)
            return True, "\nDone!\n"
        return False, "\nInvalid email format\n"

    # log out if person is logged in
    def logout(self, email):
        # checks if email is logged in or not
        if email in self.log_accounts:
            self.log_accounts.remove(email)
            return True, "\nSuccessfully logged out!\n"
        else:
            return False, "\nYou are not logged in!\n"

    # a staticmethod which checks format of email using regex
    @staticmethod
    def is_valid(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

