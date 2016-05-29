import csv
import cube_definition as cube_def
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
        cube_def.TOP: [],
        cube_def.BOTTOM: [],
    }

    for line_num, line in enumerate(reader):
        if line_num < NUM_FACES:
            face_color_dict[line[0]] = line[1]
        else:
            wedges[line[0]].append(
                cube_def.Wedge(line[1], line[2:], face_color_dict)
            )

    # TODO:  Add validation to inputs
    cube = cube_def.Cube(face_color_dict, wedges)
    return cube
