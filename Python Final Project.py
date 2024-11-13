# NAME: Benjamin Yu
# EMAIL: bzyu@usc.edu
# ID: 9864855206
# DATE: 2022-12-08
# DESCRIPTION: ITP Final project - random movie generator using dictionary with keys as genres and values as a list of movies falling within that genre

import random

# This is the dictionary with keys as the genre and values as a list of movies that fall within said genre
movies = {
        "Action": ["Shang-Chi and the Legend of the 10 rings", "Guardians of the Galaxy", "Rumble in the Bronx", "Rush Hour", "Shanghai Noon"],
        "Horror": ["Us", "Call", "Midsummer", "Barbarian", "Ready or Not", "A Quiet Place"],
        "Animated": ["Your Name", "Castle in the Sky", "Raya and the Last Dragon", "Mulan", "Neon Genesis: Evangelion"],
        "Romantic Comedy": ["Crazy Rich Asians", "The Proposal", "How to Lose a Guy in 10 Days", "The Lost City", "Midnight in Paris"],
        "International": ["Kung Fu Soccer", "Train to Busan", "The Four", "The Great Battle", "Nightmarket (Ye Dian)"]}

# set skip_list to an empty list initially
skip_list = []

# The function generateMovie has a parameter genres and returns a random movie from dictionary
def generateMovie(genres):
    # Set randomGenre to genres (keys) in the dictionary movies
    randomGenre = movies[genres]
    # Set randomMovie to random.choice of randomGenre which randomly chooses a movie from the list found in the dictionary's key
    randomMovie = random.choice(randomGenre)
    return randomMovie


# The function recMovie has parameters movie and userInput
def recMovie(movie, userInput):
    while movie in skip_list:
        movie = generateMovie(userInput)
    if movie not in skip_list:
        print("The movie recommended for you: " + movie)
        skip_list.append(movie)

def main():
    # set x to the integer 1
    x = 1
    # Ask the user to input a genre from the following options and assign it to the variable userInput
    userInput = input("Welcome! Please enter the Genre for the movie you’d like to watch (Action, Horror, Animated, Romantic Comedy, International): ")
    # if the userInput is in movies
    if userInput in movies:
        # Call the function generateMovie with userInput to randomly select a movie from the genre that the user inputted and assign it to movie
        movie = generateMovie(userInput)
        # print the following
        print("The movie recommended for you: " + movie)
        # Append the movie to skip_list
        skip_list.append(movie)
        # else there is an error when the user inputs something not from the list of genres and asks the user to choose from the list of Genres provided
    else:
        input("Error, please enter one of the following options for Genre (Action, Horror, Animated, Romantic Comedy, International): ")
    # While loop starting with while x == 1
    while x == 1:
        # Set skipInput to the user input  Yes or No in response to the question "Would you like to go again?"
        skipInput = input("Would you like to go again? (Yes/No): ")
        # If the user enters Yes
        if skipInput == "Yes":
            # Ask the user if they would like to re-generate from the same genre (Yes or No) and assign it to genreInput
            genreInput = input("Would you like to choose the same genre (Yes/No): ")
            # If the user enters Yes
            if genreInput == "Yes":
                # Assign randomGenre1 to the user inputted Genre which is a key in the dictionary movies
                randomGenre1 = movies[userInput]
                # Assign count to 0
                count = 0
                # For loop startng with for movie in randomGenre1, if the movie is in skip_list, add 1 to count
                for movie in randomGenre1:
                    # if movie is in skip_list
                    if movie in skip_list:
                        # add one to count
                        count += 1
                # If count is equal to the length of randomGenre1
                if count == len(randomGenre1):
                    # print the following statement to tell the user that they have skipped through all the movies in the Genre
                    print("You have skipped through all the movies in the Genre!")
                    # Ask the user to enter a different Genre and assign it to userInput
                    userInput = input("Please enter a different Genre: ")
                # Call the function generateMovie with userInput to randomly select a movie and assign it to the variable movie
                movie = generateMovie(userInput)
                #Call the function recMovie with parameters movie and userInput
                recMovie(movie, userInput)
            # elif the user inputs No to choosing from the same Genre
            elif genreInput == "No":
                # ask the user to input their desired Genre to generate a movie from and assign it to userInput
                userInput = input("Please enter your desired Genre: ")
                # if userInput is in movies
                if userInput in movies:
                    # call the function generateMovie with userInput and generate a random movie and assign it to the variable movie
                    movie = generateMovie(userInput)
                    # call the function recMovie with parameters movie and userInput
                    recMovie(movie, userInput)
                # anything else inputted that would result in an error
                else:
                    # tell the user that an error occurred and they must choose/input from the following list of Genres
                    input("Error, please enter one of the following options for Genre (Action, Horror, Animated, Romantic Comedy, International): ")
        # if user enters No to if they would like to go again
        elif skipInput == "No":
            # print the following statement to thank the user for using the random movie generator
            print("Thank you for using this Movie Generator :)")
            return




if __name__ == "__main__":
    main()


