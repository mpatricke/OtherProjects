# Burrows-Wheeler Transform
#
# https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform

from datetime import datetime
import os

starttime = datetime.now()

def nameValCalc(name):
    nameValue = 0
    for i in range(0,len(str(name))):
        nameValue += alphaData.index(name[i])
    return nameValue

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#rowCount = rowLen = maxProd = iMax = jMax = prodNxt = iterCount = 0

#with open('Data/BWT_Banana.txt', 'rU') as textFile:
#with open('Data/BWT_Mississippi.txt', 'rU') as textFile:
with open('Data/BWT_TreatyOfWaitangiA0part.txt', 'rU') as textFile:
#with open('Data/BWT_TreatyOfWaitangiA0.txt', 'rU') as textFile:
#with open('Data/BWT_TreatyOfWaitangiComplete.txt', 'rU') as textFile:
	textData = textFile.read().rstrip('\n')

textData = "${0}#".format(textData)

print textData

lenText = len(textData)
textDataArr = [0]*lenText
textDataLastCol = ''

textDataArr[0] = textData

for i in range(1,lenText):
	startChar = textData[:1]
	textDataTmp = textData[1:]
	textData = textDataTmp + startChar
	textDataArr[i] = textData

textDataArrSort = sorted(textDataArr)

for i in range(1,lenText):
	textDataLastCol = textDataLastCol + textDataArrSort[i][-1]

print textDataLastCol


print
print "Program:       ", os.path.abspath(__file__)
print "Data file:     ", textFile
#print "Data file:     ", newPath
print "Execution time:", datetime.now() - starttime,"secs."