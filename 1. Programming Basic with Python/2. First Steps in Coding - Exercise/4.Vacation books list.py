
number_of_pages_in_the_book = int(input())
number_of_pages_i_can_read = int(input())
number_of_days_to_read_the_book = int(input())

time_to_read_the_book = number_of_pages_in_the_book/number_of_pages_i_can_read
hours_per_day_to_read_the_book = time_to_read_the_book/number_of_days_to_read_the_book

print(int(hours_per_day_to_read_the_book))
