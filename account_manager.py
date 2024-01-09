class AccountManager:
    def __init__(self):
        self.log_accounts = []

    def register(self, email):
        if email not in self.log_accounts:
            self.log_accounts.append(email)
            return True, "Done!"
        return False, "Nope!"

    def logout(self, email):
        if email in self.log_accounts:
            self.log_accounts.remove(email)
            return True, "Successfuly logged out!"
        else:
            return False, "You are not logged in!"
        