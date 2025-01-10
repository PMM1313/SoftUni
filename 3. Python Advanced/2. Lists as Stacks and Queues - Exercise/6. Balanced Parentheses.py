
sequence = input()


stack = []

pairs = {')': '(', '}': '{', ']': '['}

balanced = True


for char in sequence:
    if char in "({[":
        stack.append(char)
    elif char in ")}]":
        if stack and stack[-1] == pairs[char]:
            stack.pop()
        else:
            balanced = False
            break

if stack:
    balanced = False

print("YES" if balanced else "NO")
