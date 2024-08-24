from typing import Protocol


class Person(Protocol):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def move(self, destination: str):
        print(f'{self.name} is moving to {destination}')

    def speak(self, message: str):
        print('Person says: ', message)
