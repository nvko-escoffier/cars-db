#!/usr/bin/env python3

import csv


def welcome_msg():
    print("\nCars DB extractor program:")


# Print lines that correspond to the brand
def brand(choice):
    print(choice)
    with open('cars.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if choice in row:
                print(row)



if __name__ == '__main__':
    try:
        while True:
            welcome_msg()
            brand(choice = input("Select your brand:"))
    except KeyboardInterrupt:
        print("Interrupted")

