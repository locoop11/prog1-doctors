#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa
import constants as const
from infoFromFiles import readRequestsFile, readDoctorsFile, readScheduleFile
from dateTime import updatehours

def updateSchedule(doctors, requests, previousSched): #  nextTime falta meter isto
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


	# 1. Ordenar os pedidos por ordem de prioridade
	
	# Sort request by priority
	sortRequests(requests)
	sortDoctors(doctors)
	match(doctors, requests)


def match(doctors, requests):
	newSchedule = []
	for i in len(doctors):
		if requests[i][-1] == 'hight':
			for docotor in doctors:
				if docotor[const.DOCT_Type_IDX] == '2' or docotor[const.DOCT_Type_IDX] == '3':
					newSchedule.append(requests[i][0], docotor[i][0])
		

	



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
	for i in range(len(doctors)):
		if doctors[i][2] == 'weekly leave':
			doctors[i][2] = '0'
		else:
			doctors[i][2] = '1'
					


doctors = readDoctorsFile('doctors10h00.txt')
requests = readRequestsFile('requests10h00.txt')

print(requests)
print("============")
sortRequests(requests)
print(requests)









