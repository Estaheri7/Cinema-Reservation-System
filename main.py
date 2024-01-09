from user import *
from employee import *
from cinemahall import *
from movie_manager import *

def help():
    print("""Welcome to the Cinema:
What is your role in hall?
1- Employee
2- Member
press Q to Exit""")

def get_details():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    return name, email, phone

def RorL(method, cinema_hall, person):
    if method == "register":
        is_login = cinema_hall.add_person(person)
        print(cinema_hall)
    elif method == "log in":
        try:
            is_login = cinema_hall.log_person(person)
        except ValueError as e:
            print(e)
            return False
    else:
        print("Invalid command!")
        return False
        
    return is_login

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
            position = input("Enter your position: ")

            emp = Employee(name, email, phone, emp_id, position)

            is_login = RorL(method, hall, emp)
            
            while is_login:
                Employee.check_role()
                pick = int(input())

                if pick == 1:
                    title = input("Enter title of the movie: ")
                    movie = movie_fetcher.movie_fetch(title)
                    emp.add_movie(movie, hall)

                elif pick == 2:
                    hall.show_movies()

                elif pick == 3:
                    print(hall.all_reservations)

                elif pick == 4:
                    is_login = hall.logout_person(emp)

                else:
                    print("Invalid option!")

        elif choice == '2':
            name, email, phone = get_details()
            user_id = input("Enter your user ID: ")
            user = User(name, email, phone, user_id)

            is_login = RorL(method, hall, user)

            while is_login:
                User.check_role()
                pick = int(input())

                if pick == 4:
                    is_login = hall.logout_person(user)
                    break
                
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
    
