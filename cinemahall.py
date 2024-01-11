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
        if not self.movies:
            print("\nEmpty\n")
            return
        for movie in self.movies.values():
            print(movie)

    def show_users(self):
        for m, val in self.members.items():
            print(f"\n{m[0].upper()}{m[1:]}s:")
            for email in val.values():
                print("<< " + email + " >>")

    def show_reserves(self):
        if not self.all_reservations:
            print("\nEmpty\n")
            return
        for e, r in self.all_reservations.items():
            print(f"{e} has reserved {r}")

    def add_person(self, person):
        if person.email in self.members['user'].values() or person.email in self.members['employee'].values():
            raise EmailRegisteredAlready(f"\nError: Email {person.email} is already registered.\n")
    
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
        raise EmailNotRegistered("\nEmail does not exist! You should register first!\n")
        
    def logout_person(self, person):
        if person.email in self.members['user'].values() or person.email in self.members['employee'].values():
            logout, msg = CinemaHall.account_manager.logout(person.email)

            if logout:
                print(msg)
                return False
            else:
                print(msg)
                return True
        print("\nYou are not registered!\n")
        return True

    def remove_user(self, person):
        for v in self.members.values():
            for id_, e in v.items():
                if person.email == e:
                    self.logout_person(person)
                    del v[id_]
                    return f"\nUser {person.email} removed from {self.name} successfuly!\n"
        return "\nUser not found!\n"

    def __str__(self):
        return f"{self.movies}, {self.members}"
    