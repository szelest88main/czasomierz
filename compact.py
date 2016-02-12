#!/usr/local/bin/python3
import os
filedescriptor = open("test.txt", 'r')
lines = filedescriptor.readlines()
filedescriptor.close()
for line in lines:
	print(line,end="")


