import time
from getpass import getpass as input

user1 = 0
user2 = 0

print("WELCOME TO A GAME OF ROCK PAPER SCISORS!")
print()
print()
print("You will play in competition with another user1")
print("You get to choose among yourselfs who is user 1 ")
print("and who is user 2. Each user will play for 3 rounds ")
print("before the game altimately decides who is the winner.")
print("To choose rock, type r as your input.")
print("To choose paper, type p as your input.")
print("To choose scisors, type s as your input.")
print("GOOD LUCK!")

valid_plays = ['r', 'p', 's']

for i in range(3):
    user1_input = input("User one play round " + str(i) + ": ").lower()
    while True:
        if user1_input not in valid_plays:
            user1_input = input(
                "You have entered an invalid play :( Please choose between 'r', 'p' and 's': ")
        else:
            break

    user2_input = input("User two play round " + str(i) + ": ").lower()
    while True:
        if user2_input not in valid_plays:
            user2_input = input(
                "You have entered an invalid play :( Please choose between 'r', 'p' and 's': ")
        else:
            break

    if user1_input == "r" and user2_input == "r":
        continue
    elif user1_input == "r" and user2_input == "p":
        user2 += 1
    elif user1_input == "r" and user2_input == "s":
        user1 += 1
    elif user1_input == "p" and user2_input == "r":
        user1 += 1
    elif user1_input == "p" and user2_input == "p":
        continue
    elif user1_input == "p" and user2_input == "s":
        user2 += 1
    elif user1_input == "s" and user2_input == "r":
        user2 += 1
    elif user1_input == "s" and user2_input == "p":
        user1 += 1
    elif user1_input == 's' and user2_input == 's':
        continue

print("*******************GAME RESULTS*******************")
time.sleep(2)
print("Congratulations to all players for playing.")

if user1 > user2:
    print("The winner of this round was...")
    time.sleep(5)
    for i in range(5):
        print("*" * i)
    print("***** User one!")
    for i in range(4, -1, -1):
        print("*" * i)
if user2 > user1:
    print("The winner of this round was...")
    time.sleep(5)
    for i in range(5):
        print("*" * i)
    print("***** User two!")
    for i in range(4, -1, -1):
        print("*" * i)
else:
    print("The game ends in a draw :/")

print("Below are the game results.")
print("User one results:", user1)
print("User two results: ", user2)
print("THE END")
