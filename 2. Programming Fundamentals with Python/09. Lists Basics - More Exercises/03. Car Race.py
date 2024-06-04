# Get the input from the user
times = list(map(int, input().split()))

# Calculate the middle index
middle_index = len(times) // 2

# Split the times into two parts
left_times = times[:middle_index]
right_times = times[middle_index+1:][::-1]

# Calculate total time for the left racer
left_total_time = 0
for time in left_times:
    left_total_time += time
    if time == 0:
        left_total_time *= 0.8

# Calculate total time for the right racer
right_total_time = 0
for time in right_times:
    right_total_time += time
    if time == 0:
        right_total_time *= 0.8

# Determine the winner
if left_total_time < right_total_time:
    winner = "left"
    total_time = left_total_time
else:
    winner = "right"
    total_time = right_total_time

# Print the result
print(f"The winner is {winner} with total time: {total_time:.1f}")
