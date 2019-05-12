'''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''
from typing import List



def sum_check(num_list: List[int], target: int) -> bool:
	pair_sums = []
	for i, num in enumerate(num_list):
		for j in range(len(num_list)):
			if j+1 == len(num_list) or i+1 == len(num_list) or i > j :
				pass
			else:
				pair_sums.append(num + num_list[j+1])
	check = target in pair_sums
#	print(pair_sums)
	print(check)
	return check	

nums = [10, 15, 3, 7]
sum_check(nums, 17)

num2 = [1, 4, 5, 8, 10, 14, 16, 19]

sum_check(num2, 11)