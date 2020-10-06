import re
inputfile = "raw_enm_alarm.csv"
outputfile = "enm_alarm.csv"
log = open (inputfile, "r")
alarm_id = {}

for line in log:
    #Skip "External Link Failure" alarm
    if re.search ("External Link Failure", line):
        pass
    #Skip "External Alarm"
    elif re.search ("External Alarm", line):
        pass 
    elif re.search ('SubNetwork=LTE_', line):
        if re.search ('CLEARED', line):
            alarm = line.split("\t")
            if len(alarm) > 26:
                if not alarm[26] in alarm_id.keys():
                    alarm_id[alarm[26]] = []
                    alarm_id[alarm[26]].append(alarm[1])
                    alarm_id[alarm[26]].append(alarm[3][:10])
                    alarm_id[alarm[26]].append(alarm[0])
                    alarm_id[alarm[26]].append(alarm[2])
                    #alarm_id[alarm[26]].append(alarm[4])
                    alarm_id[alarm[26]].append(alarm[11])
                    alarm_id[alarm[26]].append(alarm[1]+"_"+alarm[11].split("=")[1])
                    alarm_id[alarm[26]].append(alarm[18][:10])
                else:
                    alarm_id[alarm[26]][6] = alarm[18][:10]
            
        elif re.search ("MINOR", line) or re.search ("MAJOR", line) or re.search ("CRITICAL", line):
            alarm = line.split("\t")
            if len(alarm) > 26:
                if not alarm[26] in alarm_id.keys():
                    alarm_id[alarm[26]] = []
                    alarm_id[alarm[26]].append(alarm[1])
                    alarm_id[alarm[26]].append(alarm[3][:10])
                    alarm_id[alarm[26]].append(alarm[0])
                    alarm_id[alarm[26]].append(alarm[2])
                    #alarm_id[alarm[26]].append(alarm[4])
                    alarm_id[alarm[26]].append(alarm[11])
                    alarm_id[alarm[26]].append(alarm[1]+"_"+alarm[11].split("=")[1])
                    alarm_id[alarm[26]].append("2020-08-31")
                    #2020-08-31 is the enddate used to spread the alarms

enmalarm = open (outputfile, "w+")
enmalarm.write ("SITENAME,ALARMDATE,SEVERITY,SPECIFIC PROBLEM,Alarm_object,SITENAME_MO,CEASEDDATE\n")            
for i in alarm_id.keys():
    enmalarm.write (",".join(alarm_id[i]))
    enmalarm.write("\n")
enmalarm.close()
