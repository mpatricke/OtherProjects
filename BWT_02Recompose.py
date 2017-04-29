# Burrows-Wheeler Transform part 2: read sorted data, recompose to original text
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
dataFilePath = configParser.get('BWT_config','dataFilePath')+'Out'+dataFileName
endFileName = configParser.get('BWT_config','dataFilePath')+'End'+dataFileName

with open(dataFilePath, 'rU') as textFile:
    textDataIn = textFile.read().rstrip('\n')

print "Input text:", textDataIn
print

lenText = len(textDataIn)

textDataArr = ['']*lenText

for j in range(lenText,0,-1):
    for i in range(0,lenText):

        textDataArr[i] = str(textDataIn[i]) + str(textDataArr[i])

    textDataArr = sorted(textDataArr)

for i in range(0,lenText):
    textTmp = textDataArr[i]
    if textTmp[:1] == configParser.get('BWT_config','startChar'):
        textDataUnxform = textDataArr[i]
        break

lenResult = len(textDataUnxform)
textDataUnxform = textDataUnxform[1:lenResult-1]

textDataUnxform = textDataUnxform.replace('xxxstartCharxxx', configParser.get('BWT_config','startChar'))
textDataUnxform = textDataUnxform.replace('xxxendCharxxx', configParser.get('BWT_config','endChar'))

with open(endFileName,'w+') as textFileOut:
    textFileOut.write(textDataUnxform)

#print "Output text:", textDataUnxform
print
print "Program:         ", os.path.abspath(__file__)
print "Input data file:  ... ", dataFilePath
#print "Output file:      ... ", endFileName
print "Execution time:", datetime.now() - starttime,"secs."