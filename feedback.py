class Feedback:
    def __init__(self, user_id, movie_id, rating, comment):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"{self.comment}"