def print_upper_part(n):
    for row in range(1, n+1):
        print(" "*(n-row), "* "*row)


def print_bottom_part(n):
    for row in range(1, n):
        print(" "*row, "* "*(n-row))

def print_rhombus(n):
    print_upper_part(n)
    print_bottom_part(n)
n = int(input())
print_rhombus(n)
