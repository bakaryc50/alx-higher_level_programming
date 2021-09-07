#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print("{} is {}\n".format(
    number, "positive" if number > 0 else "negative" if number else "zero"
))

