# bmi = 84 / 1.65**2
# print(bmi)

# print(int(bmi))

# print(round(bmi))

# print(round(bmi, 2)

# score = 0

# score += 1

# print(score)

# print(f"Your score is {score}")


# score = 0
# height = 1.8
# is_winning = True
# print(
#     f"Your score is = {score}, your height is {height}, you are winning is {is_winning}"
# )
# print(int("5") / int(2.7))


# Day 2 Project
print("Welcome to the tip calculator.")
bill = float(input("what is the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tipAmount = (tip / 100) * bill
# print(f"Your total bill is ${bill} and your tip amount is ${tipAmount}")
billPerPerson = round((bill + tipAmount) / people, 2)
print(f"Each person should pay: ${billPerPerson}")
