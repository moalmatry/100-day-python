class User:
    def __init__(self, id: str, username: str, password: str):
        self.id = id
        self.username = username
        self.password = password
        self.followers = 0
        self.following = 0

    def follow(self, user: "User"):
        user.followers += 1
        self.following += 1


user_1 = User("1", "mohamed", "123")
user_2 = User("2", "Ahmed", "313123")


user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)
