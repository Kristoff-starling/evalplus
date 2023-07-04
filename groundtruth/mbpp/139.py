"""
Write a function to find the circumference of a circle.
"""

def circle_circumference(r):
  assert isinstance(r, int), "invalid inputs" # $_CONTRACT_$
  assert r >= 0, "invalid inputs" # $_CONTRACT_$
  perimeter=2*3.1415*r
  return perimeter

import math

assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
assert math.isclose(circle_circumference(5), 31.415000000000003, rel_tol=0.001)
assert math.isclose(circle_circumference(4), 25.132, rel_tol=0.001)
