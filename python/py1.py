#!/usr/bin/env python
def f(n)
	if n == 1:
		return 1
	return n * f(n-1)

print f(2)
