#!/bin/env python
def f(n):
	i = 0
	sum = 0
	while i < n:
		sum += i
		i = i + 1
		print sum
	return sum


print f(10)

n = raw_input()

print f(int(n))
