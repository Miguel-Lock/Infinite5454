#!/usr/bin/env python3

import random
from time import sleep

def print_char(char):
    # prints char and them sleeps for a small amout of time
    sleep_length = random.randint(1, 39) / 150
    print(char, end = "", flush = True)
    sleep(sleep_length)

def main():
    # collects the length of the line
    limit = int(input("Enter the length of the line\n>"))

    for i in range(100000000):
        # finds the actual length of the 5454 line
        length = random.randint(1, round(limit / 2))
        round(length)
        
        for i in range(length):
            print_char(5)
            print_char(4)
        print()

if __name__ == "__main__":
    main()
