import os



try:
    os.remove("my_first_file.txt")

except OSError:
    print(f"Error: Could not delete file.")