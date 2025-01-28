import re


with open("words.txt") as file:
    words = file.read().split()

with open("input.txt") as file:
    content = file.read()

occ = {}
for word in words:
    pattern = re.compile(rf"\b{word}\b", flags=re.IGNORECASE)  # Compile with flags
    founded = pattern.findall(content)  # Use the compiled pattern to find matches
    occ[word] = len(founded)

sorted_occ = sorted(occ.items(), key=lambda kvp: -kvp[-1])

with open("output.txt", "w") as file:
    for key, value in sorted_occ:
        file.write(f"{key} - {value}\n")



