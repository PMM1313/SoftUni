
to_buy_safety_nylon = int(input())
to_buy_paint = int(input())
to_buy_thinner = int(input())
hours_to_do_the_job = int(input())

# Prices:
price_of_Nylon = 1.5
price_of_pain = 14.50
price_of_thinner = 5

# Rumen wants additional:
additional_nylon = 2
additional_paint = (to_buy_paint / 10)
additional_needed_bags = 0.40

# total needed
total_needed_paint = to_buy_paint + additional_paint
total_needed_nylon = to_buy_safety_nylon+additional_nylon
total_needed_thinner = to_buy_thinner

# total cost for stuff
total_cost_for_nylon = total_needed_nylon*price_of_Nylon
total_cost_for_paint = total_needed_paint*price_of_pain
total_cost_for_thinner = to_buy_thinner*price_of_thinner
total_cost_for_bags = additional_needed_bags
total_cost_for_all = total_cost_for_bags+total_cost_for_thinner+total_cost_for_paint+total_cost_for_nylon

# hour rate is 30% of all summ
hour_rate = 30
hour_rate_as_percentage = hour_rate/100
price_per_hour_in_sum = hour_rate_as_percentage*total_cost_for_all

# hourly billing:
cost_per_hour = hours_to_do_the_job*price_per_hour_in_sum

# total cost stuff and work
total_cost_stuff_and_work = total_cost_for_all + cost_per_hour

print(total_cost_stuff_and_work)
