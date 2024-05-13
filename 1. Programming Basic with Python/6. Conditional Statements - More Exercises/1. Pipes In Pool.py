
v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

# total debit for the pipes
p1_debit = p1 * h
p2_debit = p2 * h

# all pipes
all_pipes = p1_debit + p2_debit
if all_pipes <= v:
    # find percentage of v:
    v_percentage = (all_pipes / v) * 100
    # find percentage of p1 and p:
    p1_percentage = (p1_debit/ all_pipes) * 100
    p2_percentage = (p2_debit / all_pipes) * 100
    print(f'The pool is {v_percentage:.2f}% full. Pipe 1: {p1_percentage:.2f}%. Pipe 2: {p2_percentage:.2f}%.')

else:
    extra_liters = all_pipes - v
    print(f'For {h} hours the pool overflows with {extra_liters:.2f} liters.')
