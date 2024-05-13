kilometers = int(input())
day_or_night = str(input())

# type and cost of transport
taxi_start_fee = 0.70
taxi_day_fee = 0.79
taxi_night_fee = 0.90
bus_fee = 0.09
train_fee = 0.06
# cost of transport


if kilometers < 20:
    if day_or_night == 'day':
        taxi_cost_day = (kilometers * taxi_day_fee) + taxi_start_fee
        print(f'{taxi_cost_day:.2f}')
    elif day_or_night == 'night':
        taxi_cost_night = (kilometers * taxi_night_fee) + taxi_start_fee
        print(f'{taxi_cost_night:.2f}')

elif 20 <= kilometers < 100:
    if day_or_night == 'day':
        bus_cost = (kilometers * bus_fee)
        taxi_cost_day = (kilometers * taxi_day_fee) + taxi_start_fee
        print(f'{min(taxi_cost_day, bus_cost):.2f}')
    elif day_or_night == 'night':
        bus_cost = (kilometers * bus_fee)
        taxi_cost_night = (kilometers * taxi_night_fee) + taxi_start_fee
        print(f'{min(taxi_cost_night, bus_cost):.2f}')

elif 100 <= kilometers <= 5000:
    bus_cost = (kilometers * bus_fee)
    taxi_cost_day = (kilometers * taxi_day_fee) + taxi_start_fee
    taxi_cost_night = (kilometers * taxi_night_fee) + taxi_start_fee
    train_fee = kilometers * train_fee

    if day_or_night == 'day':
        print(f'{min(taxi_cost_day, bus_cost, train_fee):.2f}')
    elif day_or_night == 'night':
        print(f'{min(taxi_cost_night, bus_cost, train_fee):.2f}')
