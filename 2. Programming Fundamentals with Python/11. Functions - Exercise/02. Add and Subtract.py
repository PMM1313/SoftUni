def add_and_subtract(a: int, b: int, c: int):

    def sum_numbers(a: int, b: int) -> int:

        return a + b

    def subtract(sum_result: int, c: int) -> int:

        return sum_result - c

    sum_result = sum_numbers(a, b)
    result = subtract(sum_result, c)
    print(result)


a = int(input())
b = int(input())
c = int(input())

add_and_subtract(a, b, c)

