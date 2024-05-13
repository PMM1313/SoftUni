import math

name_of_show = str(input())
duration_os_episode = int(input())
duration_of_break = int(input())

# needed time
lunch = duration_of_break / 8
rest = duration_of_break / 4

# calculation of needed time
total_free_time = duration_of_break - lunch - rest

if total_free_time >= duration_os_episode:
    free_time_left = total_free_time - duration_os_episode
    print(f'You have enough time to watch {name_of_show} and left with {math.ceil(free_time_left)} minutes free time.')
else:
    needed_time = duration_os_episode - total_free_time
    print(f"You don't have enough time to watch {name_of_show}, you need {math.ceil(needed_time)} more minutes.")
