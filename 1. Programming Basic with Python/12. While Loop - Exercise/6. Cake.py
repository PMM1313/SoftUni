
cake_width = int(input())
cake_high = int(input())

total_pieces = cake_width * cake_high
cakes_taken = 0

while total_pieces > 0 and cakes_taken != "STOP":
    cakes_taken = input()
    if total_pieces > 0 and cakes_taken != 'STOP':
        total_pieces -= int(cakes_taken)
    elif cakes_taken == 'STOP':
        print(f'{total_pieces} pieces are left.')

if total_pieces <= 0:
    print(f'No more cake left! You need {abs(total_pieces)} pieces more.')









