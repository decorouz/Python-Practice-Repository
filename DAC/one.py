#! /usr/bin/env python3

# Generate a random number between 1 and 10
import sys

from random import randint

first = int(sys.argv[1])
second = int(sys.argv[2])
answer = randint(first, second)

# Prompt the user to guess the random number

# check that input is a number 1~10
while True:
    try:
        guess = int(input(f"guess a number {sys.argv[1]}~{sys.argv[2]}: "))

        if guess > second:
            print(f"{guess} is out of range")

        if first <= guess <= second:
            if guess == answer:
                print("You are genius")
                break
            elif guess != answer:
                print(f"{guess} is not correct")
                continue
    except ValueError:
        print("Please enter a valid integer")
        continue
