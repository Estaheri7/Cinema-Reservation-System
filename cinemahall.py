from account_manager import *
from error_log import *

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

    def show_users(self):
        for m, val in self.members.items():
            print(f"{m[0].upper()}{m[1:]}s:")
            for email in val.values():
                print("<< " + email + " >>")

    def show_reserves(self):
        for e, r in self.all_reservations.items():
            print(f"{e} has reserved {r}")

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
        raise EmailNotRegistered("email does not exist! You should register first!")
        
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

    def remove_user(self, person):
        for v in self.members.values():
            for id_, e in v.items():
                if person.email == e:
                    self.logout_person(person)
                    del v[id_]
                    return
        print("User not found!")

    def __str__(self):
        return f"{self.movies}, {self.members}"
    