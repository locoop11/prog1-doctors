#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa

from infoFromFiles import readRequestsFile, readDoctorsFile, readScheduleFile
import constants as const
from infoFromFiles import readRequestsFile, readDoctorsFile, readScheduleFile
from dateTime import *
import re

def updateSchedule(doctors, requests, previousSched, scheduleTime, scheduleDay): #  nextTime falta meter isto
	"""
    Update birth assistance schedule assigning the given birth assistance requested
    to the given doctors, taking into account a previous schedule.
	
	Requires:
	doctors is a list of lists with the structure as in the output of
	infoFromFiles.readDoctorsFile concerning the time of previous schedule;
	requests is a list of lists with the structure as in the output of 
	infoFromFile.readRequestsFile concerning the current update time;
	previousSched is a list of lists with the structure as in the output of
	infoFromFiles.readScheduleFile concerning the previous update time;
	nextTime is a string in the format HHhMM with the time of the next schedule
	Ensures:
	a list of birth assistances, representing the schedule updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	of the project (omitted here for the sake of readability).
	"""
	# doctors exemple: ((Guilherme Gaspar, 2, weekly leave, 60, 40h10)(Horácio Horta, 3, 14h50, 140, 7h40)Ildefonso Inácio, 2, weekly leave, 60, 40h10)(José Justo, 2, 14h50, 60, 15h20))

	# request exemple: (Hortênsia Holmes, 22, yellow, low)
	# schedule exemple: (14h00, Eduarda Elói, Horácio Horta)


	# 1. Sort request by priority and doctors by skill
	newSchedule = createNewScheduleBasedOnPrevious(previousSched)
	sortRequests(requests)
	sortDoctors(doctors)
	motherWithoutDoctor = []
	for request in requests:
		doctor  = getMatchingDoctor(request, doctors) # get the doctor that is the best to do the request
		
		if( doctor != None):
			addDoctorToNewSchedule(doctor, request, newSchedule, scheduleTime, scheduleDay) # Updates doctor and the new schedule 
		else:
			# If a suitable doctor is not found, send request to another hospital
			newSchedule.append(scheduleTime, request[const.REQ_NAME_IDX], "redirected to other network")

	return newSchedule

def addDoctorToNewSchedule(doctor, request, newSchedule, scheduleTime, scheduleDay):
	"""
	this funcion adds the doctor and the request in the newSchedule, and updates the doctor carcateristics
	retorna um boleeano
	"""
	scheduleDoctorName = doctor[const.DOCT_NAME_IDX]
	scheduleRequestName = request[const.REQ_NAME_IDX]
	scheduleTime = biggestDate(scheduleDay +"|"+scheduleTime.replace("h", ":"), scheduleDay +"|"+doctor[const.DOCT_LAST_END_SCHED_TIME_IDX].replace("h", ":"))
	scheduleTime = scheduleTime.split("|")[1].replace(":", "h")
	
	# Update newSchedule
	#newSchedule have tree elements the fisrts is the time of the new programmed intervemtion 
	newSchedule.append( (scheduleTime, scheduleRequestName, scheduleDoctorName) )

	# Update doctor characteristics
	doctor[const.DOCT_ACCUM_HOURS_DAY_IDX] = str(int(doctor[const.DOCT_ACCUM_HOURS_DAY_IDX]) + 30)
	doctor[const.DOCT_ACCUM_TIME_WEEK_IDX] = updatehours(doctor[const.DOCT_ACCUM_TIME_WEEK_IDX])
	doctor[const.DOCT_LAST_END_SCHED_TIME_IDX] = updatehours(doctor[const.DOCT_LAST_END_SCHED_TIME_IDX])








def getMatchingDoctor(request, doctors):
	
	listOfMatchingDoctors = []
	for doctor in doctors:
		# A doctor is NOT availbale to do the request if:
		#    he is already fully booked for the day
		#    doctor has not enough hours free to do the request
		if( isDoctorSkillHigherOrEqual(doctor, request) ):
			# If the doctor is available to do the request, check if he has the right skill
			# That is we need to check that the skill of the available doctor is equal or higher than the request
			if isDoctorAvailable(doctor):
				listOfMatchingDoctors.append(doctor)
			#sort the doctors most qualifeid first in the list
	if len(listOfMatchingDoctors) == 0:
		return None
	else:
		prioritezeDoctors(listOfMatchingDoctors)
		return listOfMatchingDoctors[0]

def prioritezeDoctors(listOfMatchingDoctors):
	listOfMatchingDoctors.sort(key=custom_sort_key)

# Define a custom sorting key function
def custom_sort_key(arr):
	type = int(arr[const.DOCT_TYPE_IDX])
	accumHours = int(arr[const.DOCT_ACCUM_HOURS_DAY_IDX])
	accumTimeWeek = arr[const.DOCT_ACCUM_TIME_WEEK_IDX]
    
	match = re.match(r'(\d{2})h(\d{2})', accumTimeWeek)
	if match:
		hours, minutes = map(int, match.groups())
	else:
		hours, minutes = 0, 0
    
	return (-type, accumHours, hours, minutes)

def isDoctorAvailable(doctor):
	if doctor[const.DOCT_ACCUM_HOURS_DAY_IDX] != "weekly leave" :
		if updatehours(doctor[const.DOCT_ACCUM_TIME_WEEK_IDX])[0] == "4":
			return False
	return True

def createNewScheduleBasedOnPrevious(previousSched):
	newSchedule = []
	# for i in range(1, len(previousSched)):
	# 	newSchedule.append(previousSched[0])

	# # TODO: This function needs to remove the schedules that are already done (schedule time is less than current time)
	return newSchedule

def isDoctorSkillHigherOrEqual(doctor, request):
	"""
	this funcion return a tuple
	"""
	if request[-1] == 'high':
		if doctor[const.DOCT_TYPE_IDX] == '2' or doctor[const.DOCT_TYPE_IDX] == '3':
			return True
		else:
			return False
	return True	
	
def sortRequests(requests):
	"""
	Requires:
	requests is a list of lists with the structure as in the output of 
	infoFromFile.readRequestsFile concerning the current update time;
	Ensures:
	a list of lists with the same structure as requests, sorted by priority
	"""
	# Sort requests by priority then by color (red, them yellow then green), then by age descending then by name
	requests
	requests.sort(key=lambda x: (x[3], -color(x[2]), -int(x[1]), x[0]))

def color(color):
	if color == 'red':
		return 3
	elif color == 'yellow':
		return 2
	elif color == 'green':
		return 1
	else:
		return 10
	
def sortDoctors(doctors):
	"""
	Requires:
	doctors is a list of lists with the structure as in the output of
	infoFromFiles.readDoctorsFile concerning the time of previous schedule;
	Ensures:
	a list of lists with the same structure as doctors, sorted by priority
	"""
	# Sort doctors by priority then by name
	doctors.sort(key=lambda x: (-int(x[1])))

doctors = readDoctorsFile('doctors10h00.txt')
requests = readRequestsFile('requests10h30.txt')
(schedule, scheduleTime, scheduleDay) = readScheduleFile('schedule10h00.txt')
newSchedule = updateSchedule(doctors, requests, schedule, scheduleTime, scheduleDay)

print(requests)
print("============")
print(doctors)



