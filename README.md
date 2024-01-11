# Cinema Reservation System

The Cinema Reservation System is an open-source project designed to facilitate the reservation process for cinema-goers. This system aims to provide a seamless experience for users, employees, and movie managers, streamlining movie bookings, user registrations, and feedback processes.

## Features

- **User Registration and Login:**
  - Register and log in with a valid email.
  - Secure authentication process managed by the `AccountManager` class.

- **Employee Management:**
  - `Employee` class allows employees to perform actions based on their roles, such as managing movies, users, and reservations.

- **Movie Management:**
  - Add and remove movies to and from cinema halls.
  - Display a list of available movies.

- **User Management:**
  - Add and remove user emails from cinema halls.
  - Display a list of registered users.

- **Reservation System:**
  - Reserve and cancel seats for movies.
  - Display all reservations made in the cinema hall.

- **Feedback System:**
  - Users can provide feedback on movies, including ratings and comments.

## Tech Stack

- **Programming Language:** Python3
- **Libraries/Frameworks:** `requests` for API communication
- **Data Storage:** JSON for storing movie details

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/cinema-reservation-system.git
    cd cinema-reservation-system
    ```

2. Install the required Libraries/Frameworks:
    
    ```bash
    pip install -requests
    ```

3. Run the main program:

    ```bash
    python main.py
    ```
