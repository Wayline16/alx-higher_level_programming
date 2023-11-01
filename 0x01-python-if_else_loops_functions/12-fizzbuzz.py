#!/usr/bin/python3
for number in range(1, 100):
    if number % 3 == 0 and number % 9 != 0:
        print('Fizz ')
    if number % 9 == 0 and number % 3 != 0:
        print('Buzz ')
    if number % 9 == 0 and number % 3 == 0:
        print('FizzBuzz ')
    else:
        print(f'{number}')