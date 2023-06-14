from day_27_generate_game_character_stats_and_health import *

char1 = generate_character()
print()
print("Who are they battling?")
print()
char2 = generate_character()
user1_health = health_stamp()
user2_health = health_stamp()
user1_strength = stength_stat()
user2_strength = stength_stat()

print("BATTLE TIME")
print()
print("The battle begins!")

rounds = 1
print()
user1_roll = roll_dice(6)
user2_roll = roll_dice(6)

if user1_roll > user2_roll:
    print(char1["name"] + " wins the first blow.")
    print(char2["name"] + " takes a hit with " +
          str(user1_roll) + " damage.")
    user2_health -= user1_roll

elif user1_roll < user2_roll:
    print(char2["name"] + " wins the first blow.")
    print(char1["name"] + " takes a hit with " +
          str(user2_roll) + " damage.")
    user1_health -= user2_strength

while True:
    time.sleep(1)
    print()
    if user1_roll > user2_roll:
        print(char1["name"] + " wins round " + str(rounds))
        print(char2["name"] + " takes a hit with " +
              str(user2_strength) + " damage.")
        user2_health -= user1_strength

    elif user1_roll < user2_roll:
        print(char2["name"] + " wins the first blow.")
        print(char1["name"] + " takes a hit with " +
              str(user2_strength) + " damage.")
        user1_health -= user2_strength

    time.sleep(1)
    print()

    if user1_health <= 0:
        print(char2["name"] + " destroyed " + char1["name"] +
              " in " + str(rounds) + " rounds!")
        break
    elif user2_health <= 0:
        print(char1["name"] + " destroyed " + char2["name"] +
              " in " + str(rounds) + " rounds!")
        break

    time.sleep(1)
    os.system("cls")
    print("The battle continues")
    print()
    user1_roll = roll_dice(6)
    user2_roll = roll_dice(6)

    rounds += 1
