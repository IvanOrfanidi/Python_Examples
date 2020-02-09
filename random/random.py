# Program to generate a random number between low and high
# importing the random module
import random


def main():
    low = int(input('Enter low number: '))
    high = int(input('Enter high number: '))
    rand = random.randint(low, high)
    print('Rand number: {0}'.format(rand))


main()
