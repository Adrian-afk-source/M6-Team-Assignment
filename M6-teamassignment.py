e#the code should first print "guess the number that is 1 to 10"
#While doing so the code should choose a random number from a generator, 1 to 100
#The user will then type a number of their choosing
#IF the user picks a higher number than the number chosen print "Please guess lower"
#Else the user picks lower than the number chosen print "Please guess higher"

import random
random_number = random.randint(1,10)
print ("Please guess number between 1 and 10")
guess = input("Enter your guess ")
guess = int(guess)
if guess < 1 or guess > 10:
    print ("Your number must be between 1 or 10")
if guess < random_number:
    print("Please enter higher number")
elif guess > random_number:
    print ("Please enter lower number")
else:
    print("congratulations you did it")

#Looping Code
import random

random_number = random.randint(1, 10)
print("Please guess a number between 1 and 10")

while True:
    guess = input("Enter your guess: ")
    
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if guess < 1 or guess > 10:
        print("Your number must be between 1 and 10.")
    elif guess < random_number:
        print("Please enter a higher number.")
    elif guess > random_number:
        print("Please enter a lower number.")
    else:
        print("Congratulations! You did it.")
        break
        
