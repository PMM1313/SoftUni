# Read the input strings
str1, str2 = input().split()

# Initialize the total sum
total_sum = 0

# Calculate the minimum length to loop through
min_length = min(len(str1), len(str2))

# Multiply character codes of corresponding characters and add to total sum
for i in range(min_length):
    total_sum += ord(str1[i]) * ord(str2[i])

# Add remaining characters from the longer string
if len(str1) > len(str2):
    for i in range(len(str2), len(str1)):
        total_sum += ord(str1[i])
elif len(str2) > len(str1):
    for i in range(len(str1), len(str2)):
        total_sum += ord(str2[i])

# Print the total sum
print(total_sum)
