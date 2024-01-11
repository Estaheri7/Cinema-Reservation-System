from person import *
from reservations import *
from feedback import *

class User(Person):
    unq_id = 1001

    def __init__(self, name, email, phone, user_id):
        id_ = User.create_id()
        super().__init__(name, email, phone, id_)
        self.user_id = user_id
        self.reservation = {}

    @classmethod
    def create_id(cls):
        id_ = "U" + str(cls.unq_id)[1:]
        cls.unq_id += 1
        return id_

    def reserve(self, movie, cinema_hall):
        show_time = input("What is showtime? ")

        resv = Reservation(movie.id_, show_time, movie.total_reserves, self.email)
        if movie.id_ not in self.reservation.values() and movie.total_reserves < cinema_hall.total_seats and len(self.reservation) < 1:
            self.reservation[resv.movie_id] = resv
            cinema_hall.all_reservations[self.email] = movie.title

            for k, m in cinema_hall.movies.items():
                if k == movie.id_:
                    m.total_reserves += 1
                    return f"\nSuccessfuly reserved {movie.title} for {self.email} in {cinema_hall.name}\n"
        elif len(self.reservation) >= 1:
            return "\nYou can have only 1 reserve for a movie each day!\n"

        elif movie.total_reserves >= cinema_hall.total_seats:
            return f"\n{cinema_hall.name} is full!!!\n"

        else:
            return f"\n{movie.title} already reserved for {self.email}\n"

    def cancel_reserve(self, movie, cinema_hall):
        for e in cinema_hall.all_reservations:
            if e == self.email and cinema_hall.all_reservations[e] == movie.title:
                del cinema_hall.all_reservations[self.email]
                                                            
                for k, m in cinema_hall.movies.items():
                    if k == movie.id_:
                        m.total_reserves -= 1
                        return f"\nSuccessfuly canceled {movie.title} reservation for {self.email} in {cinema_hall.name}\n"
                    
        return "\nInvalid movie\n"
        

    def feedback(self, movie, cinema_hall):
        rating = 11
        while (0 > rating or rating > 10):
            try:
                rating = float(input("Please enter a number between 1-10: "))
            except ValueError:
                print("You have to enter a number between 1-10: ")

        comment = input("Leave a comment...\n")
        fb = Feedback(self.user_id, movie.id_, rating, comment)
        
        for k, m in cinema_hall.movies.items():
            if k == movie.id_:
                m.feedbacks[fb.comment] = rating

    def __str__(self):
        return f"{super().__str__()}ID: {self.user_id}\n"
    
    @staticmethod
    def check_role():
        print("""choose between 1-n:
1- Reserve for a movie
2- Cancel a reservation
3- Feedback
4- Display information
5- Logout""")