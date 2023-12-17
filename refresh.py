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
import sys



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

        

def main():
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 4:
        print("Error: invalid number of arguments.")
        print("Usage: python refresh.py <doctors filename> <schedule filename> <requests filename>")
        return
    
    # Extract the file names from the command-line arguments
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    file3 = sys.argv[3]

    doctorsFileName = ""
    requestsFilName = ""
    scheduleFileName = ""

    for file in sys.argv:
        if file.find("doctors") != -1:
            doctorsFileName = file
        if file.find("schedule") != -1:
            scheduleFileName = file
        if file.find("requests") != -1:
            requestsFilName = file
    if( doctorsFileName == "" or requestsFilName == "" or scheduleFileName == ""):
        print("Error: invalid file name.")
        print("Usage: python refresh.py <doctors filename> <schedule filename> <requests filename>")
        exit(1)
    try:
        plan(doctorsFileName, scheduleFileName, requestsFilName)
    except Exception as e:
        print(f"An error occurred: {e}")
    # Optionally, you can perform additional error handling here if needed
    # ...
    # Exit in a controlled way (e.g., with a specific exit code)
    exit(1)  # Exit with a non-zero exit code to indicate an error


if __name__ == "__main__":
    main()