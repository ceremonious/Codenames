import math
import random

def length(vector):
    sumOfSquares = 0
    for num in vector:
        sumOfSquares += num * num
    return math.sqrt(sumOfSquares)

def dotProduct(a, b):
    curSum = 0
    for i in range(0, len(a)):
        curSum += a[i] * b[i]
    return curSum

def cosSim(word1, word2, wordVectors):
    try:
        a = wordVectors[word1]
    except KeyError:
        return 0
    try:
        b = wordVectors[word2]
    except KeyError:
        return 0
    try:
        output = dotProduct(a[0], b[0]) / (a[1] * b[1])
    except ZeroDivisionError:
        output = 0
    return output

#Stores the word vectors in a list of tuples where the first entry is the
#vector and the second entry is the lenght of the vector
def readVectors():
    f = open('wordVectors.txt', 'r')
    wordVectors = {}
    for line in f:
        data = line.split()
        word = data[0]
        vector = tuple([float(i) for i in data[1:]])
        vectorInfo = (vector, length(vector))
        wordVectors[word] = vectorInfo
    return wordVectors

def readWordList():
    f = open('codenamesWords.txt', 'r')
    words = []
    for line in f:
        words.append(line.rstrip().lower())
    return words

#Create a Codenames board using the list of words
def createBoard(wordList):
    tempList = wordList[:]
    random.shuffle(tempList)
    board = {"blue": [], "red": [], "gray": [], "black": []}
    for i in range(0, 9):
        board["blue"].append(tempList.pop())
    for i in range(0, 8):
        board["red"].append(tempList.pop())
    for i in range(0, 7):
        board["gray"].append(tempList.pop())
    board["black"].append(tempList.pop())
    return board

#The best clue is the clue with the greatest cosine similarity
def bestClue(clues):
    maxSim = 0
    maxClue = ""
    for key in clues:
        if clues[key][1] > maxSim:
            maxClue = key
    return maxClue

#A clue is only legal if the clue does not appear in the word
def legalClue(word1, word2):
    return (word1 not in word2 and word2 not in word1)

SIMILARITY_THRESHOLD = 0.25
words = readWordList()
wordVectors = readVectors()

while True:
    board = createBoard(words)
    clues = {}
    print board["blue"]
    for word in board["blue"]:
        for key in wordVectors:
            #For each possible word, if it exceeds the SIMILARITY_THRESHOLD,
            #check if it would work as a clue for other words. If so, add it
            #to the clue list.
            if legalClue(key, word) and key not in clues.keys():
                sim = cosSim(key, word, wordVectors)
                if (sim > SIMILARITY_THRESHOLD):
                    totalSim = sim
                    clueList = [word]
                    for word2 in board["blue"]:
                        sim2 = cosSim(key, word2, wordVectors)
                        if (not word == word2 and legalClue(key, word2) and sim2 > SIMILARITY_THRESHOLD):
                            totalSim += sim2
                            clueList.append(word2)
                    if len(clueList) >= 2:
                        clues[key] = (clueList, totalSim)
                        print (clueList, key)
    print board["blue"]
    best = bestClue(clues)
    print "Best Clue: "
    print (best, clues[best])
    raw_input("Next")
