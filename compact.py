#!/usr/local/bin/python3
import os
import re
filedescriptor = open("test.txt", 'r')
lines = filedescriptor.readlines()
filedescriptor.close()
for line in lines:
	print(line,end="")
lines_compacted = []
for line in lines:
	if "d" in line:
		print(line.strip()+" contains d\n", end="")
	else:
		print(line.strip()+" does not\n", end = "")
		
#while hasNext:
#	if ("d" in lines[i]):
#		lines_compacted
print("Now lines in array using for loop")
for x in range(0, len(lines)):
	line = lines[x].strip()
	#print(line)
#	print("Splited line:" + str(line.split()));
#	print("Splited line components:" + str(len(line.split())));
	if(len(lines[x-1].split())>0 and len(line.split())>0):
		if(x!=0 and lines[x-1].split()[0]!=line.split()[0]):
			print(lines[x-1].strip())	
