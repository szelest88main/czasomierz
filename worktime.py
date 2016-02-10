#!/usr/local/bin/python3
from datetime import datetime
import os

var = os.popen("pmset -g log | grep -e \"PowerButton\" -e \"Start\" | tail -1| awk {'print $1 \" Start time: \" $2 \" \"'} ").read();
# samo pmset log, jak zemulować jebane awk?

# dobra, teraz trza by to troche porozdzielac na poziomie skryptu...

var = var.rstrip() # remove newlines
begindate = var.split()[0]
print("Work begin hour for day " + begindate + ":" )

begintime = var.split()[3] # extract the exact time in dd:dd:dd format
beginhour = begintime.split(":")[0]
beginmin = begintime.split(":")[1]
beginsec = begintime.split(":")[2]
print(""+beginhour+":"+beginmin+":"+beginsec)

currenttime = datetime.now().timetuple()
currenthour= currenttime[3]
currentmin = currenttime[4]
currentsec = currenttime[5]
currentday = currenttime[2]
print("Current time: "+str(currenthour)+":"+str(currentmin)+":"+str(currentsec))
print("Current date (day): " + str(currentday))

currenttimeobj = datetime.now()
previoustimeobj = datetime(currenttimeobj.year, currenttimeobj.month, currenttimeobj.day, int(beginhour), int(beginmin), int(beginsec))
timediff = currenttimeobj - previoustimeobj
print(str(timediff))

filedescriptor = open("worklog.txt", 'a')
filedescriptor.write(str(begindate)+": " + str(timediff)+"\n")
filedescriptor.close()
