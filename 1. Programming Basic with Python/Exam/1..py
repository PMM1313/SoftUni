
price_processor = float(input())
price_video_card = float(input())
price_ram = float(input())
number_of_ram = int(input())
percentage_discount = float(input())

USD_to_BGN_rate = 1.57

# percentage as NUMBER
discount = percentage_discount / 100

# needed ram
ram_needed = price_ram * number_of_ram

# conversion to bgn
processor_bgn = price_processor * USD_to_BGN_rate
video_card_bgn = price_video_card * USD_to_BGN_rate
ram_needed_bgn = ram_needed * USD_to_BGN_rate

# discount for processor and video card
processor_discount = processor_bgn * percentage_discount
processor_discounted_bgn = processor_bgn - processor_discount
video_card_discount = video_card_bgn * percentage_discount
video_card_discounted_bgn = video_card_bgn - video_card_discount

# total cost
total_sum = processor_discounted_bgn + video_card_discounted_bgn + ram_needed_bgn

print(f"Money needed - {total_sum:.2f} leva.")
