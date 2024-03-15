print("30 Days Down - What do you think?")

for i in range(1, 31):
    print(f"Day {i}")
    experience = input()
    experience = f"{experience:^50}"

    text = "You though Day {i} was amazing".format(i=i)
    text = f"{text:^50}"

    print(text)
    print(experience)

