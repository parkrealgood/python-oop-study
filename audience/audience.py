from entertainment.interface import Bookable, Watchable
from person.person import Person


class Audience(Person):

    def book(self, item: Bookable) -> bool:
        if self.age < item.get_rating():
            print(f"{self.name} cannot book {item.get_title()} because it is not suitable for children.")
            return False
        print(f"{self.name} has booked {item.get_title()}.")
        return True

    def watch(self, item: Watchable):
        print(f"{self.name} is watching {item.get_title()}.")
