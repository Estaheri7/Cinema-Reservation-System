from person import *
from reservations import *
from feedback import *

class User(Person):
    def __init__(self, name, email, phone, user_id):
        pass

    @classmethod
    def create_id(cls):
        pass

    def reserve(self, movie, cinema_hall):
        pass

    def cancel_reserve(self, movie_id):
        pass
        

    def feedback(self, movie):
        pass

    def __str__(self):
        pass

    def check_role(self):
        pass