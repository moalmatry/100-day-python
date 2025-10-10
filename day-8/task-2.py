# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")


# greet_with("Jack", "New York")
# greet_with(location="New York", name="Jack")


def calculate_love_score(name1, name2):
    nameLower1 = name1.lower()
    nameLower2 = name2.lower()
    true_score = 0
    love_score = 0
    for i in range(1, len(name1)):
        if nameLower1[i] in ["t", "r", "u", "e"]:
            true_score += 1
        if nameLower1[i] in ["l", "o", "v", "e"]:
            love_score += 1

    for i in range(1, len(name2)):
        if nameLower2[i] in ["t", "r", "u", "e"]:
            true_score += 1
        if nameLower2[i] in ["l", "o", "v", "e"]:
            love_score += 1

    print(f"{true_score}{love_score}")


calculate_love_score(name1="Angela Yu", name2="Jack Bauer")
