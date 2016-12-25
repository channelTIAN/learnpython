#!/usr/bin/python
# -*- conding: utf-8 -*-


def Calculate():
	sum = 0
	num = [i for i in range(10)]
	print("all number are : ")
	for i, number in enumerate(num):
		print(number, "", end = "")
		if (i < len(num) - 1):
			print(",", end = "")
		else:
			print("\n")
		sum += number
	print ("and the sum is:", sum)
	
if __name__ == "__main__":
	print("tell you a secret:")
	Calculate()