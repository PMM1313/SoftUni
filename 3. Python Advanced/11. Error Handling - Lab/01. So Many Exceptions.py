try:
    num = (int(input()))
    num2 = (int(input()))
    print(num/num2)
except ValueError as error:
    print(f"Invalid input! : {str(error)}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
