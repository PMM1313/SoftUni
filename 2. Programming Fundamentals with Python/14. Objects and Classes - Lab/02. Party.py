class Party:
    def __init__(self):
        self.people = []

# Create an instance of the Party class
party = Party()

# Collect names of people until "End" is received
while True:
    name = input()
    if name == "End":
        break
    party.people.append(name)

# Print the required output
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")