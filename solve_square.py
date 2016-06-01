from square1 import argparser
from square1 import input_parser
from square1 import solve_cube

def main():
    args = argparser.parse()
    with open(args.input_file) as input_fileobj:
        cube = input_parser.read_input(input_fileobj)

    try:
        solution_steps = solve_cube.solve(cube, timeout=20)
    except solve_cube.TimeoutException:
        print 'Timeout reached with no solution found!'
        return

    # Print out the solution steps
    print 'Solution found! - Steps:'
    for steps in solution_steps:
        print steps


if __name__ == '__main__':
    main()
