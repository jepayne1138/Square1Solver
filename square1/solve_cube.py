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
import time
import math
import random
from pprint import pprint
import bisect
import cube_definition as cube_def
import eval_function as eval_func

MAX_TARGET = 0.95
MIN_TARGET = 1 - MAX_TARGET
WEIGHT_MULTIPLIER = 100

class TimeoutException(Exception):
    pass


def _a(c1, c2):
    return math.log(MAX_TARGET / MIN_TARGET) / (c1 - c2)


def _b(c1, c2):
    return (c2 * math.log(MAX_TARGET) - c1 * math.log(MIN_TARGET)) / (c2 - c1)


def exponential_function(c1, c2):
    """Returns an exponential function returns .95 for c1 and .05 for c2
    Returns function in form of f(x) = e^(a*x+b)
    """
    return lambda x: WEIGHT_MULTIPLIER * math.exp(_a(c1, c2) * x + _b(c1, c2))


def wedge_possibilities(cube):
    # pprint(cube.wedges['top'])
    for top_wedge in cube.wedges[cube_def.TOP]:
        for bottom_wedge in cube.wedges[cube_def.BOTTOM]:
            cube_copy = copy.deepcopy(cube)
            cube_copy.flip(top_wedge, bottom_wedge)
            yield (cube_copy, top_wedge, bottom_wedge)
    return


def weighted_choice(weights, choices):
    total = 0
    cumulative_weights = []
    for weight in weights:
        total += weight
        cumulative_weights.append(total)
    rand_value = random.random() * total
    selected_index = bisect.bisect(cumulative_weights, rand_value)
    return choices[selected_index]


def solve_step(cube):
    """Returns a new cube and the step that was selected to get there"""
    possibilites = {}
    # pprint(cube.wedges['top'])
    # Iterate through all possible flips from current state
    for cube1, top1, bottom1 in wedge_possibilities(cube):
        cube_copy = copy.deepcopy(cube)
        try:
            cube_copy.flip(top1, bottom1)
            assert cube_copy == cube1
        except AssertionError:
            print 'cube1'
            print cube1
            print 'cube_copy'
            print cube_copy
            raise

        assert id(cube) != id(cube1)
        for cube2, top2, bottom2 in wedge_possibilities(cube1):
            assert id(cube1) != id(cube2)
            assert cube != cube2
            eval_value = eval_func.evaluate1(cube2)
            if eval_value == eval_func.EVAL_TARGET:
                # If goal state, immediately return solution
                # We don't care about returned cube as we don't need it again
                return (None, top1, bottom1, top2, bottom2, True)
            if eval_value not in possibilites:
                possibilites[eval_value] = []
            possibilites[eval_value].append(
                (top1, bottom1, top2, bottom2)
            )

    # pprint(cube.wedges['top'])
    # Select one of the possibilites
    exp_func = exponential_function(
        max(possibilites.keys()),
        min(possibilites.keys()),
    )
    print 'Number of possibilites = {}'.format(sum(map(len, possibilites.values())))
    print 'Max = {} : Min = {}'.format(
        max(possibilites.keys()),
        min(possibilites.keys()),
    )
    # weights = []
    # choices = []
    # for weight in possibilites.keys():
    #     for choice in possibilites[weight]:
    #         weights.append(weight)
    #         choices.append(choice)
    # sel_top1, sel_bottom1, sel_top2, sel_bottom2 = weighted_choice(
    #     weights, choices
    # )
    sel_top1, sel_bottom1, sel_top2, sel_bottom2 = random.choice(
        possibilites[max(possibilites.keys())]
    )
    cube.flip(sel_top1, sel_bottom1)
    cube.flip(sel_top2, sel_bottom2)
    assert eval_func.evaluate1(cube) == max(possibilites.keys())
    return (cube, sel_top1, sel_bottom2, sel_top2, sel_bottom2, False)


def solve(cube, timeout=None):
    steps = []
    cur_cube = cube
    if timeout is not None:
        start_time = time.time()
    step_number = 0
    while True:
        step_number +=1
        cur_cube, top1, bottom1, top2, bottom2, solved = solve_step(cur_cube)
        steps.append(
            (top1, bottom1, top2, bottom2)
        )
        print 'Step {: <3} = {}'.format(
            step_number, eval_func.evaluate1(cur_cube)
        )
        if solved:
            return steps
        if timeout is not None:
            if (time.time() - start_time) > timeout:
                raise TimeoutException()
