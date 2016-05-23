"""Representation for the physical Square1 cube"""


class Wedge(object):

    """A specific wedge in the cube

    Contains color, position, and wedge angle data"""

    def __init__(self, color_face, color_side, angle, position):
        self.color_face = color_face
        self.color_side = color_side
        self.angle = angle
        self.position = position


class Cube(object):

    """Contains all the wedges in the cube

    Args:
      faces (Dict[Str]): Dict of colors for each face of the cube
    """

    def __init__(self, faces):
        self.faces = faces

    def __repr__(self):
        return '<Cube(faces={self.faces})>'.format(self=self)
