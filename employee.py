from person import *

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
        if movie.id_ not in cinema_hall.movies:
            cinema_hall.movies[movie.id_] = movie
        else:
            print(f"{movie.title} already exists in {cinema_hall.name} movies!")

    @staticmethod
    def check_role():
        print("""Choose between 1-n:
1- Add a movie to Hall
2- Display movies
3- Display reservations
4- logout""")