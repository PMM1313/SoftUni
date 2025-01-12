n, m = map(int, input().split())

n_numbers = set()
m_numbers = set()
unique_in_both_sets = set()

for _ in range(n):
    number = int(input())
    n_numbers.add(number)

for _ in range(m):
    number = int(input())
    m_numbers.add(number)

# Find the intersection of the two sets
unique_in_both_sets = n_numbers & m_numbers  # Use set intersection

# Print the result, converting numbers to strings
print("\n".join(map(str, unique_in_both_sets)))