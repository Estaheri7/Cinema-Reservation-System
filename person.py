from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email, phone, id_):
        self.name = name
        self.email = email
        self.phone = phone
        self.id_ = id_

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\n"

    @abstractmethod
    def check_role():
        pass