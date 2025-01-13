from math import floor

# Input expression
expression = input().split()

# Initialize stack
stack = []

# Loop through each token
for token in expression:
    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):  # Check if token is a number
        stack.append(int(token))
    else:
        # Operator encountered; evaluate stack
        while len(stack) > 1:
            num1 = stack.pop(0)  # Take the first number
            num2 = stack.pop(0)  # Take the second number

            if token == "+":
                result = num1 + num2
            elif token == "-":
                result = num1 - num2
            elif token == "*":
                result = num1 * num2
            elif token == "/":
                result = floor(num1 / num2)  # Integer division rounding down

            stack.insert(0, result)  # Push the result back to the front of the stack

print(stack[0])  # Final result