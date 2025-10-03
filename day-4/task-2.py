states_of_america = ["Delaware", "Pennsylvania"]

states_of_america[1] = "New York"
# states_of_america.append("New Jersey")
# states_of_america.append("New State")

states_of_america.extend(["New Jersey", "New State"])

print(states_of_america[1])
