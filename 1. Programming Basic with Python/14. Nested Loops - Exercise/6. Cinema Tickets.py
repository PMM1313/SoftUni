total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie_name = input()

    if movie_name == "Finish":
        break

    free_seats = int(input())
    sold_tickets = 0

    while True:
        ticket_type = input()

        if ticket_type == "End":
            break

        sold_tickets += 1
        total_tickets += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        if sold_tickets == free_seats:
            break

    percentage_full = (sold_tickets / free_seats) * 100
    print(f"{movie_name} - {percentage_full:.2f}% full.")

total_percentage_student = (student_tickets / total_tickets) * 100
total_percentage_standard = (standard_tickets / total_tickets) * 100
total_percentage_kid = (kid_tickets / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{total_percentage_student:.2f}% student tickets.")
print(f"{total_percentage_standard:.2f}% standard tickets.")
print(f"{total_percentage_kid:.2f}% kids tickets.")