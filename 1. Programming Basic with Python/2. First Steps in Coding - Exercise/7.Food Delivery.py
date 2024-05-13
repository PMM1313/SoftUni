
# client wants
number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menu = int(input())

# prices
chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
desert = 20       # 20% of the check
delivery = 2.5    # added last

# calculating desert as percentage
desert_as_percentage = desert / 100

# calculating cost of order
cost_of_order_chicken_menu = number_of_chicken_menus * chicken_menu
cost_of_order_fish_menu = number_of_fish_menus * fish_menu
cost_of_order_vegetarian_menu = number_of_vegetarian_menu * vegetarian_menu
total_cost_for_menus = cost_of_order_chicken_menu + cost_of_order_fish_menu + cost_of_order_vegetarian_menu
cost_for_desert = total_cost_for_menus * desert_as_percentage

# total cost for all + delivery
total_cost_for_all = total_cost_for_menus + cost_for_desert + delivery

print(total_cost_for_all)
