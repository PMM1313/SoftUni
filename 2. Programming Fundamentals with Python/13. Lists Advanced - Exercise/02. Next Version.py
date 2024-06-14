def next_version(current_version):
    # Split the version string into three parts
    parts = current_version.split(".")

    # Convert the parts from string to integers
    n1 = int(parts[0])
    n2 = int(parts[1])
    n3 = int(parts[2])

    # Increment the last number
    n3 += 1

    # Handle overflow: if n3 exceeds 9, reset it and increment n2
    if n3 > 9:
        n3 = 0
        n2 += 1

    # Handle overflow: if n2 exceeds 9, reset it and increment n1
    if n2 > 9:
        n2 = 0
        n1 += 1

    # Format the new version string
    next_version = f"{n1}.{n2}.{n3}"

    # Print the next version
    print(next_version)

string = input()
next_version(string)