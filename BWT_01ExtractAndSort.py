# Burrows-Wheeler Transform part 1: extract and sort input data, write to a file
#
# https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform

from datetime import datetime
import os
import ConfigParser

starttime = datetime.now()

def nameValCalc(name):
    nameValue = 0
    for i in range(0,len(str(name))):
        nameValue += alphaData.index(name[i])
    return nameValue

os.chdir(os.path.dirname(os.path.abspath(__file__)))

configParser = ConfigParser.RawConfigParser()   
configFilePath = r'BWT_config.txt'
configParser.read(configFilePath)

dataFileName = configParser.get('BWT_config','dataFileName')
dataFilePath = configParser.get('BWT_config','dataFilePath')+dataFileName
outFileName = configParser.get('BWT_config','dataFilePath')+'Out'+dataFileName

with open(dataFilePath, 'rU') as textFile:
	textData = textFile.read().rstrip('\n')

textData = configParser.get('BWT_config','startChar')+textData+configParser.get('BWT_config','endChar')

print "Input text:",textData

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

for i in range(0,lenText):
	textDataLastCol = textDataLastCol + textDataArrSort[i][-1]

with open(outFileName,'w+') as textFileOut:
    textFileOut.write(textDataLastCol)

print
print "Output text:", textDataLastCol

print
print "Program:         ", os.path.abspath(__file__)
print "Input data file:  ... ", dataFilePath
print "Output file:      ... ", outFileName
print "Execution time:", datetime.now() - starttime,"secs."