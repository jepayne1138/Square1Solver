"""Defines the evaluation function for approaching a solution

Current plan for first naive evaluation function will assume the middle row is
always correct (meaning it must start correct and only be evaluating after an
even number of flips). The evaluation function will return the number of
correctly oriented wedges. Wedges will only be counted if they are on the
correct side. We look at each wedge and check the number of wedges that are
in the correct position relative to that wedge. We do that for all wedges
not yet checked, and return the sum of the maximum number of relatively
correct wedges on each side.
"""
import itertools
import cube_definition as cube_def
import correct_alignment as ca


def get_face_max_rel_correct(face, cube):
    """Returns maximum number of relatively correct wedges for one face

    Args:
      face (str): Name of the face to get the best relatively correct for
      cube (cube_definition.Cube): The cube we are solving
    """
    rel_correct_list = []
    for index, start_wedge in enumerate(cube.wedges[face]):
        rel_correct = 0
        running_sum = 0  # Sum of number of sides
        for wedge in ca.icircle(cube.wedges[face], index):
            running_sum += len(wedge.color_sides)
            if ca.distance[face][start_wedge.name][wedge.name] == running_sum:
                rel_correct += 1
        rel_correct_list.append(rel_correct)
    return max(rel_correct_list)


def evaluate1(cube):
    """Returns maximum number of relatively correct wedges on top and bottom

    Args:
      cube (cube_definition.Cube): The cube we are solving
    """
    return (
        get_face_max_rel_correct(cube_def.TOP, cube) +
        get_face_max_rel_correct(cube_def.BOTTOM, cube)
    )
