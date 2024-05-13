
number_of_days = int(input())
type_of_room = str(input())
assessment = str(input())

overnight_stays = number_of_days - 1

# prices:
room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00

# assessment after stay as percentage, now 100%:
positive_or_negative = 1

total_sum = 0

# calculating discount:

if overnight_stays < 10:
    apartment *= 0.70
    president_apartment *= 0.90
elif 10 <= overnight_stays <= 15:
    apartment *= 0.65
    president_apartment *= 0.85
elif overnight_stays > 15:
    apartment *= 0.50
    president_apartment *= 0.80

if type_of_room == 'room for one person':
    total_sum = room_for_one_person * overnight_stays
elif type_of_room == 'apartment':
    total_sum = apartment * overnight_stays
elif type_of_room == 'president apartment':
    total_sum = president_apartment * overnight_stays

if assessment == 'positive':
    total_sum *= 1.25
elif assessment == "negative":
    total_sum *= 0.90

print(f'{total_sum:.2f}')
