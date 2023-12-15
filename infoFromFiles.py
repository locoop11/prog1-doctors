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

    inFile = removeHeader(fileName)       

    doctorsList = [] 
    for line in inFile:
        requestData = line.rstrip().split(", ")
        doctorsList.append(requestData)        

    return doctorsList


def readDoctorsFile(fileName):
    """
   this funcion reads a file that contans a line that is called hour and then reutrns the string on the next line that is the hour
    """
    






def readRequestsFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.

    
    """

    inFile = removeHeader(fileName)       

    requestsList = [] 
    for line in inFile:
        requestData = line.rstrip().split(", ")
        requestsList.append(requestData)        

    return requestsList




def readScheduleFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.

    
    """

    inFile = removeHeader(fileName)       

    scheduleList = [] 
    for line in inFile:
        scheduleData = line.rstrip().split(", ")
        scheduleList.append(scheduleData)        

    return scheduleList







def removeHeader(filename):
    l=[]
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print("Could not found any file")
    finally:
        for line in f.readlines():
            l.append(line)
        for i in l[:7]:
            l.remove(i)
    r=[]
    for line in l:
        r.append(line)
    return r



#print(readRequestsFile('schedule10h00.txt'))