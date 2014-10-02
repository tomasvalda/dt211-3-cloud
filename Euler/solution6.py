#!/usr/bin/python

sum_square = 0		# sum of squares
sum_num = 0		# sum of numbers
y = 1			# counter
difference = 0

for x in range(100):
	sum_square = sum_square + y * y		# sum of the squares of the first 100 numbers
	sum_num = sum_num + y			# sum of the first 100 numbers
	y = y + 1				# counter

sum_num = sum_num * sum_num			# the square of the first 100 numbers

difference = sum_num - sum_square

print difference				# print the difference between
