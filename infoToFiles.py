#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa

from dateTime import updatedheaderhour, updatedtitlehour
from infoFromFiles import saveheader


def writeScheduleFile(schedule, fileName):
    header = saveheader(fileName)
    header[3]= updatedheaderhour(header[3])
    timefilename= fileName[8:-4]
    timefilename= updatedtitlehour(timefilename)
    newFileName = fileName[:7]
    newFileName += timefilename + '.txt'
    newfile = open(newFileName, 'w')
    header = str(header)
    header = header.replace('[','')
    header = header.replace(']','')
    header = header.replace("'","")
    header = header.replace(",","")
    header = header.replace(r'\n','\n')
    header = header.replace(' ','')
    newfile.write(header)
    for item in schedule:
        item = str(item)
        item = item.replace('[','')
        item = item.replace(']','')
        item = item.replace("'","") 
        newfile.write(item + '\n')   
    newfile.close
    return newfile

def writeDoctorsFile(doctors, fileName):
    
    header = saveheader(fileName)
    header[3]= updatedheaderhour(header[3])
    timefilename= fileName[7:-4]
    timefilename= updatedtitlehour(timefilename)
    newFileName = fileName[:7]
    newFileName += timefilename + '.txt'
    newfile = open(newFileName, 'w')
    header = str(header)
    header = header.replace('[','')
    header = header.replace(']','')
    header = header.replace("'","")
    header = header.replace(",","")
    header = header.replace(r'\n','\n')
    header = header.replace(' ','')
    newfile.write(header)
    for item in doctors:
        item = str(item)
        item = item.replace('[','')
        item = item.replace(']','')
        item = item.replace("'","") 
        newfile.write(item + '\n')   
    newfile.close
    return newfile


doctors = ['Abílio Amaral' + '1' +  '10h30'+  '80'+ '7h20', 'Abílio Amaral' + '1' +  '10h30'+  '80'+ '7h20', 'Abílio Amaral' + '1' +  '10h30'+  '80'+ '7h20']
print(writeDoctorsFile(doctors, 'doctors10h00.txt'))