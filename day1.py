'''Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?'''

from typing import List

sample = [1, 2, 3, 4, 5]

def no_i_in_product(num_list: List[int]) -> List[int]:
	output = []
	for i, num in enumerate(num_list):
		fill = 1
		j = i
		for j in range(len(num_list)):
			if j == i or j >= len(num_list):
				pass
			else:
				if fill == 1:
					fill = num_list[j]
				else:
					fill =	fill * num_list[j]
		output.append(fill)
	print(output)
	return output

no_i_in_product(sample)			

test = [2, 4, 6, 8, 10]
no_i_in_product(test)