# 2023-2024 Programação 1 (LTI)
# Grupo 30
# 60267 Antonio Neco
# 60253 Hugo Silva


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
	newSchedule = createNewScheduleBasedOnPrevious(previousSched, scheduleTime, scheduleDay)
	(newScheduleTime, newScheduleDay) = computeNewTimes(scheduleTime, scheduleDay)

	sortRequests(requests)
	sortDoctors(doctors)

	for request in requests:
		doctor  = getMatchingDoctor(request, doctors) # get the doctor that is the best to do the request
		
		if( doctor != None):
			addDoctorToNewSchedule(doctor, request, newSchedule, newScheduleTime, newScheduleDay) # Updates doctor and the new schedule 
		else:
			# If a suitable doctor is not found, send request to another hospital
			sendRequestToOtherHospital(request, newSchedule, scheduleTime)

	return newSchedule

def sendRequestToOtherHospital(request, newSchedule, scheduleTime):
	"""
	Writes a request in the newSchedule with the message "redirected to other network" which signals that the request was sent to another hospital either because there are no doctors available 
	or because there are no doctors with the required skill level or even if the doctor does not have available time to perform the request.

	Requires:
	request that should be sent to another hospital, the schedule to which append the request to and the time of the schedule
	"""	
	newSchedule.append((scheduleTime, request[const.REQ_NAME_IDX], "redirected to other network"))

def addDoctorToNewSchedule(doctor, request, newSchedule, scheduleTime, scheduleDay):
	"""
	this funcion adds the doctor and the request in the newSchedule, and updates the doctor carcateristics
	Requires:
	The doctor to add to the schedule. The request to append to the schedule. The newSchedule to append the request to. The time of the schedule. The day of the schedule.

	Ensures:
	The doctor is added to the schedule and the doctor characteristics are updated.
	"""
	scheduleDoctorName = doctor[const.DOCT_NAME_IDX]
	scheduleRequestName = request[const.REQ_NAME_IDX]
	doctorScheduleTime = biggestDate(scheduleDay +"|"+scheduleTime.replace("h", ":"), scheduleDay +"|"+doctor[const.DOCT_LAST_END_SCHED_TIME_IDX].replace("h", ":"))
	doctorScheduleTime = doctorScheduleTime.split("|")[1].replace(":", "h")
	if( doctorScheduleTime[:2] == "20" and scheduleTime[:2] == "04"):
		doctorScheduleTime = scheduleTime
	else:
		if( doctorScheduleTime[:2] == "20"):
			return sendRequestToOtherHospital(request, newSchedule, scheduleTime)

	# Update newSchedule
	#newSchedule have tree elements the fisrts is the time of the new programmed intervemtion 
	newSchedule.append( (doctorScheduleTime, scheduleRequestName, scheduleDoctorName) )

	# Update doctor characteristics
	doctor[const.DOCT_ACCUM_HOURS_DAY_IDX] = str(int(doctor[const.DOCT_ACCUM_HOURS_DAY_IDX]) + 30)
	doctor[const.DOCT_ACCUM_TIME_WEEK_IDX] = updateHours(doctor[const.DOCT_ACCUM_TIME_WEEK_IDX])
	doctor[const.DOCT_LAST_END_SCHED_TIME_IDX] = updateHours(doctorScheduleTime)


def getMatchingDoctor(request, doctors):
	"""
	Calculates the doctors that have the required skill and availability to perform the request given

	Requires:
	The request to be performed and the list of all doctors

	Ensures:
	A doctor that has the required skill and availability to perform the request given. The doctors are sorted by priority which means that when more than one doctor is available 
	to perform the request the doctor with the highest priority is returned. Priority is given by the lowest accumulated hours in the day, the lowest accumulated hours in the week,
	"""	
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
	"""
	Function to be used to sort doctors by priority
	"""
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
	"""
	Checks thast a doctor is available to perform a request, ie is not in weekly leave and has enough hours to perform the request
	Requires:
	The doctor to check if is available
	Ensures to return a boolean value True if the doctor is available and False otherwise
	"""
	if doctor[const.DOCT_ACCUM_HOURS_DAY_IDX] != "weekly leave" :
		if updateHours(doctor[const.DOCT_ACCUM_TIME_WEEK_IDX])[0] == "4":
			return False
	return True

def createNewScheduleBasedOnPrevious(previousSched, scheduleTime, scheduleDay):
	"""
	Creates a new schedule copying to the new schedule all requests that are not yet performed
	Requires:
	the previous schedule to copy schedules from, the time of the schedule and the day of the schedule
	Ensures:
	To return a new schedule containing all requests that are not yet performed
	"""
	newScheduleTime = updateHours(scheduleTime)
	if( newScheduleTime[:1] == "20"):
		newScheduleTime = "04h00"
		newScheduleDay = updateDay(scheduleDay)
	else:
		newScheduleDay = scheduleDay

	newScheduleDate = newScheduleDay +"|"+newScheduleTime.replace("h", ":")
	newSchedule = []
	for oldSchedule in previousSched:
		oldScheduleDate = scheduleDay +"|"+oldSchedule[0].replace("h", ":")
		if( biggestDate(oldScheduleDate, newScheduleDate) == oldScheduleDate):
			newSchedule.append(oldSchedule)

	return newSchedule

def isDoctorSkillHigherOrEqual(doctor, request):
	"""
	Checks if a doctor skill is enough for a given request
	Requires: 
	The doctor to check if has the required skill and the request to be performed.
	Ensures:
	To return a boolean value True if the doctor has the required skill and False otherwise
	"""
	if request[-1] == 'high':
		if doctor[const.DOCT_TYPE_IDX] == '2' or doctor[const.DOCT_TYPE_IDX] == '3':
			return True
		else:
			return False
	return True	
	
def sortRequests(requests):
	"""
	Sorts requests by priority, bracelet color, age and Name of the mother 
	Requires:
	The requests to be sorted
	
	Ensures:
	The requests given as input to be, sorted by priority
	"""
	# Sort requests by priority then by color (red, them yellow then green), then by age descending then by name
	requests
	requests.sort(key=lambda x: (x[3], -color(x[2]), -int(x[1]), x[0]))

def color(color):
	"""
	Converts a color to an integerr to be used in sorting
	"""
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
	Sorts doctors by skill
	Requires:
	The list of doctorts to sort
	Ensures:
	The doctors given as input to be, sorted by skill
	"""
	# Sort doctors by priority then by name
	doctors.sort(key=lambda x: (-int(x[1])))




