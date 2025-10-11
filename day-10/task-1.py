# def format_name(f_name, l_name):
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f"{f_name} {l_name}"


# print(
#     format_name(input("What is your first name? "), input("What is your last name? "))
# )


# def function_1(text):
#     return text + text


# def function_2(text):
#     return text.title()


# output = function_1("hello")
# output = function_2(output)
# print(output)


def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"


format_name(input("What is your first name? "), input("What is your last name? "))
