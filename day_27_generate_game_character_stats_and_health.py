import random
import os
import time


def generate_character():
    name = input("Name your Legend: ")
    char_type = input("Character Type (Human, Elf, Wizard, Orc): ")
    return {"name": name, "type": char_type}


def roll_dice(sides):
    return random.randint(1, sides)


def health_stamp():
    return ((roll_dice(6) * roll_dice(12)) / 2) + 10


def stength_stat():
    return ((roll_dice(6) * roll_dice(8)) / 2) + 12


if __name__ == "__main__":

    print("WELCOME TO THE CHARACTER BUILDER PROGRAM")
    print()

    while True:
        name = generate_character()["name"]
        print()
        print(name.upper())
        print("HEALTH:", health_stamp())
        print("STRENGTH:", stength_stat())
        print()
        print("May your name go down in Legends...")
        print()
        if input("Again(Yes or No)?: ").lower().strip() != "yes":
            break

        time.sleep(1)
        os.system("cls")
