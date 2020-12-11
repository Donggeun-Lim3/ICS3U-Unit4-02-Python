#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This is while loop program

def main():
    loop_counter = 1
    factorial = 1

    positive_string = input("Enter the positive integer: ")
    print("")
    try:
        positive_number = int(positive_string)
        if positive_number > 0:

            while loop_counter <= positive_number:
                factorial = factorial * loop_counter
                loop_counter = loop_counter + 1
            print(factorial)
        else:
            print("This is negative number")
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
