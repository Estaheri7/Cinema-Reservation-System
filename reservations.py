class Reservation:
    resv_id = 1

    def __init__(self, movie_id, showtime, seat_number, email):
        self.id_ = Reservation.resv_id
        self.movie_id = movie_id
        self.showtime = showtime
        self.seat_number = seat_number
        self.email = email
        self.all_reservations = {}
        Reservation.resv_id += 1

    def __str__(self):
        return f"{self.movie_id}, {self.showtime}, {self.seat_number}, {self.email}"