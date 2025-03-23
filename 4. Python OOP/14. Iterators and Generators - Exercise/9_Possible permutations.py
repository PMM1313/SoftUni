# def possible_permutations(list_data):
#     if len(list_data) <= 1:
#         yield list_data
#
#     else:
#         for i in range(len(list_data)):
#             cur_el = list_data[i]
#             remaining_elements = list_data[:i] + list_data[i + 1:]
#             permutations = possible_permutations(remaining_elements)
#
#             for permutation in permutations:
#                 yield [cur_el, *permutation]
from itertools import permutations

def possible_permutations(ls):
    for perm in permutations(ls):
        yield list(perm)