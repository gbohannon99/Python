#The Number Guessing Game

#The objective of this program is to create a program that generates a random number and prompts the user to guess it. 
#The program should provide hints to the user, such as "too high" or "too low," until the correct number is guessed


import random 

rand_number = random.randint(1, 20)
validation = False
Guess = False
count = 0

user_guess = input("Try and guess the correct number between 1-20 (type '000' to quit): ")


while Guess == False:
    if(not user_guess.isdigit()):
        user_guess = input("Invalid Input! Please enter a Number! ")
        continue

    user_guess = int(user_guess)
    
    #Checks if the guess is within the boundaries 
    if(user_guess == 000):
        print("\nExiting the Game...")
        break
    
    elif(user_guess > 20 or user_guess < 1):
        print("\nNumber is out of range! Guess a number between 1-20! ")
        user_guess = input("Enter A New Guess: ")
        count += 1

    #Checks if the guess is less than the Target
    elif(user_guess > rand_number):
        print("\nToo High, Guess Again!")
        user_guess = input("Enter A New Guess: ")
        count += 1
    
    #Checks if the guess is greater than the Target
    elif(user_guess < rand_number):
        print("\nToo Low, Guess Again!")
        user_guess = input("Enter A New Guess: ")
        count += 1

    #Checks to see if the guess is correct
    elif(user_guess == rand_number):
        count += 1
        print(f"\nCongrats, you guessed the correct number! It too you {count} tries!")
        Guess = True
    


