number_of_models = int(input())

total_sales = 0
total_rating = 0

for i in range(number_of_models):
    number = int(input())

    rating = number % 10
    # print (rating)
    sales = number // 10
    # print (sales)

    # sales
    if rating == 2:
        real_sales = 0
    elif rating == 3:
        real_sales = sales * 0.5
    elif rating == 4:
        real_sales = sales * 0.7
    elif rating == 5:
        real_sales = sales * 0.85
    else:
        real_sales = sales

    # total sales
    total_sales += real_sales

    # total reiting
    total_rating += rating

# avarage raiting
average_rating = total_rating / number_of_models

print(f"{total_sales:.2f}")
print(f"{average_rating:.2f}")
