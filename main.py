from user import *
from employee import *
from cinemahall import *
from movie_manager import *

# a function to call in start loop
def help():
    print("""Welcome to the Cinema:
What is your role in hall?
1 - Employee
2 - Member
press Q to Exit.""")

# a function to get common details a person can have
def get_details():
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    # handling phone to be an integer number
    while True:
        try:
            phone = int(input("Enter your phone number: "))
            break
        except ValueError:
            print("Invalid PhoneNumber! Please enter a numeric value for the phone number.")

    return name, email, phone

# a function that can register or log person in
def RorL(method, cinema_hall, person):
    if method == "register":
        # handling error if email registered already
        try:
            is_login = cinema_hall.add_person(person)
        except EmailRegisteredAlready as e:
            print(e)
            return False
    elif method == "log in":
        # handling error if email is not registered and trying to log in
        try:
            is_login = cinema_hall.log_person(person)
        except EmailNotRegistered as e:
            print(e)
            return False
    else:
        print("\nInvalid method!\n")
        return False
        
    return is_login

# a function to handle picks for every type of user
def handle_pick():
    while True:
        try:
            pick = int(input(">>> "))
            return pick
        except ValueError: # handling if user entered non-integer number
            print("Please enter a number between 1-n!")

# MAIN
def main():
    # creating a cinemahall to work with it
    hall = CinemaHall("H1", 20)
    movie_fetcher = MovieFetch() # a movie fetcher which can fetch movies from API

    while True:
        help()
        is_login = False # declare a flag for users
        choice = input().upper()

        if choice == 'Q':
            break

        method = input("do you want to register or log in? ")
        # for employees
        if choice == '1':
            name, email, phone = get_details()
            emp_id = input("Enter your employee ID: ")
            position = input("Enter your position (Movie manager, User manager, Reserve manager): ").lower()
            # create an employee
            emp = Employee(name, email, phone, emp_id, position)
            # set is_login
            is_login = RorL(method, hall, emp)
            # while is_login is True
            while is_login:
                if emp.position == "movie manager":
                    emp.check_role()
                    pick = handle_pick()

                    if pick == 1:
                        title = input("Enter title of the movie: ")
                        movie = movie_fetcher.movie_fetch(title) # create movie object
                        # handling if movie not found
                        try:
                            emp.add_movie(movie, hall)
                        except TypeError as e:
                            print(e)

                    elif pick == 2:
                        title = input("Enter title of the movie: ")
                        movie = movie_fetcher.movie_fetch(title) # create a movie object
                        # handling if movie not found
                        try:
                            emp.remove_movie(movie, hall)
                        except TypeError as e:
                            print(e)

                    elif pick == 3:
                        hall.show_movies()

                    elif pick == 4:
                        is_login = hall.logout_person(emp)

                    else:
                        print("\nInvalid option!\n")

                elif emp.position == "user manager":
                    emp.check_role()
                    pick = handle_pick()

                    if pick == 4:
                        is_login = hall.logout_person(emp)

                    elif pick == 1:
                        email = input("Enter user email: ")
                        # create user
                        user = User(name = None, email = email, phone = None, user_id = None)
                        # handling if email already exists
                        try:
                            hall.add_person(user)
                        except EmailRegisteredAlready as e:
                            print(e)

                    elif pick == 2:
                        email = input("Enter user email: ")
                        # create user
                        user = User(name = None, email = email, phone = None, user_id = None)
                        # remove user and print its msg
                        msg = hall.remove_user(user)
                        print(msg)

                    elif pick == 3:
                        hall.show_users()

                    else:
                        print("\nInvalid option!\n")

                elif emp.position == "reserve manager":
                    emp.check_role()
                    pick = handle_pick()
                    if pick == 4:
                        is_login = hall.logout_person(emp)
                        break

                    elif pick == 3:
                        hall.show_reserves()
                        continue

                    email = input("Enter user email: ")
                    user = User(name = None, email = email, phone = None, user_id = None)

                    if email in hall.members['user'].values():
                        title = input("Enter title of the movie to reserve or cancel for user: ")
                        movie = movie_fetcher.movie_fetch(title) # create movie object 

                        flag = True # a flag to check if movie exists in hall
                        for m in hall.movies:
                            if movie.id_ == m:
                                flag = False
                        if flag:
                            print(f"{title} does not exist in {hall.name}")
                            continue

                        if pick == 1:
                            msg = user.reserve(movie, hall)
                            print(msg)

                        elif pick == 2:
                            msg = user.cancel_reserve(movie, hall)
                            print(msg)

                        else:
                            print("\nInvalid option!\n")
                            
                    else:
                        print(f"\n{email} does not exist in {hall.name}\n")

                else:
                    hall.logout_person(emp)
                    print("Invalid position for employee!")
                    break
        # for users
        elif choice == '2':
            name, email, phone = get_details()
            user_id = input("Enter your user ID: ")
            # create user
            user = User(name, email, phone, user_id)
            # set is_login value
            is_login = RorL(method, hall, user)
            # while is_login is true
            while is_login:
                User.check_role()
                pick = handle_pick()
                if pick == 5:
                    is_login = hall.logout_person(user)
                    break # break because we just want to end loop instead of going till the end
                elif pick == 4:
                    print(user)
                    continue
                title = input("Enter title of the movie: ")
                movie = movie_fetcher.movie_fetch(title) # create movie object

                if pick == 1:
                    flag = True # a flag to check if movie exists in hall
                    for m in hall.movies:
                        if movie.id_ == m:
                            msg = user.reserve(movie, hall) # create reservation if movie exists
                            print(msg)
                            flag = False
                    if flag:
                        print(f"{title} does not exist in {hall.name}")

                elif pick == 2:
                    msg = user.cancel_reserve(movie, hall)
                    print(msg)

                elif pick == 3:
                    user.feedback(movie, hall)
                else:
                    print("Invalid option!")
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
    
