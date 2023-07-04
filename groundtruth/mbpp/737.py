"""
Write a function to check whether the given string is starting with a vowel or not using regex.
"""

import re 
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
def check_str(string): 
	assert isinstance(string, str), "invalid inputs" # $_CONTRACT_$
	return re.search(regex, string)



assert check_str("annie")
assert not check_str("dawood")
assert check_str("Else")
