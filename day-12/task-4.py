import art
import random


def get_user_attempts():
    """
    Asks the user for a difficulty and returns the corresponding number of attempts.

    The user is prompted to type 'easy' or 'hard'. If the user types 'easy', the function returns 10 attempts. If the user types 'hard', the function returns 5 attempts. If the user types anything else, the function recursively calls itself until the user types 'easy' or 'hard'.

    Returns:
        int: The number of attempts based on the user's difficulty choice.
    """
    messsage = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if messsage == "easy":
        return 10
    elif messsage == "hard":
        return 5
    else:
        return get_user_attempts()


def welcome_screen():
    """
    Prints a welcome message to the user, including the game's logo.
    """
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def guess_number():
    """
    Returns a random integer between 0 and 100.

    Returns:
        int: A random integer between 0 and 100.
    """
    return random.randint(0, 100)


def play_guess_number():
    """
    Plays a round of the number guessing game.

    First, it calls the welcome_screen function to print the game's logo and a welcome message.
    Then, it generates a random number between 0 and 100 using the guess_number function.
    The user is then prompted to make a guess. If the guess is correct, the function prints a success message and returns.
    If the guess is too high or too low, the function prints an appropriate message and decrements the number of attempts.
    If the user runs out of attempts, the function prints a failure message and returns.
    """
    welcome_screen()
    number = guess_number()
    attempts = get_user_attempts()
    while attempts > 0:
        print(f"You have {attempts} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}")
            return
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1
    print(f"You've run out of guesses, you lose. The answer was {number}")


play_guess_number()
