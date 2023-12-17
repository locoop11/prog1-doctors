#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa

from dateTime import *



def writeScheduleFile(schedule, fileName, scheduleDay, scheduleTime):
    header = saveheader(fileName, scheduleDay, scheduleTime)
    newfile = open(fileName, 'w')
    newfile.writelines(header)
    schedule = sorted(schedule, key=lambda x: x[0])
    for item in schedule:
        item = str(item)
        item = item.replace('(','')
        item = item.replace(')','')
        item = item.replace('[','')
        item = item.replace(']','')
        item = item.replace("'","") 
        newfile.write(item + '\n')   
    newfile.close()
    return True

def saveheader(filename, scheduleDay, scheduleTime):
    (newScheduleTime, newScheduleDay) = computeNewTimes(scheduleTime, scheduleDay)
    
    header = []
    header.append("Organization:\n")
    header.append("SmartH\n")
    header.append("Hour:\n")
    header.append(newScheduleTime + "\n")
    header.append("Day:\n")
    header.append(newScheduleDay + "\n")
    if( filename.find("schedule") != -1):
        header.append("Schedule:\n")
    else :
        header.append("Doctors:\n")

    return header

def writeDoctorsFile(doctors, fileName, scheduleDay, scheduleTime):
    header = saveheader(fileName, scheduleDay, scheduleTime)
    newfile = open(fileName, 'w')
    newfile.writelines(header)
    doctors = sorted(doctors, key=lambda x: x[0])
    for item in doctors:
        item = str(item)
        item = item.replace('(','')
        item = item.replace(')','')
        item = item.replace('[','')
        item = item.replace(']','')
        item = item.replace("'","") 
        newfile.write(item + '\n')   
    newfile.close()
    return True

