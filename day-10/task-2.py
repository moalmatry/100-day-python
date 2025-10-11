import art


def sum(number1, number2):
    return number1 + number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


def subtract(number1, number2):
    return number1 - number2


operations = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(number1, number2, operation):
    return operations[operation](number1, number2)


print(art.logo)


def calculator():
    end_app = True
    use_old_result = True
    while end_app:
        number1 = int(input("What is the first number? "))
        number2 = int(input("What is the second number? "))
        operation = input("What operation would you like to perform? ")
        calc_result = calculate(number1, number2, operation)
        print(calc_result)
        is_user_want_old_result = input(
            f"Do you want to use the old result {calc_result} ? Type 'yes' or 'no'.\n"
        )
        if is_user_want_old_result == "no":
            use_old_result = False
        while use_old_result:
            number1 = calc_result
            number2 = int(input("What is the second number? "))
            operation = input("What operation would you like to perform? ")
            calc_result = calculate(number1, number2, operation)
            print(calc_result)
            using_old_result = input(
                f"Do you want to use the old result {calc_result} ? Type 'yes' or 'no'.\n"
            )
            if using_old_result == "no":
                use_old_result = False

        restart = input(
            "Type 'yes' if you want to go again. Otherwise, type 'no'.\n"
        ).lower()
        if restart == "no":
            end_app = False


calculator()
