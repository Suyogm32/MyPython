# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
movies = []


def main():
    while True:
        ch = input(
            "Enter yoru choice 'a' for adding a movie,'l' for listing a movie,'f' to find a movie,'q' for quit\n")
        match ch:
            case 'a':
                add_movie()
            case 'l':
                show_movies()
            case 'f':
                fproperty = input("Enter the category that you want to find?\n")
                look_for = input("Enter what you looking for?\n")
                find_movie(fproperty, look_for)
            case 'q':
                break
            case _:
                break


def add_movie():
    Name = input("Enter the movie name\n")
    Director = input("Enter the name of Director\n")
    year = input("Enter the release year of movie\n")
    mydict = {}
    mydict['Name'] = Name
    mydict['Director'] = Director
    mydict['Release year'] = year
    movies.append(mydict)


def show_movies():
    for element in movies:
        for key, val in element.items():
            print(f"{key}:{val}")


def show_movie_details(movie):
    for element in movies:
        if element.get('Name') == movie:
            print(f"Name:{element.get('Name')}, ", end="")
            print(f"Director:{element.get('Director')}, ", end="")
            print(f"Release year:{element.get('Release year')}")


def find_movie(exp, finder):
    pointer = False
    for element in movies:
        if element.get(exp) == finder:
            pointer = True
            show_movie_details(element.get('Name'))

    if pointer == False:
        print("No movies Found.\n")


if __name__ == '__main__':
    main()