# Guessing number when user set the lower bound and upper bound . then user has 7 attempt to make correct within this boundary
#then print correct if user dont find that number then print sorry  better luck next time .
import random
print("Hello Guys! Welcome to the Number Guessing Game ");
low=int(input("Enter the Lower bound: "))
high=int(input("Enter the Higher Bound: "))
print(f"\n you have 7 chancs to guess the number between{low} and {high}. Let's Start!");
num=random.randint(low,high)
ch=7# total allowed counter
gc=0#guess counter
while gc<ch:
    gc+=1
    guess=int(input('Enter your guess: '))

    if guess==num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempt.')
        break
    elif gc>=ch and guess !=num:
        print(f'Sorry!. the number was {num}. Better luck next time.')

    elif guess>num:
        print('Too high ! try a lower number')

    elif guess<num:
        print('Too low! try a higher number.')