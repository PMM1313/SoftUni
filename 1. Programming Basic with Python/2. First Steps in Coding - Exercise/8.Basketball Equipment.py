

annual_fee = int(input())

# equipment:
shoes = 40      # 40% less than annual_fee
clothes = 20    # 20 % less than shoes
ball = clothes / 4
accessories = ball / 5

# calculating percentages:
shoes_as_percentage = (shoes / 100) * annual_fee
sum_for_shoes = annual_fee - shoes_as_percentage
clothes_as_percentage = (clothes / 100) * sum_for_shoes
sum_for_clothes = sum_for_shoes - clothes_as_percentage
sum_for_ball = sum_for_clothes / 4
sum_for_accessories = sum_for_ball / 5


# calculating prices + annual fee:
total_sum = sum_for_ball + sum_for_accessories + sum_for_clothes + sum_for_shoes
total_sum_with_fee = total_sum + annual_fee

print(total_sum_with_fee)
