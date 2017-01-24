'''This script prints out all integers from 1 to 100,
except replacing any number that is divisible by 3
with "Fizz", any number that is divisible by 5 with
"Buzz", and any number that is divisible by both 5 and 3 with "FizzBuzz." '''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0: print("Fizz")
    elif i % 3 != 0 and i % 5 == 0: print("Buzz")
    elif i % 3 == 0 and i % 5 == 0: print("FizzBuzz")
    else: print(i)
