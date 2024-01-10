class Reservation:
    resv_id = 1

    def __init__(self, movie_id, showtime, seat_number, email):

        if not isinstance(movie_id, str) or not movie_id:
            raise ValueError("Invalid movie_id! Please provide a non-empty string.")
        
        if not isinstance(showtime, str) or not showtime:
            raise ValueError("Invalid showtime! Please provide a non-empty string.")
        
        if not isinstance(seat_number, int) or seat_number < 0:
            raise ValueError("Invalid seat_number! Please provide a positive integer.")
        
        if not isinstance(email, str) or not email:
            raise ValueError("Invalid email! Please provide a non-empty string.")
        
        self.id_ = Reservation.resv_id
        self.movie_id = movie_id
        self.showtime = showtime
        self.seat_number = seat_number
        self.email = email
        self.all_reservations = {}
        Reservation.resv_id += 1

    def __str__(self):
        return f"{self.movie_id}, {self.showtime}, {self.seat_number}, {self.email}"