import os

# locates, opens and reads file
os.chdir("/Users/alyshapm/Desktop/BINUS/Algorithm and Programming/SEM 1/Texts")
openText = open("info.txt", "r")
fileContent = openText.read()

totalWordLength = sum(len(word) for word in fileContent.split()) # sum of the length or number of character for every word in the text file
wordCount = len(fileContent.split()) # counts the number of words in the text file
averageWordLength = totalWordLength / wordCount # calculates the average word length by dividing the sum of length for every word with the total word count
print("The average word length in this text file is {:.3} to 3 s.f.".format(averageWordLength))
