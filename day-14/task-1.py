from game_data import data
import random
import os
import art


def check_answer(guess, a_follower, b_follower):
    return guess == "a" if a_follower > b_follower else guess == "b"


def get_random_account():
    return data[random.randint(0, len(data) - 1)]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def paly_the_game():
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()
        while account_a["follower_count"] == account_b["follower_count"]:
            account_b = get_random_account()

        print(
            f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}."
        )
        print(
            f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}."
        )
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        clear()
        print(art.logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")


paly_the_game()
