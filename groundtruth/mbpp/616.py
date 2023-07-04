"""
Write a function which takes two tuples of the same length and performs the element wise modulo.
"""

def tuple_modulo(test_tup1, test_tup2):
  assert isinstance(test_tup1, tuple), "invalid inputs" # $_CONTRACT_$
  assert isinstance(test_tup2, tuple), "invalid inputs" # $_CONTRACT_$
  assert len(test_tup1) == len(test_tup2), "invalid inputs" # $_CONTRACT_$
  assert all(isinstance(x, int) for x in test_tup1 + test_tup2), "invalid inputs" # $_CONTRACT_$
  assert all(x > 0 for x in test_tup2), "invalid inputs" # $_CONTRACT_$
  res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2)) 
  return (res) 



assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
assert tuple_modulo((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)
assert tuple_modulo((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)
