centuries = int(input())

years_rate = centuries * 100
days_rate = int(years_rate * 365.2422)
hours_rate = days_rate * 24
minutes_rate = hours_rate * 60

print(f'{centuries} centuries = {years_rate} years = {days_rate} days = {hours_rate} hours = {minutes_rate} minutes')