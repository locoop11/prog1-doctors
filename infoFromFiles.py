#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa



def readDoctorsFile(fileName):
    """
    Reads a file with a list of doctors into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of doctors organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a doctor listed in
    the file fileName (with all the info pieces belonging to that doctor),
    following the order provided in the lines of the file.
    """

    (inFile, fileTime, fileDay) = removeHeader(fileName)       

    doctorsList = [] 
    for line in inFile:
        requestData = str(line).rstrip().split(", ")
        doctorsList.append(requestData)        

    return doctorsList


def readRequestsFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.

    
    """

    (inFile, fileTime, fileDay) = removeHeader(fileName)       

    requestsList = [] 
    for line in inFile:
        requestData = str(line).rstrip().split(", ")
        requestsList.append(requestData)        

    return requestsList


def readScheduleFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.

    
    """

    (inFile, scheduleTime, scheduleDay) = removeHeader(fileName)       

    scheduleList = [] 
    for line in inFile:
        scheduleData = line.rstrip().split(", ")
        scheduleList.append(scheduleData)        

    return (scheduleList, scheduleTime, scheduleDay)




def removeHeader(filename):
    l=[]
    i = 0
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    finally:
        for line in f.readlines():
            l.append(line.strip())
        scheduleTime = l[3]
        scheduleDay = l[5]
        for i in l[:7]:
            l.remove(i)
    r=[]
    for line in l:
        r.append(line)
    
    

    return r, scheduleTime, scheduleDay



removeHeader('schedule10h00.txt')