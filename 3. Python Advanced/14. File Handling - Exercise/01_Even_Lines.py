symbols = {"-", ",", ".", "!", "?"}

with open("text.txt") as f:
    for row, line in enumerate(f.readlines()):
        if row % 2 == 0:
            for ch in symbols:
                line = line.replace(ch, "@")

            print(" ".join(reversed(line.split())))



