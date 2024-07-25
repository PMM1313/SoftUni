# Initialize dictionaries to keep track of the data
user_scores = {}
language_submissions = {}
banned_users = set()

while True:
    command = input().strip()
    if command == "exam finished":
        break

    if '-' in command:
        parts = command.split('-')
        if len(parts) == 3:
            username, language, points = parts
            points = int(points)
            if username in banned_users:
                # If user is banned, skip their submissions
                continue

            # Update language submission count
            if language not in language_submissions:
                language_submissions[language] = 0
            language_submissions[language] += 1

            # Update user scores
            if username not in user_scores:
                user_scores[username] = {}
            if language not in user_scores[username]:
                user_scores[username][language] = points
            else:
                user_scores[username][language] = max(user_scores[username][language], points)
        elif len(parts) == 2:
            username, _ = parts
            banned_users.add(username)

# Calculate final scores for each user
final_scores = {}
for user, languages in user_scores.items():
    if user not in banned_users:
        final_scores[user] = sum(languages.values())

# Print results
print("Results:")
for user, score in final_scores.items():
    print(f"{user} | {score}")

# Print language submissions count
print("Submissions:")
for language, count in language_submissions.items():
    print(f"{language} - {count}")
