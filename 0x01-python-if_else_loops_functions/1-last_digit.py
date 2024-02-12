#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
str = f'Last digit of {number} is {last}'
if last > 5:
    print(str + ' and is greater than 5')
elif last == 0:
    print(str + ' and is 0')
elif last < 6:
    print(str + ' and is less than 6 and not 0')
