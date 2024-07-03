students = []

# Read input until the course name line
while True:
    line = input().strip()
    if ":" in line:
        # Process student information
        students.append(line)
    else:
        # This is the course name line
        course_name = line.replace("_", " ").lower()  # Remove underscores and convert to lowercase
        break

# Print the collected student information for the given course name
for student in students:
    name, id, course = student.split(":")
    course = course.strip().replace("_", " ").lower()  # Remove underscores and convert to lowercase for comparison
    if course == course_name:
        print(f"{name} - {id}")
