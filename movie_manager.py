import requests

# a class to create Movie object
class Movie:
    def __init__(self, id_, title, runtime, rating, year, description):
        # handling movie rating to be float
        try:
            float(rating)
        except ValueError:
            print("Invalid format for movie rating")
        self.id_ = id_
        self.title = title
        self.runtime = runtime
        self.rating = rating
        self.year = year
        self.description = description
        self.total_reserves = 0
        self.feedbacks = {}

    def __str__(self):
        return f"""\n{"-"*136}\nTitle: {self.title}
RunTime: {self.runtime}, Rating: {self.rating}, Year: {self.year}
\nDescription: {self.description}
\nTotal reserves: {self.total_reserves}
Feedbacks: {self.feedbacks}
{"-"*136}"""

# a class to fetch movies from API
class MovieFetch:
    API_KEY = "3acfbd8a"
    BASE_URL = "http://www.omdbapi.com/"

    @staticmethod
    def movie_fetch(title):
        params = {"apikey": MovieFetch.API_KEY, "t": title} # params for this API
        response = requests.get(MovieFetch.BASE_URL, params=params) # requesting to API
        data = response.json() 

        # checking if our response is okay
        if data['Response'] == "True":
            movie = Movie(data['imdbID'], data['Title'], data['Runtime'], data['imdbRating'], data['Year'],
                        data['Plot'])
            return movie
        else:
            print("\nNothing found!")
            return None
        

