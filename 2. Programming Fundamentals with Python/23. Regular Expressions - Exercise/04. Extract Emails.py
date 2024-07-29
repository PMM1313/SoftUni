import re


def extract_emails(input_string):
    # Regular expression pattern for a valid email address
    email_pattern = r"\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"

    # Find all matches in the input string
    matches = re.findall(email_pattern, input_string)

    # Print each email address on a new line
    for email in matches:
        print(email[0])


# Example usage
input_string = input()
extract_emails(input_string)
