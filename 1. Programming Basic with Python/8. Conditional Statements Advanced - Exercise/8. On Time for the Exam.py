exam_hour = int(input())
exam_min = int(input())
hour_arrived = int(input())
min_arrived = int(input())

# calculating in minutes:
exam_hour_in_minutes = exam_hour * 60
hour_arrived_in_minutes = hour_arrived * 60

# total in minutes:
exam_in_minutes = exam_hour_in_minutes + exam_min
arrived_in_minutes = hour_arrived_in_minutes + min_arrived
min_early = exam_in_minutes - arrived_in_minutes
min_late = arrived_in_minutes - exam_in_minutes

if 0 <= min_early <= 30:
    if arrived_in_minutes == exam_in_minutes:
        print(f'On time')
    elif arrived_in_minutes != exam_in_minutes:
        print(f'On time')
        print(f'{min_early} minutes before the start')

elif 30 < min_early <= 59:
    print(f'Early')
    print(f'{min_early} minutes before the start')

elif min_early >= 60:
    min_early_in_hours = min_early // 60
    min_early_in_minutes = min_early % 60
    minutes_str = str(min_early_in_minutes).zfill(2)
    print(f'Early')
    print(f'{min_early_in_hours}:{minutes_str} hours before the start')

elif min_late <= 59:
    print(f'Late')
    print(f'{min_late} minutes after the start')

elif min_late >= 60:
    min_late_in_hours = min_late // 60
    min_late_in_minutes = min_late % 60
    minutes_str = str(min_late_in_minutes).zfill(2)
    print(f'Late')
    print(f'{min_late_in_hours}:{minutes_str} hours after the start')
