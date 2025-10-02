# print("welcome to the rollercoaster!")
# height = int(input("Please enter your height in cm: "))
# age = int(input("Please enter your age: "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     if age < 12:
#         print("Please pay $5")

#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")

# else:
#     print("You can't ride the rollercoaster")


# print("welcome to the rollercoaster!")
# height = int(input("Please enter your height in cm: "))
# age = int(input("Please enter your age: "))
# ticketPrice = 0
# if height >= 120:
#     print("You can ride the rollercoaster")
#     if age < 12:
#         print("Child tickets are $5")
#         ticketPrice = 5

#     elif age <= 18:
#         print("Youth tickets are $7")
#         ticketPrice = 7
#     else:
#         print("Adult tickets are $12")
#         ticketPrice = 12
#     wantPhoto = input("Do you want a photo taken? Y or N. ")
#     if wantPhoto == "Y":
#         ticketPrice += 3
#     print(f"Your final bill is ${ticketPrice}")

# else:
#     print("You can't ride the rollercoaster")


print("welcome to the rollercoaster!")
height = int(input("Please enter your height in cm: "))
age = int(input("Please enter your age: "))
ticketPrice = 0
if height >= 120:
    print("You can ride the rollercoaster")
    if age < 12:
        print("Child tickets are $5")
        ticketPrice = 5

    elif age <= 18:
        print("Youth tickets are $7")
        ticketPrice = 7
    # elif age >= 45 and age <= 55:
    elif 45 <= age <= 55:
        print("You got free ticket")

    else:
        print("Adult tickets are $12")
        ticketPrice = 12
    wantPhoto = input("Do you want a photo taken? Y or N. ")
    if wantPhoto == "Y":
        ticketPrice += 3
    print(f"Your final bill is ${ticketPrice}")

else:
    print("You can't ride the rollercoaster")
