import re

class AccountManager:
    def __init__(self):
        self.log_accounts = []

    def register(self, email):
        if self.is_valid(email) and email not in self.log_accounts:
            self.log_accounts.append(email)
            return True, "Done!"
        return False, "Invalid email format"

    def logout(self, email):
        if email in self.log_accounts:
            self.log_accounts.remove(email)
            return True, "Successfully logged out!"
        else:
            return False, "You are not logged in!"

    @staticmethod
    def is_valid(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

