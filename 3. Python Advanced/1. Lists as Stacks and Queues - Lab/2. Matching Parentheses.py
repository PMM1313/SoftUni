text = input()
stack = []

for index in range(len(text)):

    if text[index] == '(':

        stack.append(index)

    elif text[index] == ')':

        start_index = stack.pop()
        end_index = index + 1
        print(text[start_index:end_index])