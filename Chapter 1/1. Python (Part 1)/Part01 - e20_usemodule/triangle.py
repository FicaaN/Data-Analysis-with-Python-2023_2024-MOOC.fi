"""
A module for calculating properties of right-angled triangles.

This module provides functions to calculate the hypotenuse and the area of a right-angled triangle given the lengths of its sides.

Functions:
- hypotenuse(a, b): Returns the length of the hypotenuse.
- area(a, b): Returns the area of the triangle.
"""

import math

__version__ = "1.0"
__author__ = "FicaaN"


def hypotenuse(a, b):
    """
    Calculate the length of the hypotenuse of a right-angled triangle.
    """
    return math.sqrt(a**2 + b**2)


def area(a, b):
    """
    Calculate the area of a right-angled triangle.
    """
    return 0.5 * a * b
