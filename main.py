from user import *
from employee import *
from cinemahall import *
from movie_manager import *

def help():
    print("""Welcome to the Cinema:
What is your role in hall?
1 - Employee
2 - Member
press Q to Exit.""")

def get_details():
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    while True:
        try:
            phone = int(input("Enter your phone number: "))
            break
        except ValueError:
            print("Invalid PhoneNumber! Please enter a numeric value for the phone number.")

    return name, email, phone


def RorL(method, cinema_hall, person):
    if method == "register":
        is_login = cinema_hall.add_person(person)
    elif method == "log in":
        try:
            is_login = cinema_hall.log_person(person)
        except EmailNotRegistered as e:
            print(e)
            return False
    else:
        print("Invalid method!")
        return False
        
    return is_login

def handle_pick():
    try:
        pick = int(input())
        return pick
    except ValueError:
        print("Please enter a number between 1-n!\n")
        return 0

def main():
    hall = CinemaHall("H1", 20)
    movie_fetcher = MovieFetch()

    while True:
        help()
        is_login = False
        choice = input().upper()

        if choice == 'Q':
            break

        method = input("do you want to register or log in? ")

        if choice == '1':
            name, email, phone = get_details()
            emp_id = input("Enter your employee ID: ")
            position = input("Enter your position (Movie manager, User manager, Reserve manager): ").lower()

            emp = Employee(name, email, phone, emp_id, position)

            is_login = RorL(method, hall, emp)
            
            while is_login:
                if emp.position == "movie manager":
                    emp.check_role()
                    pick = handle_pick()
                    if pick == 0:
                        continue
                    if pick == 1:
                        title = input("Enter title of the movie: ")
                        movie = movie_fetcher.movie_fetch(title)
                        try:
                            emp.add_movie(movie, hall)
                        except TypeError as e:
                            print(e)

                    elif pick == 2:
                        title = input("Enter title of the movie: ")
                        movie = movie_fetcher.movie_fetch(title)
                        try:
                            emp.remove_movie(movie, hall)
                        except TypeError as e:
                            print(e)

                    elif pick == 3:
                        hall.show_movies()

                    elif pick == 4:
                        is_login = hall.logout_person(emp)

                    else:
                        print("Invalid option!")

                elif emp.position == "user manager":
                    emp.check_role()
                    pick = handle_pick()
                    if pick == 0:
                        continue

                    if pick == 4:
                        is_login = hall.logout_person(emp)

                    elif pick == 1:
                        email = input("Enter user email: ")
                        user = User(name = None, email = email, phone = None, user_id = None)
                        hall.add_person(user)

                    elif pick == 2:
                        email = input("Enter user email: ")
                        user = User(name = None, email = email, phone = None, user_id = None)
                        hall.remove_user(user)

                    elif pick == 3:
                        hall.show_users()

                    else:
                        print("Invalid option!")

                elif emp.position == "reserve manager":
                    emp.check_role()
                    pick = handle_pick()
                    if pick == 0:
                        continue
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
                        movie = movie_fetcher.movie_fetch(title)

                        flag = True
                        for m in hall.movies:
                            if movie.id_ == m:
                                flag = False
                        if flag:
                            print(f"{title} does not exist in {hall.name}")
                            continue

                        if pick == 1:
                            user.reserve(movie, hall)

                        elif pick == 2:
                            user.cancel_reserve(movie, hall)
                        
                        else:
                            print("Invalid option!")
                            
                    else:
                        print(f"{email} does not exist in Hall")

                else:
                    hall.logout_person(emp)
                    print("Invalid position for employee!")
                    break

        elif choice == '2':
            name, email, phone = get_details()
            user_id = input("Enter your user ID: ")
            user = User(name, email, phone, user_id)

            is_login = RorL(method, hall, user)

            while is_login:
                User.check_role()
                pick = handle_pick()
                if pick == 0:
                    continue

                if pick == 5:
                    is_login = hall.logout_person(user)
                    break
                elif pick == 4:
                    print(user)
                    continue
                title = input("Enter title of the movie: ")
                movie = movie_fetcher.movie_fetch(title)

                if pick == 1:
                    flag = True
                    for m in hall.movies:
                        if movie.id_ == m:
                            user.reserve(movie, hall)
                            print(user.reservation)
                            flag = False
                    if flag:
                        print(f"{title} does not exist in {hall.name}")

                elif pick == 2:
                    user.cancel_reserve(movie, hall)

                elif pick == 3:
                    user.feedback(movie, hall)
                else:
                    print("Invalid option!")
        else:
            print("Invalid command!")



if __name__ == "__main__":
    main()
    
