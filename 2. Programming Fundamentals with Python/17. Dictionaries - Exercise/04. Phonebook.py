phonebook = {}

while True:
    entry = input()
    if entry.isdigit():
        N = int(entry)
        break
    name, number = entry.split('-')
    phonebook[name] = number

for _ in range(N):
    query_name = input()
    if query_name in phonebook:
        print(f"{query_name} -> {phonebook[query_name]}")
    else:
        print(f"Contact {query_name} does not exist.")