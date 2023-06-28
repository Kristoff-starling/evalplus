"""
Write a function that takes in the radius and height of a cylinder and returns the the volume.
"""

def volume_cylinder(r,h):
  volume=3.1415*r*r*h
  return volume

import math

assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
assert math.isclose(volume_cylinder(4,5), 251.32000000000002, rel_tol=0.001)
assert math.isclose(volume_cylinder(4,10), 502.64000000000004, rel_tol=0.001)
