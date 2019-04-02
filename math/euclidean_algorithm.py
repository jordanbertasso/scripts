#!/usr/bin/env python3

a = int(input('Input a: '))
b = int(input('Input b: ')) 
r = a % b

while (not (r==0)):
	q = a//b
	r = a%b

	print(str(a) + " = " + str(q) + " x " + str(b) + " + " + str(r))

	a = b
	b = r
