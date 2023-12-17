# 2023-2024 Programação 1 (LTI)
# Grupo 30
# 60267 Antonio Neco
# 60253 Hugo Silva




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
    """
    Removes the header from a file.
    Requires:
    filename is a string with the name of the file to write to
    Ensures:
    To raise an exception if the file does not exist or if the header is not correct
    """
    l=[]
    i = 0
    f = None
    fileTime = filename.split(".")[0][-5:]
    fileType = ""
    if( filename.find("schedule") != -1):
        fileType = "Schedule:"
    if ( filename.find("doctors") != -1):
        fileType = "Doctors:"
    if ( filename.find("requests") != -1):
        fileType = "Mothers:"


    try:
        f = open(filename, "r")
        for line in f.readlines():
            l.append(line.strip())
        scheduleTime = l[3]
        scheduleDay = l[5]
        fileHeaderType = l[6]
        for i in l[:7]:
            l.remove(i)
    except Exception as e:
        raise e
    finally:
        if( f != None): 
            f.close()

    r=[]
    for line in l:
        r.append(line)
    
    if( fileHeaderType != fileType):
        raise ValueError("File head error: scope inconsistency between name and header in file " + filename + ".")
    

    return r, scheduleTime, scheduleDay
