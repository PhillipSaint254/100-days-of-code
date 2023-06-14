from day_27_generate_game_character_stats_and_health import *

char1 = generate_character()
user1_health = health_stamp()
user1_strength = stength_stat()

print(char1["name"].upper())
print("HEALTH:", user1_health)
print("STRENGTH:", user1_strength)
print()
print("Who are they battling?")
print()
user2_health = health_stamp()
char2 = generate_character()
user2_strength = stength_stat()

print(char1["name"].upper())
print("HEALTH:", user1_health)
print("STRENGTH:", user1_strength)
print()

time.sleep(1)

print("BATTLE TIME")
print()
print("The battle begins!")

rounds = 1
print()
user1_roll = roll_dice(6)
user2_roll = roll_dice(6)

hit = abs(user1_strength - user2_strength) + 1

if user1_roll > user2_roll:
    print(char1["name"] + " wins the first blow.")
    print(char2["name"] + " takes a hit with " +
          str(hit) + " damage.")
    user2_health -= hit

elif user1_roll < user2_roll:
    print(char2["name"] + " wins the first blow.")
    print(char1["name"] + " takes a hit with " +
          str(hit) + " damage.")
    user1_health -= hit

while True:
    time.sleep(1)
    print()
    print(char1["name"], "health", user1_health)
    print(char2["name"], "health", user2_health)
    print()
    time.sleep(1)

    user1_roll = roll_dice(6)
    user2_roll = roll_dice(6)

    if user1_roll > user2_roll:
        print(char1["name"] + " wins round " + str(rounds))
        print(char2["name"] + " takes a hit with " +
              str(hit) + " damage.")
        user2_health -= hit

    elif user1_roll < user2_roll:
        print(char2["name"] + " wins round " + str(rounds))
        print(char1["name"] + " takes a hit with " +
              str(hit) + " damage.")
        user1_health -= hit
    else:
        print("Their swords clash and they draw round", rounds)

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

    rounds += 1
