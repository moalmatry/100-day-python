import art


bid_dict = {}


def ask_for_info():
    return input("What is your name? ").lower()


def ask_for_bid_price():
    return int(input("What is your bid? $"))


def print_logo():
    print(art.logo)


def add_bid(name, bid):
    bid_dict[name] = bid


def get_the_winner():
    highest_bid = 0
    for key in bid_dict:
        if bid_dict[key] > highest_bid:
            highest_bid = bid_dict[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")


def bid_system():
    isBid = "True"
    while isBid == "True":
        print_logo()
        name = ask_for_info()
        price = ask_for_bid_price()
        bid_dict[name] = price
        is_more_users = input(
            "Are there any other bidders? Type 'yes' or 'no'.\n"
        ).lower()
        if is_more_users == "no":
            isBid = "False"
        get_the_winner()


bid_system()
