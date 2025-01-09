from collections import deque

quantity_of_food = int(input())
orders = deque(map(int, input().split()))

biggest_order = max(orders)

print(biggest_order)


while orders:
    next_order = orders[0]

    if next_order <= quantity_of_food:
        quantity_of_food -= next_order
        orders.popleft()

    else:
        print(f'Orders left: {" ".join(map(str, orders))}')
        break  # Exit the loop since no more orders can be processed

if not orders:
    print(f'Orders complete')
