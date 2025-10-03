import random

# randomInteger = random.randint(1, 10)
# print(randomInteger)


# random_number_0_1 = random.random()
# print(int(random_number_0_1 * 100))


# random_float = random.uniform(1, 10)
# print(random_float)


# headOrTail = int(random.random() * 2)
headOrTail = random.randint(0, 1)

if headOrTail == 0:
    print("Heads")
elif headOrTail == 1:
    print("Tails")
