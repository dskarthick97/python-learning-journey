""" Higher or Lower game """

from random import choice
from os import system

from art import logo, vs
from game_data import data


count = 0


def get_random_data():
    random_data = choice(data)
    name_ = random_data.get("name")
    description = random_data.get("description")
    country = random_data.get("country")
    follower_count = random_data.get("follower_count")

    return name_, description, country, follower_count


def compare(choise, count_one, count_two):
    if choise == "A":
        return count_one > count_two
    else:
        return count_two > count_one 


def lets_play(name, description, country, follower_count):
    print(logo)

    second_name, second_description, second_country, second_follower_count = get_random_data()
    while follower_count == second_follower_count:
        second_name, second_description, second_country, second_follower_count = get_random_data()

    global count
    if count > 0:
        print(f"You're right! Current Score: {count}")
    
    print(f"Compare A: {name}, {description} , from {country}.")
    print(vs)
    print(f"Compare B: {second_name}, {second_description} , from {second_country}.")
    
    res = input("Who has more followers? Type 'A' or 'B': ").upper()
    result = compare(res, follower_count, second_follower_count)
    if result:
        count += 1
        system("clear")
        lets_play(second_name, second_description, second_country, second_follower_count)
    
    if not result:
        system("clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score {count}")


if __name__ == '__main__':
    first_name, first_description, first_country, first_follower_count = get_random_data()
    
    lets_play(
        name=first_name, 
        description=first_description, 
        country=first_country, 
        follower_count=first_follower_count
    )
