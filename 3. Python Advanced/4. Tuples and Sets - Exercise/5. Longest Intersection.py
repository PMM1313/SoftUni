


N = int(input())

longest_intersection = []
length_longest_intersection = 0

for _ in range(N):

    range_input = input().split('-')

    first_start, first_end = map(int, range_input[0].split(','))
    second_start, second_end = map(int, range_input[1].split(','))

    start_intersection = max(first_start, second_start)
    end_intersection = min(first_end, second_end)

    if start_intersection <= end_intersection:
        intersection = list(range(start_intersection, end_intersection + 1))

        if len(intersection) > length_longest_intersection:
            longest_intersection = intersection
            length_longest_intersection = len(intersection)

print(f"Longest intersection is {longest_intersection} with length {length_longest_intersection}")
