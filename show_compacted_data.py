#!/usr/local/bin/python3
import os
import re

def getFile(filename):
	filedescriptor = open(filename, 'r')
	lines = filedescriptor.readlines()
	filedescriptor.close()
	return lines;
	
#filedescriptor = open("log.txt", 'r')
#lines = filedescriptor.readlines()
#filedescriptor.close()

lines = getFile("log.txt")

#print("The file:")
#for line in lines:
#	print(line,end="")
lines_compacted = []
print("Now lines in array using for loop:")
for x in range(0, len(lines)):
	line = lines[x].strip()
	currentline = line.split()[0];
	previousline = "";
	lastline = "";
	if(x!=0):	
		previousline = lines[x-1].split()[0];
	if(x!=0 and (currentline!=previousline)):
		print(lines[x-1].strip())	
		lastline = lines[x-1].strip()

	if((x==len(lines)-1 and currentline!=lastline)):
		print(lines[x].strip())
