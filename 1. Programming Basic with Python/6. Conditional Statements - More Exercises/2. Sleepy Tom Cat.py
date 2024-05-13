
number_of_rest_days = int(input())

# play time
rest_days_play_time = 127
work_days_play_time = 63

# needed play rtime
norm = 30000

# working days
year_working_days = 365
working_days = year_working_days - number_of_rest_days

# calculating play time for year
work_days_play_time_yearly = (year_working_days - number_of_rest_days) * work_days_play_time
rest_days_play_time_yearly = number_of_rest_days * rest_days_play_time
total_play_time_yearly = work_days_play_time_yearly + rest_days_play_time_yearly


if total_play_time_yearly < norm:
    less_time_for_play_in_hours = (norm - total_play_time_yearly) // 60
    less_time_for_play_in_minutes = (norm - total_play_time_yearly) % 60
    print(f'Tom sleeps well')
    print(f'{less_time_for_play_in_hours} hours and {less_time_for_play_in_minutes} minutes less for play')
if total_play_time_yearly > norm:
    more_time_for_play = total_play_time_yearly - norm
    less_time_for_play_in_hours = (total_play_time_yearly - norm) // 60
    less_time_for_play_in_minutes = (total_play_time_yearly - norm) % 60
    print(f'Tom will run away')
    print(f'{less_time_for_play_in_hours} hours and {less_time_for_play_in_minutes} minutes more for play')
