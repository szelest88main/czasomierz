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
	print(line)
	
	p = re.compile(r'*szata*')
	searchObj = p.search(str(line))
	print("Match: "+str(searchObj.groups()))
	
