capitals = {"France": "Paris", "Germany": "Berlin", "Italy": "Rome"}

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }


# print(travel_log["France"][0])
nested_lits = ["a", "b", ["c", "d"]]

# print(nested_lits[2][1])


travel_log = {
    "France": {"total_visits": 12, "cities_visited": ["Paris", "Lille", "Dijon"]},
    "Germany": {
        "total_visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    },
}

print(travel_log["Germany"]["cities_visited"][2])
