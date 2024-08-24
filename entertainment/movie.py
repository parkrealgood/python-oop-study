from entertainment.interface import Bookable, Watchable


class Movie(Bookable, Watchable):
    def __init__(self, number: int, title: str, rating: int):
        self.number = number
        self.title = title
        self.rating = rating

    def __str__(self):
        return f'{self.number}] {self.title}'

    def get_title(self) -> str:
        return self.title

    def get_rating(self) -> int:
        return self.rating