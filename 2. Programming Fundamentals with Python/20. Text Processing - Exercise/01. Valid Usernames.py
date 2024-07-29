import re


# Function to check if a username is valid
def is_valid_username(username):
    # Check the length of the username
    if not (3 <= len(username) <= 16):
        return False
    # Check if the username contains only valid characters (letters, numbers, hyphens, and underscores)
    if not re.match(r'^[\w-]+$', username):
        return False
    # Check if the username contains no redundant symbols (extra spaces, leading/trailing spaces are not allowed)
    if username != username.strip():
        return False
    return True


# Read the input usernames
input_usernames = input().split(', ')

# Filter and print valid usernames
for username in input_usernames:
    if is_valid_username(username):
        print(username)
