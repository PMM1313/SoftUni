from string import punctuation

with open("text2.txt", "r") as f, open("output.txt", "w") as output_file:
    result = []
    for row, line in enumerate(f):
        letters_count = 0
        punctuation_count = 0
        for ch in line:
            if ch.isalpha():
                letters_count += 1
            elif ch in punctuation:
                punctuation_count += 1

        result.append(f"Line {row+1}: {line.strip()} ({letters_count})({punctuation_count})")

    output_file.write("\n".join(result))
