#!/usr/local/bin/python3

from datetime import datetime
import os
import re
import sys

var = os.popen("pmset -g log | grep -e \"PowerButton\" -e \"Start\" | tail -1| awk {'print $1 \" Start time: \" $2 \" \"'} ").read();

# dobra, teraz trza by to troche porozdzielac na poziomie skryptu...

def getFile(filename):
	filedescriptor = open(filename, 'r')
	lines = filedescriptor.readlines()
	filedescriptor.close()
	return lines;


FORCE_READ_FROM_FILE = False # make it possible to set it via param

print("Add -f param to force read the overriding data from the file");
print("");
if(len(sys.argv) > 1 and sys.argv[1] == "-f"):
	FORCE_READ_FROM_FILE = True

if(FORCE_READ_FROM_FILE):
	print("WARNING! FORCE_READ_FROM_FILE FLAG ENABLED!");
data_read_from_file = False
var = var.rstrip() # remove newlines
log_read_corrupted = False
# do print beginhour w try catch i w catch: daymatches = False
try:
	begindate = var.split()[0]
	day_from_begindate = begindate.split("-")[2]
	begintime = var.split()[3] # extract the exact time in dd:dd:dd format
	beginhour = begintime.split(":")[0]
	beginmin = begintime.split(":")[1]
	beginsec = begintime.split(":")[2]
except IndexError:
	log_read_corrupted = True
currenttime = datetime.now().timetuple()
currenthour= currenttime[3]
currentmin = currenttime[4]
currentsec = currenttime[5]
currentday = currenttime[2]
currentmonth = currenttime[1]
currentyear = currenttime[0]

print("current time: "+str(currenthour) + ":" +str(currentmin) +":"+str(currentsec))

daymatches = False
testingMode = False

timediff = -1

if (testingMode == True):
	print("------------====== WARNING: testingMode ENABLED ======--------------")

if ((not log_read_corrupted) and currentday==int(day_from_begindate)):
	daymatches = True
	print("Day matches");

if (testingMode == True):
	daymatches = False
file_data_has_been_read = False
currenttimeobj = datetime.now()
if(daymatches == False or log_read_corrupted == True or FORCE_READ_FROM_FILE):
	print("day doesnt match (or forced to read from file via parameter), trying to read from file...")
	overridingDates = getFile("overriding_dates.txt")
	if(len(overridingDates)>0): # line format: 2016-03-10 09:00:00
		for x in range(0, len(overridingDates)):
			line = overridingDates[x].strip()
			currentline = line
			currentyear_read = int(re.split('[- :]', currentline)[0])
			currentday_read = int(re.split('[- :]', currentline)[2])
			currentmonth_read = int(re.split('[-: ]', currentline)[1])
			if(currentday == currentday_read and currentmonth == currentmonth_read and currentyear == currentyear_read):
				file_data_has_been_read = True
				beginhour=int(re.split('[- :]',currentline)[3])	
				beginmin=int(re.split('[- :]',currentline)[4])
				beginsec=int(re.split('[- :]', currentline)[5])
				print("found overridingData="+str(beginhour)+":"+str(beginmin))
				previoustimeobj = datetime(currenttimeobj.year, currenttimeobj.month, currenttimeobj.day, int(beginhour), int (beginmin), 0)
#			if(currentda
	else:
		print("failed (no entries)")
if(daymatches==False and (not file_data_has_been_read)):
	print("WARNING! Day does not match and overriding data not found!")
if(log_read_corrupted == False):
	previoustimeobj = datetime(currenttimeobj.year, currenttimeobj.month, currenttimeobj.day, int(beginhour), int(beginmin), int(beginsec))
	timediff = currenttimeobj - previoustimeobj
	previousJustHour = ""+str(beginhour)+":"+str(beginmin)+":"+str(beginsec);
	print("Workday begin: " + str(previousJustHour));
	print("NORMAL RESULT: "+str(timediff))

if ((daymatches==False or testingMode==True) and (not file_data_has_been_read)):
	print("Day does not match 2!");
	manualSelection = input ("Do you want to select the start time manually?");
	if(manualSelection=='y' or manualSelection=='Y'):
		print("Chose: yes");
		manualHour=input("Hour:");
		manualMinute=input("Minute:");
		previoustimeobj = datetime(currenttimeobj.year, currenttimeobj.month, currenttimeobj.day, int(manualHour), int (manualMinute), 0)
		overridingdatesFileDescriptor = open("overriding_dates.txt",'a')
		overridingdatesFileDescriptor.write(str(previoustimeobj)+"\n")
		overridingdatesFileDescriptor.close()
	else:
		print("Chose: other than yes");
		print("Leaving the script");

if ((daymatches==False or testingMode==True) and (file_data_has_been_read ==True or manualSelection=='y' or manualSelection=='Y')):
	timediff = currenttimeobj - previoustimeobj
	print ("Corrected time:")
	print(str(timediff))
if (not timediff==-1):
	filedescriptor = open("log.txt", 'a')
	filedescriptor.write(str(currenttimeobj.year).zfill(2)+"-"+str(currenttimeobj.month).zfill(2)+"-"+str(currenttimeobj.day).zfill(2)+": " + str(timediff)+"\n")
	filedescriptor.close()
