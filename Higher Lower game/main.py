from art import *
from data import data
import random


# 1. Randomly choose 2 people to compare
def random_choice():
    return random.choice(data)


# 2. Compare 2 people and print the result
def compare_a_vs_b(guess, a_followers, b_followers):
    if a_followers >= b_followers:
        return guess == "a"
    else:
        return guess == "b"


# 3. Print information
def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}."


def game():
    print(logo)
    score = 0
    compare_a = random_choice()
    compare_b = random_choice()
    stop_game = False
    while not stop_game:
        compare_a = compare_b
        compare_b = random_choice()
        while compare_a == compare_b:
            compare_b = random_choice()
        print(f"Compare A: {format_data(compare_a)}")
        print(vs)
        print(f"Compare B: {format_data(compare_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = compare_a['follower_count']
        b_followers = compare_b['follower_count']
        is_correct = compare_a_vs_b(guess, a_followers, b_followers)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            stop_game = True
            print(f"Sorry, that's wrong. Final score: {score}")


game()
