'''Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.'''

'''
a 1
b 2
c 3
d 4
e 5
f 6
g 7
h 8
i 9
j 10
k 11

111 -> 1-1-1, 11-1, 1-11

number of messages = length of number (single number letters) plus the number pairs less than 26

'''
import re

def possible_messages(code: int) -> int:
	string = str(code)
	#need to do an re to find leading zeros and subtract those from single
	single = len(string)
	zeros = 0
	for l in string:
		if re.match('0', l, flags = 0):
			zeros += 1
		else:
			pass	
	double = 0
	for n in range(len(string) - 1):
		twos = string[n:n+2]
		if re.match('0', twos, flags = 0):
			zeros +=1
		else:
			pass	
		#do the same re for leading zeros
		if int(twos) <= 26:
			double +=1
		else:
			pass			
	print (single + double - zeros)
	return 

possible_messages(12134)

'''1, 2, 1, 3, 4, 12, 21, 13'''
