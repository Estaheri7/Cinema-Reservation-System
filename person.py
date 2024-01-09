from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email, phone, id_):
        self.name = name
        self.email = email
        self.phone = phone
        self.id_ = id_
        self.is_regestered = False
        self.is_loggin = False

    def __str__(self):
        return f"Name: {self.name}"

    @abstractmethod
    def check_role():
        pass