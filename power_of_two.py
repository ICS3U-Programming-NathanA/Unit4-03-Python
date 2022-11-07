#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Oct 6 2022
# This program determines the squared of the users number and the numbers before it


def main():

    power_of_two = 0
    # Get the users number
    user_num_string = input("Enter a integer: ")

    # An try catch to catch any errors if they enter a string or a decimal
    try:
        user_num = int(user_num_string)
    except Exception:
        print("Please a enter whole number")
    else:
        # An if statement to see if the integer is a negative
        if user_num >= 0:
            # A for loop to calculate the squared of the users number and the numbers before it
            for counter in range(user_num + 1):
                power_of_two = counter**2
                print("{}^2 = {}".format(counter, power_of_two))
        else:
            print("Please a enter positive whole number")


if __name__ == "__main__":
    main()
