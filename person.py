from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email, phone, id_):
        pass

    def __str__(self):
        pass

    @abstractmethod
    def check_role(self):
        pass