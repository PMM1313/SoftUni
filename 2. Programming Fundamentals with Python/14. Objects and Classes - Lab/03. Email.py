class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender}, says to {self.receiver},: {self.content}. Sent: {self.is_sent}"


# List to store email objects
emails = []

# Read input until "Stop" is received
while True:
    data = input()
    if data == "Stop":
        break
    sender, receiver, content = data.split(", ")
    emails.append(Email(sender, receiver, content))

# Read the indices of emails to send
indices = input().split(", ")
indices = [int(index) for index in indices]

# Send the emails at the given indices
for index in indices:
    emails[index].send()

# Print information about all emails
for email in emails:
    print(email.get_info())