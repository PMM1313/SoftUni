try:
    file = open("examplee.txt")
except FileNotFoundError:
    print("Not found")
finally:
    print("exiting .....")