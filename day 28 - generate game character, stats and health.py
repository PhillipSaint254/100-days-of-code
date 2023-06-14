import random

print("WELCOME TO THE CHARACTER BUILDER PROGRAM")
print()


def generate_caharacter():
    name = input("Name your Legend: ")
    char_type = input("Character Type (Human, Elf, Wizard, Orc): ")
    return name


def health_stamp(sided, roll):
    return (((6-sided-roll) * (12-sided-roll)) / 2) + 10


def stength_stat(sided, roll):
    return (((6-sided-roll) * (8-sided-roll)) / 2) + 12


while True:
    sided = 6
    roll = random.randint(1, 6)

    print()
    print(generate_caharacter())
    print("HEALTH:", health_stamp(sided, roll))
    print("STRENGTH:", stength_stat(sided, roll))
    print()
    print("May your name go down in Legends...")
    print()
    if input("Again(Yes or No)?: ").lower().strip() != "yes":
        break
