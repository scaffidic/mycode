#!/usr/bin/env python3

round = 0

while True:
    round += 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    if answer == "Brian":
        print("Correct!")
        break
    elif round == 3:
        print("Sorry! The answer was Brian.")
        break
    else: 
        print("Sorry! Try again!")


