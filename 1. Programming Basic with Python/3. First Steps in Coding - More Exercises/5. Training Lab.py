

length = float(input())
width = float(input())

# not usable space:
corridor = 100         # in cm.
door_and_desk = 3      # they take room for 3 working desk

# working desk size:
working_desk_width = 70
working_desk_length = 120

# converting to centimeters:
length_in_centimeters = length*100
width_in_centimeters = width*100

# calculating usable space:
usable_space_in_width = width_in_centimeters - corridor
working_desk_in_width = usable_space_in_width//working_desk_width
working_desk_in_length = length_in_centimeters//working_desk_length

# working desks in length + width - not usable space:
all_working_desk_in_the_room = working_desk_in_width * working_desk_in_length - door_and_desk

print(all_working_desk_in_the_room)
