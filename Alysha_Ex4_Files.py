import os
import re

# locates, opens, and reads file
os.chdir("/Users/alyshapm/Desktop/BINUS/Algorithm and Programming/SEM 1/Texts")
openText = open("testFile.txt", "r")
readText = openText.read()

# file is closed
openText.close()

# the following are parameters (I'm not sure the word) that contain the set of characters to match
capitalLetters= "([A-Z])"
lowercase = "([a-z])"
digits = "([0-9])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
websites = "[.](com|net|org|io|gov)"
ie = "(i)[.](e)[.]"

editText = readText.replace("\n"," ") # replaces line with space
editText = re.sub(websites,"<prd>\\1",editText) # avoids splitting between a website
editText = re.sub(prefixes,"\\1<prd>",editText) # avoids splitting after prefixes
editText = re.sub(" "+suffixes+"[.]"," \\1<prd>",editText) # avoid splitting after suffix
editText = re.sub("[.]" + digits,"<prd>\\1",editText) # avoids splitting at a period between 2 numbers, i.e. 1.5 
editText = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",editText) # avoids splitting at a period between after a number, i.e. 0.9
editText = re.sub(ie, "i<prd>e<prd>", editText)  # converts i.e. to i<prd>e<prd>

# adds a <stop> after sentence boundaries, a point where the sentence will be split
editText = editText.replace("...","<prd><prd><prd><stop>") 
editText = editText.replace(".",".<stop>")
editText = editText.replace("?","?<stop>")
editText = editText.replace("!","!<stop>")
editText = editText.replace("<prd>",".") 
splitSentences = editText.split("<stop>") # split at <stop>
splitSentences = [sentence.strip() for sentence in splitSentences] # removes leading and trailing spaces

print(*splitSentences, sep="\n") # prints sentences on a new line