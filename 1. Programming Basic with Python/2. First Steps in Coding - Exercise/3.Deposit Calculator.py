
sum_to_deposit = float(input())
term_of_deposit = int(input())
interest = float(input())

interest_as_percent = interest/100
all_interest = sum_to_deposit * interest_as_percent
interest_for_one_month = all_interest / 12
deposit_and_interest = sum_to_deposit+(term_of_deposit*interest_for_one_month)

print(deposit_and_interest)
