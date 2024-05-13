
hours = int(input())
minutes = int(input())

add_15_minutes = 15

if 0 <= minutes + add_15_minutes < 60:
    updated_hours = hours
    updated_minutes = minutes + add_15_minutes
else:
    updated_hours = (hours + 1) % 24
    updated_minutes = (minutes + add_15_minutes) % 60

print(f'{updated_hours}:{updated_minutes:02d}')


