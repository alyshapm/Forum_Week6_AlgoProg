import os

# locates, opens, and reads file by lines
os.chdir("/Users/alyshapm/Desktop/BINUS/Algorithm and Programming/SEM 1/Texts")
openText = open("info.txt", "r")
unnumberedText = openText.readlines()

# file is closed
openText.close()

lineNumber = 1 # number is set to 1 so that it doesn't count from 0
numberedList = [] # new list is declared
for line in unnumberedText:
    lineNumber += 1 # for every line, 1 is added to the lineNumber, in which the resultant value will replace the previous value
    numberedLines = lineNumber, line # the format will be number, then the line
    numberedList.append(numberedLines)
numberedListToString = "\n".join([str(line) for line in numberedList[1:]]) # because .write cannot append lists, I converted it into a string

numberedText = open("fileWrittenEx2.txt","w") # open file for the text to be appended
numberedText.write(numberedListToString) 
numberedText.close() 

