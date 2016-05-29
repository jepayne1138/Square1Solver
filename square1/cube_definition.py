"""Representation for the physical Square1 cube

I'm stating it here once for now that we repeatedly will use the number of
side colors of a wedge as a proxy for the angle of the wedge itself as if the
wedge has one color on the side is it a small wedge of 30d, and a large wedge
of 60d will have two colors as it is always a corner piece.  This means we
will essentially treat each side color as representing a 30d slice.
"""
from pprint import pprint
TOP = 'top'
BOTTOM = 'bottom'
HALF_COLORS = 6
# When validating if a wedge defines a full straight boundary on the left side
# we count the side colors of wedges proceeding right from the starting wedge
# as this represents even slices of 30d for each color.  If we hit this value
# of HALF_COLORS = 6 we know we have a full boundary (6 * 30d = 180d).  If we
# exceed this value we know a large wedge fills the boundary location 180d
# from our starting wedge's left side and we don't have a straight line.

class Wedge(object):

    """A specific wedge in the cube

    Contains color, position, and wedge angle data

    Args:
      color_face (str): Color of the side face of the wedge
      color_side (List[str]): List of colors on the side of the wedge
    """

    def __init__(self, color_face, color_sides, face_color_dict):
        self.color_face = color_face
        self.color_sides = color_sides
        self.face = face_color_dict[color_face]
        self.name = self.get_name(face_color_dict)

    def __repr__(self):
        return (
            '<Wedge('
                'name={self.name}, '
                'face={self.color_face}, '
                'sides={self.color_sides}'
            ')>'
        ).format(self=self)

    def get_name(self, face_color_dict):
        """Generates a name based on the colors of the wedge"""
        return '_'.join(
                sorted([face_color_dict[color] for color in self.color_sides])
        )


class Cube(object):

    """Contains all the wedges in the cube

    Args:
      faces (Dict[Str]): Dict of colors for each face of the cube
    """

    def __init__(self, faces, wedges):
        self.faces = faces
        self.wedges = wedges

    def __repr__(self):
        return (
            '<Cube('
                'faces={self.faces}), '
                'wedges={self.wedges}'
            '>'
        ).format(self=self)

    def flip(self, top_wedge, bottom_wedge):
        """Flip along the boundary defined by a top and bottom wedge"""
        # Rotate wedges to the beginning of the
        self.rotate_wedge_to_front(top_wedge, TOP)
        self.rotate_wedge_to_front(bottom_wedge, BOTTOM)

        # Get the number of wedges defining exactly half of on side
        top_slice_size = self.get_half_slice_size(TOP)
        bottom_slice_size = self.get_half_slice_size(BOTTOM)

        # Validate that the wedges defines a flippable boundary
        if top_slice_size is None or bottom_slice_size is None:
            return False
            raise ValueError('Invalid wedges')

        # Perform the flip
        top_slice = self.wedges[TOP][:top_slice_size]
        self.wedges[TOP] = self.wedges[BOTTOM][:bottom_slice_size] + self.wedges[TOP][top_slice_size:]
        self.wedges[BOTTOM] = top_slice + self.wedges[BOTTOM][bottom_slice_size:]
        return True

    def rotate_wedge_to_front(self, wedge, side):
        """Rotates the wedge list so the given wedge is first

        Returns:
          boolean: True if the wedge was found in the list and is not first
        """
        # Find wedge location in wedge dict
        if wedge not in self.wedges[side]:
            return False
        wedge_index = self.wedges[side].index(wedge)
        front_slice = self.wedges[side][:wedge_index]
        back_slice = self.wedges[side][wedge_index:]
        self.wedges[side] = back_slice + front_slice
        return True

    def get_half_slice_size(self, side):
        """Returns the number of wedges forms exactly one half of the side

        Returns:
          int: Number of wedges the form half of a side exactly (None if not
            possible)
        """
        slice_wedge_sides = 0
        wedge_index = 0

        while slice_wedge_sides < HALF_COLORS:
            cur_wedge = self.wedges[side][wedge_index]
            slice_wedge_sides += len(cur_wedge.color_sides)
            wedge_index += 1

        if slice_wedge_sides == HALF_COLORS:
            return wedge_index
        return None

    def print_wedges(self):
        pprint(self.wedges)
