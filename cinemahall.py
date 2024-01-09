from account_manager import *

class CinemaHall:
    account_manager = AccountManager()

    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.all_reservations = {}
        self.members = {
            "user": {},
            "employee": {}
        }
        self.movies = {}

    def show_movies(self):
        for movie in self.movies.values():
            print(movie)

    def add_person(self, person):
        if person.email in self.members['user'].values() or person.email in self.members['employee'].values():
            print(f"Error: Email {person.email} is already registered.")
            return False

        person_type = type(person).__name__.lower()
        can_regester, msg = CinemaHall.account_manager.register(person.email)

        if can_regester:
            if person_type == "user":
                self.members['user'][person.id_] = person.email
                print(msg)
                return True
            elif person_type == "employee":
                self.members['employee'][person.id_] = person.email
                print(msg)
                return True 
        else:
            print(msg)
            return False

    def log_person(self, person):
        if person.email in self.members['user'].values() or person.email in self.members['employee'].values():
            registered, msg = CinemaHall.account_manager.register(person.email)
            if registered:
                return True
            else:
                print(msg)
                return False
        raise ValueError("Invalid email! You should register first!")
        


    
    def logout_person(self, person):
        if person.email in self.members['user'].values() or person.email in self.members['employee'].values():
            logout, msg = CinemaHall.account_manager.logout(person.email)

            if logout:
                print(msg)
                return False
            else:
                print(msg)
                return True
        print("You are not registered!")
        return True


    def __str__(self):
        return f"{self.movies}, {self.members}"