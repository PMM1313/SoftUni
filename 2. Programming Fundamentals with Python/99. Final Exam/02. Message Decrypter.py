import re


def decrypt_message(message):
    # Extract numbers from the message
    numbers = re.findall(r'\[(\d+)\]', message)

    # Convert numbers to ASCII characters and concatenate
    decrypted_message = ''.join(chr(int(num)) for num in numbers)

    return decrypted_message


def is_valid_message(message):
    # Regular expression to match the entire message format
    pattern = r'^([%$])([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'

    match = re.match(pattern, message)
    if match:
        tag = match.group(2)
        return tag
    else:
        return None


def process_messages(num_messages, messages):
    results = []

    for message in messages:
        tag = is_valid_message(message)
        if tag:
            decrypted_message = decrypt_message(message)
            results.append(f"{tag}: {decrypted_message}")
        else:
            results.append("Valid message not found!")

    return results


def main():
    # Read number of messages
    num_messages = int(input().strip())

    # Read all messages
    messages = []
    for _ in range(num_messages):
        messages.append(input().strip())

    # Process messages
    results = process_messages(num_messages, messages)

    # Print results
    for result in results:
        print(result)


if __name__ == "__main__":
    main()


