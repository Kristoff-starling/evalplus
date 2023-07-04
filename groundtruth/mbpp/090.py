"""
Write a python function to find the length of the longest word.
"""

def len_log(list1):
    assert isinstance(list1, list), "invalid inputs" # $_CONTRACT_$
    assert len(list1) > 0, "invalid inputs" # $_CONTRACT_$
    assert all(isinstance(item, str) for item in list1), "invalid inputs" # $_CONTRACT_$
    max=len(list1[0])
    for i in list1:
        if len(i)>max:
            max=len(i)
    return max



assert len_log(["python","PHP","bigdata"]) == 7
assert len_log(["a","ab","abc"]) == 3
assert len_log(["small","big","tall"]) == 5
