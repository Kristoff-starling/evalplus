"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
"""

def max_product_tuple(list1):
    assert isinstance(list1, list), "invalid inputs" # $_CONTRACT_$
    assert all(isinstance(x, tuple) for x in list1), "invalid inputs" # $_CONTRACT_$
    assert all(len(x) == 2 for x in list1), "invalid inputs" # $_CONTRACT_$
    assert all(isinstance(x[0], (int, float)) for x in list1), "invalid inputs" # $_CONTRACT_$
    assert all(isinstance(x[1], (int, float)) for x in list1), "invalid inputs" # $_CONTRACT_$
    result_max = max([abs(x * y) for x, y in list1] )
    return result_max



assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
assert max_product_tuple([(10,20), (15,2), (5,10)] )==200
assert max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==484
