def operate(operator, *args):
    if not args:
        return "No numbers provided!"

    def sum_nums():
        return sum(args)

    def sub_nums():
        result = args[0]
        for el in args[1:]:
            result -= el
        return result

    def mul_nums():
        result = 1
        for el in args:
            result *= el
        return result

    def div_nums():
        result = args[0]
        for el in args[1:]:
            if el == 0:
                return
            result /= el
        return result

    if operator == "+":
        return sum_nums()
    elif operator == "-":
        return sub_nums()
    elif operator == "*":
        return mul_nums()
    elif operator == "/":
        return div_nums()
    else:
        return "Invalid operator!"