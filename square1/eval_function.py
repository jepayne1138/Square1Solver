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

sides = {
    'left': 0,
    'back': 1,
    'right': 2,
    'front': 3,
}


def icircle(iterable, start=0):
    return itertools.islice(
        itertools.cycle(iterable, start, start+len(iterable))
    )

def evaluate1(self, cube):
    """Returns maximum number of relatively correct wedges

    Args:
      cube (cube_definition.Cube): The cube we are solving
    """
    pass
    # top_color = cube.faces[cube_def.TOP]
    # bottom_color = cube.faces[cube_def.BOTTOM]

    # # Number correct starting at each wedge
    # rel_correct_top = []
    # visited = []
    # for wedge in cube.wedges[cube_def.TOP]:
    #     if wedge.color_face !````= cube.faces[cube_def.TOP]:
    #         visited.append(wedge)
    #     if wedge in visited:
    #         continue

    #     # Wedge not visited and proper color
    #     rel_correct = 1
    #     wedge_iter = icircle(
    #         cube.wedges[cube_def.TOP], cube.wedges[cube_def.TOP].index(wedge)
    #     )
    #     side_sum = 0
    #     for cur_wedge in wedge_iter:
    #         if cur_wedge in visited:
    #             continue
    #         if cur_wedge.color_face != cube.faces[cube_def.TOP]:
    #             visited.append(cur_wedge)


