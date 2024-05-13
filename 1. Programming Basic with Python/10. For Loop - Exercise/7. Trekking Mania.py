
group_count = int(input())
musala_count = 0
montblanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for _ in range(group_count):
    group_size = int(input())

    if group_size <= 5:
        musala_count += group_size
    elif 6 <= group_size <= 12:
        montblanc_count += group_size
    elif 13 <= group_size <= 25:
        kilimanjaro_count += group_size
    elif 26 <= group_size <= 40:
        k2_count += group_size
    else:
        everest_count += group_size

total_people = musala_count + montblanc_count + kilimanjaro_count + k2_count + everest_count

musala_percentage = musala_count / total_people * 100
montblanc_percentage = montblanc_count / total_people * 100
kilimanjaro_percentage = kilimanjaro_count / total_people * 100
k2_percentage = k2_count / total_people * 100
everest_percentage = everest_count / total_people * 100

print(f"{musala_percentage:.2f}%")
print(f"{montblanc_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
