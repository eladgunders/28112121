from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def __init__(self, id_, name, address, age):
        self.id_ = id_
        self.name = name
        self.address = address
        self.age = age

    @abstractmethod
    def calculate_salary(self):
        return

    def __str__(self):
        return f'Employee[id_ = {self.id_}, name = {self.name}, address = {self.address}, age = {self.age}]'

