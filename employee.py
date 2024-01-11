from person import *
from movie_manager import *

class Employee(Person):
    unq_id = 1001

    def __init__(self, name, email, phone, employee_id, position):
        id_ = Employee.create_id()
        super().__init__(name, email, phone, id_)
        self.employee_id = employee_id
        self.position = position

    # a classmethod to create uniqe ID for each employee
    @classmethod
    def create_id(cls):
        id_ = "E" + str(cls.unq_id)[1:]
        cls.unq_id += 1
        return id_

    def add_movie(self, movie, cinema_hall):
        # checking if movie is Movie instance
        if not isinstance(movie, Movie):
            raise TypeError("\nInvalid movie! Expected a movie but got none!\n")

        # checks if movie already exists in hall
        if movie.id_ not in cinema_hall.movies:
            cinema_hall.movies[movie.id_] = movie
            print(f"\n{movie.title} added to {cinema_hall.name} successfuly!\n")
        else:
            print(f"\n{movie.title} already exists in {cinema_hall.name} movies!\n")

    def remove_movie(self, movie, cinema_hall):
        # checking if movie is Movie instance
        if not isinstance(movie, Movie):
            raise TypeError("\nInvalid movie! Expected a movie but got none!\n")
            
        # checks if movie exists in hall
        if movie.id_ in cinema_hall.movies:
            del cinema_hall.movies[movie.id_]
            print(f"\n{movie.title} removed from {cinema_hall.name} successfuly!\n")
        else:
            print("\nMovie does not exist\n")
    
    # gives options to employees by their position
    def check_role(self):
        if self.position == "movie manager":
            print("""Choose between 1-n:
    1- Add a movie to Hall
    2- Remove a move from Hall
    3- Display movies
    4- logout""")
            
        elif self.position == "user manager":
            print("""Choose between 1-n:
    1- Add a user email to Hall
    2- Remove a user email from Hall
    3- Display users
    4- Logout""")
            
        elif self.position == "reserve manager":
            print("""Choose between 1-n:
    1- Create a reservation for a member
    2- Cancel a reservation for a member
    3- Display all reservations
    4- Logout""")