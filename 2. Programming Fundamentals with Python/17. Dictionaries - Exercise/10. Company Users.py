# Initialize an empty dictionary to store company names and employee IDs
companies = {}

# Read input until "End" is encountered
while True:
    text = input().strip()
    if text == 'End':
        break

    # Split the line into company name and employee ID
    company, employee = text.split(' -> ')

    # If the company is not in the dictionary, add it with an empty list
    if company not in companies:
        companies[company] = []

    # Add the employee ID to the company's list of employee IDs if not already present
    if employee not in companies[company]:
        companies[company].append(employee)

# Print the results
for company_name, employee_ids in companies.items():
    print(company_name)
    for employee_id in employee_ids:
        print(f'-- {employee_id}')


