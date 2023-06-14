import random
print("Today's game will be testing your maths skills.")
print("""
You will be prompted for a number. You will then be asked
to fill a multiplication table for the number you provided.
You will then be grade out of 10. GOOD LUCK!
""")

user_number = int(input("Enter a number: "))
grade = 0
used = []

for i in range(10):
    number = random.randint(1, 10)
    while number in used:
        if len(used) == 10:
            break
        number = random.randint(1, 10)

    used.append(number)
    answer = int(input(str(user_number) + " x " + str(number) + " = "))
    correct_answer = number * user_number
    if correct_answer:
        print("Correct! You have earned 1 point.")
        grade += 1
    else:
        print("Incorrect. " + str(user_number) + " x " +
              str(number) + " should equal " + str(correct_answer))

print("Congratulations on finishing the table of " + str(user_number))
print("You have scored " + str(grade) + "/10")
