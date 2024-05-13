def figure_out_things():
    one = input()
    two = input()
    return one, two


def do_clever_things(a, b):
    final_thing = a + b  # Some clever arithmetic!

    return final_thing


# Pass the values to the second function
def result():
    first_thing, second_thing = figure_out_things()
    result_value = do_clever_things(int(first_thing), int(second_thing))
    if result_value % 2 == 0:
        print('Hey its an even NUMBER !')
    else:
        print('LoL its not an even NUMBER')
    print(result_value)
    return result_value


result()
