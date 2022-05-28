# FIND WORDS ---> https://www.bestwordlist.com/indexwordswith.htm
import random
import sys 
from termcolor import colored

print("\n")
numTries = int(input("Enter number of tries (1-10): "))
numBlanks = numTries

def getWords(file):
    wordle_file = open(file, "r")
    wordArray = wordle_file.read().splitlines()
    wordle_file.close()
    return wordArray

allWords = getWords("6LettersAllWords.txt")
mostUsed = getWords("6LettersMostUsed.txt")
finalWord = random.choice(mostUsed).upper()

def checkWord(word):
    for realWord in allWords:
        if firstWord.upper() == realWord.upper():
            return word
    print("\nWord does not exist. Try again.\n")
    return "||||||"

def checkFinalWord(word):
    if word.upper() == "X":
        sys.exit()
    if word.upper() == finalWord.upper():
        printTries()
        print("YOU WIN! THE WORD WAS " + word.upper() + "!\n") 
        sys.exit()

def colorWords(word):
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

def printTries():
    match numBlanks:
        case 10:
            colorWords(firstWord.upper())
            colorWords(secondWord.upper())
            colorWords(thirdWord.upper())
            colorWords(fourthWord.upper())
            colorWords(fifthWord.upper())
            colorWords(sixthWord.upper())
            colorWords(seventhWord.upper())
            colorWords(eighthWord.upper())
            colorWords(ninthWord.upper())
            colorWords(tenthWord.upper())
        case 9:
            colorWords(firstWord.upper())
            colorWords(secondWord.upper())
            colorWords(thirdWord.upper())
            colorWords(fourthWord.upper())
            colorWords(fifthWord.upper())
            colorWords(sixthWord.upper())
            colorWords(seventhWord.upper())
            colorWords(eighthWord.upper())
            colorWords(ninthWord.upper())
        case 8:
            colorWords(firstWord.upper())
            colorWords(secondWord.upper())
            colorWords(thirdWord.upper())
            colorWords(fourthWord.upper())
            colorWords(fifthWord.upper())
            colorWords(sixthWord.upper())
            colorWords(seventhWord.upper())
            colorWords(eighthWord.upper())
        case 7:
            colorWords(firstWord.upper())
            colorWords(secondWord.upper())
            colorWords(thirdWord.upper())
            colorWords(fourthWord.upper())
            colorWords(fifthWord.upper())
            colorWords(sixthWord.upper())
            colorWords(seventhWord.upper())
        case 6:
            colorWords(firstWord.upper())
            colorWords(secondWord.upper())
            colorWords(thirdWord.upper())
            colorWords(fourthWord.upper())
            colorWords(fifthWord.upper())
            colorWords(sixthWord.upper())
        case 5:
            colorWords(firstWord.upper())
            colorWords(secondWord.upper())
            colorWords(thirdWord.upper())
            colorWords(fourthWord.upper())
            colorWords(fifthWord.upper())
        case 4:
            colorWords(firstWord.upper())
            colorWords(secondWord.upper())
            colorWords(thirdWord.upper())
            colorWords(fourthWord.upper())
        case 3:
            colorWords(firstWord.upper())
            colorWords(secondWord.upper())
            colorWords(thirdWord.upper())
        case 2:
            colorWords(firstWord.upper())
            colorWords(secondWord.upper())
        case 1:
            colorWords(firstWord.upper())

firstWord = "||||||"
secondWord = "||||||"
thirdWord = "||||||"
fourthWord = "||||||"
fifthWord = "||||||"
sixthWord = "||||||"
seventhWord = "||||||"
eighthWord = "||||||"
ninthWord = "||||||"
tenthWord = "||||||"

while firstWord == "||||||" and numTries > 0:
    firstWord = input("\nEnter first word: ")
    checkFinalWord(firstWord)
    firstWord = checkWord(firstWord)
    if firstWord != "||||||":
        printTries()
        numTries -= 1

while secondWord == "||||||" and numTries > 0:
    secondWord = input("\nEnter second word: ")
    checkFinalWord(secondWord)
    secondWord = checkWord(secondWord)
    if secondWord != "||||||":
        printTries()
        numTries -= 1

while thirdWord == "||||||" and numTries > 0:
    thirdWord = input("\nEnter third word: ")
    checkFinalWord(thirdWord)
    thirdWord = checkWord(thirdWord)
    if thirdWord != "||||||":
        printTries()
        numTries -= 1

while fourthWord == "||||||" and numTries > 0:
    fourthWord = input("\nEnter fourth word: ")
    checkFinalWord(fourthWord)
    fourthWord = checkWord(fourthWord)
    if fourthWord != "||||||":
        printTries()
        numTries -= 1

while fifthWord == "||||||" and numTries > 0:
    fifthWord = input("\nEnter fifth word: ")
    checkFinalWord(fifthWord)
    fifthWord = checkWord(fifthWord)
    if fifthWord != "||||||":
        printTries()
        numTries -= 1

while sixthWord == "||||||" and numTries > 0:
    sixthWord = input("\nEnter sixth word: ")
    checkFinalWord(sixthWord)
    sixthWord = checkWord(sixthWord)
    if sixthWord != "||||||":
        printTries()
        numTries -= 1

while seventhWord == "||||||" and numTries > 0:
    seventhWord = input("\nEnter seventh word: ")
    checkFinalWord(seventhWord)
    seventhWord = checkWord(seventhWord)
    if seventhWord != "||||||":
        printTries()
        numTries -= 1

while eighthWord == "||||||" and numTries > 0:
    eighthWord = input("\nEnter eighth word: ")
    checkFinalWord(eighthWord)
    eighthWord = checkWord(eighthWord)
    if eighthWord != "||||||":
        printTries()
        numTries -= 1

while ninthWord == "||||||" and numTries > 0:
    ninthWord = input("\nEnter ninth word: ")
    checkFinalWord(ninthWord)
    ninthWord = checkWord(ninthWord)
    if ninthWord != "||||||":
        printTries()
        numTries -= 1

while tenthWord == "||||||" and numTries > 0:
    firstWord = input("\nEnter tenth word: ")
    checkFinalWord(tenthWord)
    tenthWord = checkWord(tenthWord)
    if tenthWord != "||||||":
        printTries()
        numTries -= 1

sys.exit("\nYOU LOSE. TRY AGAIN!\n")