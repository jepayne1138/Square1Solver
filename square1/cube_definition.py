"""Representation for the physical Square1 cube"""


class Wedge(object):

    """A specific wedge in the cube

    Contains color, position, and wedge angle data"""

    def __init__(self, color_face, color_sides):
        self.color_face = color_face
        self.color_sides = color_sides

    def __repr__(self):
        return (
            '<Wedge('
                'face={self.color_face}, '
                'sides={self.color_sides}'
            ')>'
        ).format(self=self)


class Cube(object):

    """Contains all the wedges in the cube

    Args:
      faces (Dict[Str]): Dict of colors for each face of the cube
    """

    def __init__(self, faces):
        self.faces = faces

    def __repr__(self):
        return '<Cube(faces={self.faces})>'.format(self=self)
