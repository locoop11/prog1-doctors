# 2023-2024 Programação 1 (LTI)
# Grupo 30
# 60267 Antonio Neco
# 60253 Hugo Silva



from datetime import datetime
from datetime import timedelta
import constants as const


def hourToInt(time):
    """

    """
    t = time.split("h")
    return int(t[0])



def minutesToInt(time):
    """

    """
    t = time.split("h")
    return int(t[1])
    


def intToTime(hour, minutes):
    """

    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + "h" + m




def dayToInt(day):
    """

    """
    day = day.split(":")
    return int (day[0])


def monthToInt(month):
    """


    """
    month = month.split(":")
    return int (month[1])


def yearToInt(year):
    """
  
    """
    year = year.split(":")
    return int (year[2])



def addHoursToDateTime(dateTime, hours):
    """
        Function adds a time to a datetime.It only adds hours not minutes
        Requires: DateTime in the format "dd:mm:yyyy|hh:mm" and hour is the integer representing the number of hours to add. 
                  Unfortunately no validation is done on the dateTime format after adding the hours as it can be bigger than 24.
                  In that case the date will be wrong
        Ensures: Returns a string with the new date and time in the format "dd:mm:yyyy|hh:mm"
        Extra function reason: We need to add hours to the date and time of the last run mainly so we can calculate when next travel is.
    """
    time = dateTime.split("|")[1]
    date = dateTime.split("|")[0]
    newHour = hourToInt(time) + hours
    
    returnDate = ""
    # Compute current run date and time (which is 30 minutes after last run date unless it's a new day)
    if( newHour >= const.END_OF_DAY_INT_HOUR ):
        # This day is over we should start a new day based on todays date
        newTime = datetime.strptime(date, '%d:%m:%Y') + timedelta(days=1)
        returnDate = newTime.strftime("%d:%m:%Y") + "|" + const.START_OF_DAY_STRING_TIME
    else:
        # We are still in the same day
        returnDate = date + "|" + intToTime(newHour, minutesToInt(time))
    
    return returnDate


def biggestDate(dateTime1, dateTime2):
    """
    This function takes two dates and times and returns the biggest one.
    
    Requires: The dates and times to be in the format: dd:mm:yyyy|hh:mm
    
    Ensures: When the dates are the same, the function returns one of them
    
    Extra function reason: We need to compare dates and times to know which one is bigger
    """
    date1 = dateTime1.split("|")[0]
    date2 = dateTime2.split("|")[0]
    day1 = date1.split(":")[0]
    month1 = date1.split(":")[1]
    year1 = date1.split(":")[2]
    day2 = date2.split(":")[0]
    month2 = date2.split(":")[1]
    year2 = date2.split(":")[2]
    time1 = dateTime1.split("|")[1]
    time2 = dateTime2.split("|")[1]
    hour1 = time1.split(":")[0]
    min1 = time1.split(":")[1]
    hour2 = time2.split(":")[0]
    min2 = time2.split(":")[1]

    if date1 == date2 :
        if int ( hour1 + min1 )  >  int( hour2 + min2 ):
            return dateTime1
        else:
            return dateTime2
        
    else:
        if int(year1+month1+day1) > int(""+year2+month2+day2):
            return dateTime1
        else:
            return dateTime2

def updateHours(time):    
    min = minutesToInt(time)
    h=hourToInt(time)
    min=min +30
    if min>=60:
        h=h+1
        min=min-60
    finalTime=intToTime(h, min)
    return finalTime

def updateDay(day):
    """ This function adds one day to the given input date in the format dd:mm:yyyy.
        If the new day is bigger than 31, the month is updated. Also if the new month is bigger than 12, the year is updated.
        Also if the new day is in february and it's bigger than 28, the month is updated to march. Also if in february and it's a leap year, the day is updated to 29.
    """
    splittedDay = day.split(":")
    _day = splittedDay[0]
    _month = splittedDay[1]
    _year = splittedDay[2]
    intDay = int(_day)
    intMonth = int(_month)
    intYear = int(_year)
    intDay = intDay + 1
    if intDay > 31:
        intDay = 1
        intMonth = intMonth + 1
    if intMonth > 12:
        intMonth = 1
        intYear = intYear + 1
    if intDay > 28 and intMonth == 2:
        day = 1
        intMonth = 3
    if intDay > 29 and intMonth == 2 and intYear % 4 == 0:
        intDay = 29
    strDay = str(intDay)
    strMonth = str(intMonth)
    strYear = str(intYear)
    retDay = strDay + ":" + strMonth + ":" + strYear
    return retDay

def computeNewTimes(scheduleTime, scheduleDay):
    newScheduleTime = updateHours(scheduleTime)
    if( newScheduleTime[:2] == "20"):
        newScheduleTime = "04h00"
        newScheduleDay = updateDay(scheduleDay)
    else:
        newScheduleDay = scheduleDay
    return (newScheduleTime, newScheduleDay)
