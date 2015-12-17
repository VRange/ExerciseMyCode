#! /usr/bin/env python
def judge(n):
	if n < 10:
		print "<10"
	elif n > 10 and n < 100:
		print "> 10 and < 100" 
	else:
		print "Nan"

print judge(9)

print judge(15)

print judge (99)

print judge (101)
