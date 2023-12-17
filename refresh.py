#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa
import constants as const
from infoFromFiles import readRequestsFile, readDoctorsFile, readScheduleFile
from planning import updateSchedule
from infoToFiles import writeScheduleFile, writeDoctorsFile
from dateTime import *



def plan(doctorsFileName, scheduleFileName, requestsFileName):
    """
    Runs the birthPlan application.

    Requires:
    doctorsFileName is a str with the name of a .txt file containing a list
    of doctors at date d and time t, organized as in the examples provided;
    scheduleFileName is a str with the name of a .txt file containing a list
    of birth assistances assigned to doctors at date d and time t, as in the examples provided;
    requestsFileName is a str with the name of a .txt file containing a list
    of cruises requested at date d and time t+30mins;
    Ensures:
    writing of two .txt files containing the updated list of doctors assigned
    to mothers and the updated list of birth assistances, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, doctorsXXhYY.txt and
    scheduleXXhYY.txt, where XXhYY represents the time 30 minutes
    after the time t indicated in the files doctorsFileName,
    scheduleFileName and requestsFileName, and are written in the same directory
    of the latter.
    """
    doctors = readDoctorsFile(doctorsFileName)
    (schedule, scheduleTime, scheduleDay) = readScheduleFile(scheduleFileName)      #le os ficheiros
    requests = readRequestsFile(requestsFileName)


    newSchedule = updateSchedule(doctors, requests, schedule, scheduleTime, scheduleDay)               #faz o update do schedule

    (scheduleFileName, doctorsFileName) = computeNewFileNames (scheduleTime, scheduleDay)


    writeDoctorsFile(doctors, doctorsFileName, scheduleDay, scheduleTime)
    writeScheduleFile(newSchedule, scheduleFileName, scheduleDay, scheduleTime)          
   
def computeNewFileNames (scheduleTime, scheduleDay):
    (newScheduleTime, newScheduleDay) = computeNewTimes(scheduleTime, scheduleDay)
    
    newScheduleFileName = "schedule" + newScheduleTime + ".txt"
    newDoctorsFileName = "doctors" + newScheduleTime + ".txt"

    return (newScheduleFileName, newDoctorsFileName)

plan("doctors19h00.txt", "schedule19h00.txt", "requests19h30.txt")

        

