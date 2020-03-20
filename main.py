#!/usr/bin/env python3

import csv

manufacturer = ['audi', 'bmw', 'mercedes']


def welcome_msg():
    print("\nCars DB extractor program:")


# Print lines that correspond to the brand
def brand(choice):
    print(choice)
    with open('cars.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if manufacturer[int(choice)] in row:
                print(row)


if __name__ == '__main__':
    try:
        while True:
            welcome_msg()
            for position, item in enumerate(manufacturer):
                print(" ", position, item)
#                print(item, manufacturer[int(item)])
#                print(manufacturer[item)]
#                print(item)

            choice = input("Select your brand: ")
            brand(choice)
    except KeyboardInterrupt:
        print("Interrupted")

