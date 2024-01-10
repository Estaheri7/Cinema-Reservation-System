from person import *
from movie_manager import *

class Employee(Person):
    unq_id = 1001

    def __init__(self, name, email, phone, employee_id, position):
        id_ = Employee.create_id()
        super().__init__(name, email, phone, id_)
        self.employee_id = employee_id
        self.position = position

    @classmethod
    def create_id(cls):
        id_ = "E" + str(cls.unq_id)[1:]
        cls.unq_id += 1
        return id_

    def add_movie(self, movie, cinema_hall):

        if not isinstance(movie, Movie):
            raise TypeError("Invalid movie! Expected a movie but got none!\n")

        if movie.id_ not in cinema_hall.movies:
            cinema_hall.movies[movie.id_] = movie
        else:
            print(f"{movie.title} already exists in {cinema_hall.name} movies!")

    def remove_movie(self, movie, cinema_hall):
        if not isinstance(movie, Movie):
            raise TypeError("Invalid movie! Expected a movie but got none!\n")
            
        if movie.id_ in cinema_hall.movies:
            del cinema_hall.movies[movie.id_]
        else:
            print("Movie does not exist")
    
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