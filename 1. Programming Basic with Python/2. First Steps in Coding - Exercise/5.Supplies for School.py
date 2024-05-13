
to_buy_number_of_pens = int(input())
to_buy_number_of_markers = int(input())
to_buy_cleaner = int(input())
discount = int(input())

discount_as_percentage = discount/100

price_of_packet_of_pens = 5.8
price_of_packet_of_markers = 7.2
price_of_cleaner = 1.2

price_for_all_pens = to_buy_number_of_pens*price_of_packet_of_pens
price_for_all_markers = to_buy_number_of_markers*price_of_packet_of_markers
price_for_all_cleaning = to_buy_cleaner*price_of_cleaner
price_for_all_the_stuff = price_for_all_markers+price_for_all_pens+price_for_all_cleaning
calculated_discount = price_for_all_the_stuff*discount_as_percentage
final_price_with_discount = price_for_all_the_stuff-calculated_discount

print(final_price_with_discount)
