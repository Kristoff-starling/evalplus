"""
Write a python function to find the length of the smallest list in a list of lists.
"""

def Find_Min_Length(lst):  
    assert isinstance(lst, list), "invalid inputs" # $_CONTRACT_$
    assert len(lst) > 0, "invalid inputs" # $_CONTRACT_$
    assert all(isinstance(item, list) for item in lst), "invalid inputs" # $_CONTRACT_$
    minLength = min(len(x) for x in lst )
    return minLength 



assert Find_Min_Length([[1],[1,2]]) == 1
assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3
