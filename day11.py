'''Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
'''


import re
from typing import List

def auto_complete(words: List[str], seed: str) -> List[str]:
	matches = []
	for word in words:
		if re.match(seed, word):
			matches.append(word)
		else:
			pass
	print(matches)		
	return matches

ex = ['dog', 'deer', 'deal']

auto_complete(ex, 'de')				


test = ['apple', 'application', 'axe', 'batt', 'mouse']

auto_complete(test, 'm')