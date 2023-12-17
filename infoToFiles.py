# 2023-2024 Programação 1 (LTI)
# Grupo 30
# 60267 Antonio Neco
# 60253 Hugo Silva


from dateTime import *



def writeScheduleFile(schedule, fileName, scheduleDay, scheduleTime):
    """
    Writes the schedule to a file.
    Requires:
    schedule is a list of lists each containing a schedule item (Hour, Mother, Doctor)
    fileName is a string with the name of the file to write to
    scheduleDay is a string in the format DD-MM-YYYY with the day of the current schedule
    scheduleTime is a string in the format HHhMM with the time of the current schedule
    Ensures:
    writing of a .txt file containing the updated list of birth assistances, according to schedule
    The schedule is writen sorted by hour
    """
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
    """
    Saves the header of the file.
    Requires:
    filename is a string with the name of the file to write to
    scheduleDay is a string in the format DD-MM-YYYY with the day of the current schedule
    scheduleTime is a string in the format HHhMM with the time of the current schedule

    Ensures:
    header is a list of strings with the header of the file
    The header changes according to the filename (schedule or doctors)
    """
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
    """
    Writes the doctors to a file.
    Requires:
    doctors is a list of lists each containing a doctor (Name, Type, Skill)
    fileName is a string with the name of the file to write to
    scheduleDay is a string in the format DD-MM-YYYY with the day of the current schedule
    scheduleTime is a string in the format HHhMM with the time of the current schedule

    Ensures:
    writing of a .txt file containing the updated list of doctors
    The doctors are writen sorted by name
    """
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

