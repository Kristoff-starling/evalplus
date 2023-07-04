"""
Write a function to check for the number of jumps required of given length to reach a point of form (d, 0) from origin in a 2d plane.
"""

def min_Jumps(steps, d): 
    assert isinstance(steps, tuple), "invalid inputs" # $_CONTRACT_$
    assert len(steps) == 2, "invalid inputs" # $_CONTRACT_$
    assert all(isinstance(x, int) for x in steps), "invalid inputs" # $_CONTRACT_$
    assert isinstance(d, int), "invalid inputs" # $_CONTRACT_$
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2



assert min_Jumps((3,4),11)==3.5
assert min_Jumps((3,4),0)==0
assert min_Jumps((11,14),11)==1
