import random

print("""
Today we play a guessing game. You are going to choose
a random number between 1 and 1 million :) and then I'll 
tell you if your guess is what I have. If the number is 
too hight, I'll tell you 'too high'. If it's too low, I'll
tell you 'too low'. You win by getting the guess right.
""")
print("The number of attempts also figures in calculating your core.")
print("To exit the game, simply enter a negative number :(")
print("GOOD LUCK!")

lucky_number = random.randint(1, 1000000)
attemts = 0

user_guess = int(input("Enter your guess: "))

while True:
    if user_guess < 0:
        print("You have ended the game :(")
        break
    if user_guess > lucky_number:
        user_guess = int(input("Too high, try again: "))
    elif user_guess < lucky_number:
        user_guess = int(input("Too low, try again: "))
    else:
        print("Your guess is correct! Congratulation, you win the game in " +
              str(attemts) + " attempts.")
        break
    attemts += 1
