import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to rock, paper, scissors!")
userChoice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
choices = [rock, paper, scissors]
computerChoice = random.randint(0, 2)

# if userChoice == 0:
#     print(f"You chose {rock}")
# elif userChoice == 1:
#     print(f"You chose {paper}")
# elif userChoice == 2:
#     print(f"You chose {scissors}")

if (userChoice >= 0) and (userChoice <= 2):
    print(f"You chose {choices[userChoice]}")
else:
    print("You entered an invalid number")
print(f"Computer chose {choices[computerChoice]}")
if userChoice == computerChoice:
    print("Draw")

elif (
    userChoice == 0
    and computerChoice == 2
    or userChoice == 1
    and computerChoice == 0
    or userChoice == 2
    and computerChoice == 1
):
    print("You win")
else:
    print("You lose")
