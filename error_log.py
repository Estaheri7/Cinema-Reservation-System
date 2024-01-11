# An error for emails which try to log in without registering
class EmailNotRegistered(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

# An error for emails which are registered already and trying to register again
class EmailRegisteredAlready(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg