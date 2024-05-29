
a = int(input())
b = int(input())

old_a = a
old_b = b

a = b
b = old_a

print(f'Before:\na = {old_a}\nb = {old_b}\nAfter:\na = {a}\nb = {b}')
