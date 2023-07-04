"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
"""

def check_smaller(test_tup1, test_tup2):
  assert isinstance(test_tup1, tuple), "invalid inputs" # $_CONTRACT_$
  assert isinstance(test_tup2, tuple), "invalid inputs" # $_CONTRACT_$
  assert len(test_tup1) == len(test_tup2), "invalid inputs" # $_CONTRACT_$
  assert all(isinstance(x, int) for x in test_tup1), "invalid inputs" # $_CONTRACT_$
  assert all(isinstance(x, int) for x in test_tup2), "invalid inputs" # $_CONTRACT_$
  return all(x > y for x, y in zip(test_tup1, test_tup2))



assert check_smaller((1, 2, 3), (2, 3, 4)) == False
assert check_smaller((4, 5, 6), (3, 4, 5)) == True
assert check_smaller((11, 12, 13), (10, 11, 12)) == True
