"""Representation for the physical Square1 cube"""


class Wedge(Object):

    """A specific wedge in the cube

    Contains color, position, and wedge angle data"""

    def __init__(self, color_face, color_side, angle, position):
        self.color_face = color_face
        self.color_side = color_side
        self.angle = angle
        self.position = position


class Cube(Object):

    """Contains all the wedges in the cube"""

    def __init__(self):
        pass
