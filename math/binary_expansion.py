#!/usr/bin/env python3

binary = str(input('Enter binary number: '))

result = ''

for i in range(len(binary)):
	if binary[i] == '1':
		result = result + '2^'+'{'+str(len(binary)-i-1)+'}' + ' + '

	else:
		result = result + '0' + ' + '

print(result)
