#!/usr/bin/env python3

#from os import system


def welcome_msg():
    return print("Cars DB extractor program:")


if __name__ == '__main__':
    try:
        while True:
            input(welcome_msg())
    except KeyboardInterrupt:
        print("Interrupted")

