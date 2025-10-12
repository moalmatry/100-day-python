game_level = 10
enimes = ["Skeleton", "Zombie", "Alien"]

# if game_level < 5:
#     new_enemy = enimes[0]


def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enimes[0]
    print(new_enemy)
