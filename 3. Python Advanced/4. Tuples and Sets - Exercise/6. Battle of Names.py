N = int(input())

odd_set = set()
even_set = set()

for i in range(N):
    name = input()
    ascii_sum = sum(ord(char) for char in name)
    result = ascii_sum // (i + 1)  # Adjust index for 1-based indexing
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    result_set = odd_set.union(even_set)
elif odd_sum > even_sum:
    result_set = odd_set.difference(even_set)
else:
    result_set = odd_set.symmetric_difference(even_set)

print(", ".join(map(str, result_set)))



