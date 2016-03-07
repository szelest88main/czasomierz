#!/usr/local/bin/python3
import os
import re
filedescriptor = open("log.txt", 'r')
lines = filedescriptor.readlines()
filedescriptor.close()
#print("The file:")
#for line in lines:
#	print(line,end="")
lines_compacted = []
print("The file and containing test:");
#for line in lines:
#	if "d" in line:
#		print(line.strip()+" contains d\n", end="")
#	else:
#		print(line.strip()+" does not\n", end = "")
		
#while hasNext:
#	if ("d" in lines[i]):
#		lines_compacted
print("Now lines in array using for loop:")
for x in range(0, len(lines)):
	#print("processing"+str(x)+":"+lines[x].strip());
	line = lines[x].strip()
#	print("processed line:"+line)
#	print("Splited line:" + str(line.split()));
#	print("Splited line components:" + str(len(line.split())));
		#print(line.strip()+" is ok");
	currentline = line.split()[0];
	previousline = "";
#	if(x==0 && lines // jeśli jest ppierwszy (0) i inny niż kolejny, daj go
	lastline = "";
	if(x!=0):	
		previousline = lines[x-1].split()[0];
	if(x!=0 and (currentline!=previousline)):
		print(lines[x-1].strip())	
		lastline = lines[x-1].strip()

	if((x==len(lines)-1 and currentline!=lastline)): # nie że jest różna od poprzedniej, tylko że jest różna od ostatniej wyświetlonej (czy tam dodanej do docelowego kontenera)
		print(lines[x].strip())
