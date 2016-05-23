import csv
import cube_definition
from pprint import pprint

NUM_FACES = 6


def read_input(fileobj):
    """Parses an input csv into a Cube instance

    As per the README instructions:
     - first 6 lines define the colors of the cube
     - next 16 lines define starting wedge position"""
    reader = csv.reader(fileobj)
    face_color_dict = {}
    wedges = {
        'top': [],
        'bottom': [],
    }

    for line_num, line in enumerate(reader):
        if line_num < NUM_FACES:
            face_color_dict[line[0]] = line[1]
        else:
            wedges[line[0]].append(
                cube_definition.Wedge(line[1], line[2:])
            )

    # TODO:  Add validation to inputs
    cube = cube_definition.Cube(face_color_dict)
    return cube
