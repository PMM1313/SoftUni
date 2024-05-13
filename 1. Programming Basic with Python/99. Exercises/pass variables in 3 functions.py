def figure_out_things():
    one = 1
    two = 2
    return one, two


def do_clever_things(a, b):
    final_thing = a + b  # Some clever arithmetic!

    return final_thing


# Call the first function to get the values
first_thing, second_thing = figure_out_things()

# Pass the values to the second function
result = do_clever_things(first_thing, second_thing)

print(result)
