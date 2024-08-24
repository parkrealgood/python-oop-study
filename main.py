from entertainment.movie import Movie
from audience.audience import Audience


def main():
    audience1 = Audience(name='John', age=25)
    audience2 = Audience(name='Peter', age=7)

    audience1.move(destination='London')

    movie1 = Movie(1, 'The Godfather', rating=7)
    movie2 = Movie(2, 'The Dark Knight', rating=15)
    movie3 = Movie(3, 'The Shawshank Redemption', rating=19)

    is_booked1 = audience1.book(item=movie1)
    audience1.watch(item=movie1) if is_booked1 else print(f"{audience1.name} cannot watch {movie1.get_title()}.")

    is_booked2 = audience2.book(item=movie3)
    audience2.watch(item=movie3) if is_booked2 else print(f"{audience2.name} cannot watch {movie3.get_title()}.")


if __name__ == "__main__":
    main()
