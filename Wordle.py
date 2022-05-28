import random
import sys 
from termcolor import colored

class OutOfRange(Exception): #ERROR FOR NUMBERS OUTSIDE OF THE REQUIRED RANGE
    pass

numTries = 0
while numTries > 10 or numTries < 1: #RUNS UNTIL USER ENTERS NUMBER BETWEEN 1 AND 10
    try:
        numTries = int(input("\nEnter number of tries (1-10): "))
        if numTries > 10 or numTries < 1:
            raise OutOfRange
    except ValueError: 
        print("\nInput must be a number!")
    except OutOfRange:
        print("\nNumber must be between 1 and 10!")
numBlanks = numTries

totalWords = ["||||||", "||||||", "||||||", "||||||", "||||||", "||||||", "||||||", "||||||", "||||||", "||||||"]
numWords = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

def getWords(file): #CREATES AN ARRAY OF THE WORDS FROM THE FILE PARAMETER
    wordle_file = open(file, "r")
    wordArray = wordle_file.read().splitlines()
    wordle_file.close()
    return wordArray

allWords = getWords("6LettersAllWords.txt")
mostUsed = getWords("6LettersMostUsed.txt")
finalWord = random.choice(mostUsed).upper()

def checkWord(word): #CHECKS TO SEE IF PARAMETER IS 6 LETTERS AND IF IT IS A REAL WORD
    splitWord = list(word)
    if len(word) != 6:
        print("\nWord must be 6 letters. Try again.")
        return "||||||"
    for x in range(0,5):
        if splitWord[x] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("\nWord can only contain letters. Try again.")
            return "||||||"
    for realWord in allWords:
        if word.upper() == realWord.upper():
            return word
    print("\nWord does not exist. Try again.")
    return "||||||"

def checkFinalWord(word): #CHECKS TO SEE IF PARAMETER MATCHES THE CORRECT WORD
    if word.upper() == "X":
        sys.exit()
    if word.upper() == finalWord.upper():
        printTries(totalWords)
        sys.exit("\nYOU WIN! THE WORD WAS " + word.upper() + "!\n")

def colorWords(word): #COLORS THE PARAMETER BASED ON THE LETTERS IN THE CORRECT WORD
    splitWord = list(word)
    splitFinalWord = list(finalWord)

    for x in range(0,6): 
        if splitWord[x] == splitFinalWord[x]:
            splitWord[x] = colored(splitWord[x], 'green')
            splitFinalWord[x] = "0"
        for y in range(0,6):
            if splitWord[x] == splitFinalWord[y]:
                splitWord[x] = colored(splitWord[x], 'yellow')
                splitFinalWord[y] = "0"
    print(splitWord[0] + splitWord[1] + splitWord[2] + splitWord[3] + splitWord[4] + splitWord[5])

def printTries(totalWords): #PRINTS OUT THE USERS ATTEMPTS
    colorWords(totalWords[0].upper())
    if numBlanks > 1:
        colorWords(totalWords[1].upper())
    if numBlanks > 2:
        colorWords(totalWords[2].upper())
    if numBlanks > 3:
        colorWords(totalWords[3].upper())
    if numBlanks > 4:
        colorWords(totalWords[4].upper())
    if numBlanks > 5:
        colorWords(totalWords[5].upper())
    if numBlanks > 6:
        colorWords(totalWords[6].upper())
    if numBlanks > 7:
        colorWords(totalWords[7].upper())
    if numBlanks > 8:
        colorWords(totalWords[8].upper())
    if numBlanks > 9:
        colorWords(totalWords[9].upper())

for x in range(0, numBlanks):
    while totalWords[x] == "||||||" and numTries > 0:
        totalWords[x] = input("\nEnter " + numWords[x] + " word: ")
        checkFinalWord(totalWords[x])
        totalWords[x] = checkWord(totalWords[x])
        if totalWords[x] != "||||||":
            print()
            printTries(totalWords)
            numTries -= 1

sys.exit("\nYOU LOSE! THE WORD WAS " + finalWord + "!\n")