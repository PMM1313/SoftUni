
month = str(input())
number_of_days = int(input())

price_of_studio = 0
price_of_apartment = 0

# discount as percentage 1 == 100% before calculation:
studio_discount = 1
apartment_discount = 1

# choosing month
if month == 'May' or month == 'October':
    price_of_studio = 50.00
    price_of_apartment = 65.00
elif month == 'June' or month == 'September':
    price_of_studio = 75.20
    price_of_apartment = 68.70
elif month == 'July' or month == 'August':
    price_of_studio = 76.00
    price_of_apartment = 77.00

# calculating discount:
if 7 < number_of_days < 14 and (month == 'May' or month == 'October'):
    studio_discount = 0.95
elif number_of_days > 14 and (month == 'May' or month == 'October'):
    studio_discount = 0.70
elif number_of_days > 14 and (month == 'June' or month == 'September'):
    studio_discount = 0.80

if number_of_days > 14:
    apartment_discount = 0.90


full_price_apartment = (price_of_apartment * apartment_discount) * number_of_days
full_price_studio = (price_of_studio * studio_discount) * number_of_days

print(f'Apartment: {full_price_apartment:.2f} lv.')
print(f'Studio: {full_price_studio:.2f} lv.')

