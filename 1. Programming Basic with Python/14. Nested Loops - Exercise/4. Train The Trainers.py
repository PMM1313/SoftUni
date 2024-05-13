n = int(input())
total_score, presentations_count = 0, 0

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    average_score = sum(float(input()) for _ in range(n)) / n
    total_score += average_score
    presentations_count += 1

    print(f"{presentation_name} - {average_score:.2f}.")

if presentations_count > 0:
    final_average = total_score / presentations_count
    print(f"Student's final assessment is {final_average:.2f}.")