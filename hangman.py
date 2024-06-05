#Defining class for random picking of word
import random

print("Welcome to Hangman:")
wordDict = ["baby","code","python","game","house","alpha"]
randomWord = random.choice(wordDict)
for x in randomWord:
    print("_", end=" ")

#Defining a function to print the hangman diagram 
def print_hangman(wrong):
    if(wrong==0):
        print("\n+---+")
        print("   |")
        print("   |")
        print("   |")
        print("   ===")
    elif(wrong==1):
        print("\n+---+")
        print("O  |")
        print("   |")
        print("   |")
        print("   ===")
    elif(wrong==2):
        print("\n+---+")
        print("O  |")
        print("|  |")
        print("   |")
        print("   ===")
    elif(wrong==3):
        print("\n+---+")
        print(" O |")
        print("/| |")
        print("   |")
        print("   ===")
    elif(wrong==4):
        print("\n+---+")
        print(" O |")
        print("/|\|")
        print("   |")
        print("   ===")
    elif(wrong==5):
        print("\n+---+")
        print(" O |")
        print("/|\|")
        print("/  |")
        print("   ===")
    elif(wrong==6):
        print("\n+---+")
        print(" O |")
        print("/|\|")
        print("/ \|")
        print("   ===")

#Defining a function to print the correctly guessed letters 
def printWord(guessedLetters):
    counter=0
    rightLetters=0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[counter], end=" ")
            rightLetters+=1
        else:
            print(" ", end=" ")
        counter+=1
    return rightLetters

#Defining a function to give dashes under guessing word
def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E", end= " ")

#Main program for the Hangman game
length_word_to_guess = len(randomWord)
no_of_wrong = 0
cur_guess_index = 0
cur_letters_guessed = []
cur_letters_right = 0

while(no_of_wrong != 6 and cur_letters_right != length_word_to_guess):
    print("\nLetters guessed so far:")
    for letter in cur_letters_guessed:
        print(letter, end=" ")
    letterGuessed = input("\nGuess a letter")
    if(randomWord[cur_guess_index] == letterGuessed):
        print_hangman(no_of_wrong)
        cur_guess_index+=1
        cur_letters_guessed.append(letterGuessed)
        cur_letters_right = printWord(cur_letters_guessed)
        printLines()
    else:
        no_of_wrong+=1
        cur_letters_guessed.append(letterGuessed)
        print_hangman(no_of_wrong)
        cur_letters_right = printWord(cur_letters_guessed)
        printLines()

print("\nGame over")
