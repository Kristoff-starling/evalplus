"""
The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
"""

def filter_data(students,h,w):
    assert isinstance(students, dict), "invalid inputs" # $_CONTRACT_$
    assert all(isinstance(x, str) for x in students.keys()), "invalid inputs" # $_CONTRACT_$
    assert all(isinstance(x, tuple) for x in students.values()), "invalid inputs" # $_CONTRACT_$
    assert isinstance(h, (int, float)), "invalid inputs" # $_CONTRACT_$
    assert isinstance(w, (int, float)), "invalid inputs" # $_CONTRACT_$
    assert h >= 0, "invalid inputs" # $_CONTRACT_$
    assert w >= 0, "invalid inputs" # $_CONTRACT_$
    result = {k: s for k, s in students.items() if s[0] >=h and s[1] >=w}
    return result    



assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},5.9,67)=={'Cierra Vega': (6.2, 70),'Kierra Gentry': (6.0, 68)}
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},5.7,64)=={'Cierra Vega': (6.2, 70),'Alden Cantrell': (5.9, 65),'Kierra Gentry': (6.0, 68),'Pierre Cox': (5.8, 66)}
