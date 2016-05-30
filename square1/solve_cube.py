"""Module contains the code that will attempt to solve the cube

The plan is given an input, repeatedly calculate the evaluation function value
for each combination of possible two flips. In this way we know the middle row
will stay oriented properly. I believe this means we need to maximize the
evaluation function for up to 4096 possible combinations. This would get
prohibitively expensive very quickly to continuously check all branches of all
calculated possibilities. Therefore my first idea is only take the largest
only, but I don't know we can assume an always constantly increasing
evaluation function will solve the cube, so I'm actually going to try a
stochastic maximizing algorithm with the evaluation values weighting the
choice of move to try.  In this way all moves have a possibility of being
chosen, but increasing accurate choices are most likely.
"""
import copy
import cube_definition as cube_def
import eval_function as eval_func


def wedge_possibilities(cube):
    cube_copy = copy.copy(cube)
    for top_wedge in cube.wedges[cube_def.TOP]:
        for bottom_wedge in cube.wedges[cube_def.BOTTOM]:
            cube_copy.flip(top_wedge, bottom_wedge)
            yield (cube_copy, top_wedge, bottom_wedge)
    return

def solve_step(cube):
    """Returns a new cube and the step that was selected to get there"""
    possibilites = {}
    # Iterate through all possible flips from current state
    for cube1, top1, bottom1 in wedge_possibilities(cube):
        for cube2, top2, bottom2 in wedge_possibilities(cube1):
            eval_value = eval_func.evaluate1(cube2)
            if eval_value not in possibilites:
                possibilites[eval_value] = []
            possibilites[eval_value].append(
                (top1, bottom1, top2, bottom2)
            )

    # Select one of the possibilities
    sel_top1, sel_bottom1, sel_top2, sel_bottom2 = # Something here
    cube.flip(sel_top1, sel_bottom1)
    cube.flip(sel_top2, sel_bottom2)
    return (cube, sel_top1, sel_bottom2, sel_top2, sel_bottom2)
