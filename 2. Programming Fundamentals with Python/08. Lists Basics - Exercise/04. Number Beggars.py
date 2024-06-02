
offerings = list(map(int, input().split(", ")))
beggars_count = int(input())

beggars_sums = [0] * beggars_count

for i, offering in enumerate(offerings):
    beggars_sums[i % beggars_count] += offering

print(beggars_sums)
