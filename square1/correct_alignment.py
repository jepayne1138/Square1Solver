"""Defines a dictionary that given two wedges stores the distance between them
in number of 30d slices (which we measure by counting the number of sides of
the wedges inbetween the wedges in a clockwise direction facing the top or
bottom face (always right).

The wedges follow the cube_definition naming convention. (Join with
cube_definition module?)  The naming lists the sides in alphabetical order
(i.e. back_left, front_right, right, front, etc).
"""

import itertools


def icircle(iterable, start=0):
    return itertools.islice(
        itertools.cycle(iterable),
        start, start+len(iterable)
    )


def build_side_map_dict(side_map):
    return_dict = {}
    for index, (curr_side, _) in enumerate(side_map):
        running_sum = 0
        curr_side_dict = {}
        for name, sides in icircle(side_map, index):
            running_sum += sides
            curr_side_dict[name] = running_sum
        return_dict[curr_side] = curr_side_dict
    return return_dict


top_side_map = [
    ('front', 1),
    ('front_left', 2),
    ('left', 1),
    ('back_left', 2),
    ('back', 1),
    ('back_right', 2),
    ('right', 1),
    ('front_right', 2),
]
bottom_side_map = top_side_map[:1] + list(reversed(top_side_map[1:]))


distance = {
    'top': build_side_map_dict(top_side_map),
    'bottom': build_side_map_dict(bottom_side_map),
}
