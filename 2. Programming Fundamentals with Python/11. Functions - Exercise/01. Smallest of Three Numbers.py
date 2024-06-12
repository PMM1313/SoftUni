def find_smallest_of_three(a: int, b: int, c: int) -> int:

    if a <= b and a <= c:
        print(a)
    elif b <= a and b <= c:
        print(b)
    else:
        print(c)

a = int(input())
b = int(input())
c = int(input())

find_smallest_of_three(a, b, c)