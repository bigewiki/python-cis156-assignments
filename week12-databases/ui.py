#!/usr/bin/env/python3

import db
from objects import Movie

def display_title():
    print("The Movie List program")
    print()    
    display_menu()

def display_menu():
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("year - View movies by year")
    # STEP 7 modify display menu to provide for min command
    print("min  - View movies by minutes")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()    

def display_categories():
    print("CATEGORIES")
    categories = db.get_categories()    
    for category in categories:
        print(str(category.id) + ". " + category.name)
    print()

def display_movies(movies, title_term):
    print("MOVIES - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
    print("-" * 64)
    for movie in movies:
        print(line_format.format(str(movie.id), movie.name,
                                 str(movie.year), str(movie.minutes),
                                 movie.category.name))
    print()    

def display_movies_by_category():
    category_id = int(input("Category ID: "))
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_category(category_id)
        display_movies(movies, category.name.upper())
    
def display_movies_by_year():
    year = int(input("Year: "))
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, str(year))

def add_movie():
    name        = input("Name: ")
    year        = int(input("Year: "))
    minutes     = int(input("Minutes: "))
    category_id = int(input("Category ID: "))
    
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID. Movie NOT added.\n")
    else:        
        movie = Movie(name=name, year=year, minutes=minutes,
                      category=category)
        db.add_movie(movie)    
        print(name + " was added to database.\n")

def delete_movie():
    movie_id = int(input("Movie ID: "))
    # Get a movie by the ID
    movies = db.get_movie_by_id(movie_id)
    # display to the user
    display_movies(movies, f'Movie ID {movie_id}')
    # ask whether user is sure they want to delete the movie
    print("Are you sure you want to delete the above movie?")
    # Should only delete when the user enters "y"
    answer = input("Type 'y' to confirm: ")
    if answer.lower() == "y":
        db.delete_movie(movie_id)
        print("Movie ID " + str(movie_id) + " was deleted from database.\n")
    else:
        # just in case they don't type y
        print("No movie was deleted")

# Step 6: add a display_movies_by_minutes() function that prompts the user
# to enter the maximum numbe rof minutes and displays all selected movies.
# sort by minutes in ascending order
def display_movies_by_minutes():
    # get minute input from user
    minutes = int(input("Enter maximum number of minutes: "))
    # run the function to get the matching rows
    movies = db.get_movies_by_minutes(minutes)
    # display to user
    display_movies(movies, f'Runtime less than {minutes}')
        
def main():
    db.connect()
    display_title()
    display_categories()
    while True:        
        command = input("Command: ")
        if command == "cat":
            display_movies_by_category()
        elif command == "year":
            display_movies_by_year()
        elif command == "add":
            add_movie()
        elif command == "del":
            delete_movie()
        # Update main() to provide for min command
        elif command == "min":
            display_movies_by_minutes()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
