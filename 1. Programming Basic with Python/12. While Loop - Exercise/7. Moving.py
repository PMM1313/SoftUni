cubic_m_h = int(input())
cubic_m_w = int(input())
cubic_m_l = int(input())

total_space = cubic_m_l * cubic_m_h * cubic_m_w
crates = 0

while total_space > 0 and crates != "Done":
    crates = input()

    if crates != 'Done':
        total_space -= int(crates)

if total_space <= 0:
    print(f'No more free space! You need {-total_space} Cubic meters more.')
else:
    print(f'{total_space} Cubic meters left.')

