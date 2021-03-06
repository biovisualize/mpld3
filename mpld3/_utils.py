"""Utility Routines"""
import warnings

from matplotlib.colors import colorConverter

def get_text_coordinates(txt):
    """Get figure coordinates of a text instance"""
    return txt.get_transform().transform(txt.get_position())


def color_to_hex(color):
    """Convert rgb tuple to hex color code"""
    rgb = colorConverter.to_rgb(color)
    return '#{:02X}{:02X}{:02X}'.format(*(int(255 * c) for c in rgb))


def many_to_one(input_dict):
    """Convert a many-to-one mapping to a one-to-one mapping"""
    return dict((key, val)
                for keys, val in input_dict.items()
                for key in keys)

LINESTYLES = many_to_one({('solid', '-'): "10,0",
                          ('dashed', '--'): "8,8",
                          ('dotted', ':'): "2,2",
                          ('', ' ', 'None', 'none'): "none"})

def get_dasharray(line):
    """Get an SVG dash array for the given matplotlib linestyle"""
    ls = line.get_linestyle()
    dasharray = LINESTYLES.get(ls, None)
    if dasharray is None:
        warnings.warn("dash style '{0}' not understood: "
                      "defaulting to solid.".format(ls))
        dasharray=LINESTYLES['-']
    return dasharray
