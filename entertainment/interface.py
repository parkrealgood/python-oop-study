from typing import Protocol


class Bookable(Protocol):
    def get_title(self) -> str:
        pass

    def get_rating(self) -> int:
        pass


class Watchable(Protocol):
    def get_title(self) -> str:
        pass
