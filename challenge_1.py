#!/usr/bin/python3

"""script that asks user for name and day of the week """

def main():

# Ask user for name
    user_name = input("What is your name?")


# Ask user for the day of the week
    day_of_week = input("What day of the week is it?")


# print user name with day of the week
    print(f"Hello, {user_name.capitalize()}! Happy {day_of_week.capitalize()}!")

main()
