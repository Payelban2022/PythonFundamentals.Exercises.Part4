import random
n = random.randint(1,100)

guess = int(input("Give me a number from 1 to 100: "))

while guess != n:
    if guess < n:
        print("Too low")
        guess = int(input("Give me a number from 1 to 100: "))

    else:

        print("Too high")
        guess = int(input("Give me a number from 1 to 100: "))

print("You got it.")





