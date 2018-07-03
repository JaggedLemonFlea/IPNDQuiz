# Steve Brylka IPND Stage 2 Final Project

# function to clear the terminal window -------------------------------------------------------------------------------
def clearScreen():
	import os
	osname = os.name
	print osname
	if osname == 'posix':
		os.system('clear')
	elif osname == 'nt' or osname == 'dos':
		os.system('clr')
	else:
		print('\n' * 30)

# Clears the screen and asks user for their name and say hello --------------------------------------------------------
clearScreen()
print "<Fill 'em In> - a quiz game coded in Python by Steve Brylka\n"
name = raw_input('Please type your name: ')

# Game Data -----------------------------------------------------------------------------------------------------------
# game title string for use througout the program
gameTitle = "<Fill 'em In> - a quiz game coded in Python by Steve Brylka\n"

# Easy Test variables:
easyText = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
easyAnswers = ['function', 'arguments', 'None', 'list']

# Medium Test variables:
mediumText = '''Medium difficulty test text with ___1___, ___2___, ___3___, and ___4___ blanks.'''
mediumAnswers = ['One', 'Two', 'Three', 'Four']

# Hard Test variables:
hardText = '''Hard difficulty test text with ___1___, ___2___, ___3___ and ___4___ blanks.'''
hardAnswers = ['One', 'Two', 'Three', 'Four']

# list of blanks
gameBlanks = ['___1___', '___2___', '___3___', '___4___']

# delay and clear screen function -------------------------------------------------------------------------------------
def timeDelay():
	import time
	delay = 1
	count = 1
	while count > 0:
		# print count
		time.sleep(delay)
		count = count -1
	clearScreen()

# Sets the game difficulty per user input -----------------------------------------------------------------------------
def setLevel():
	clearScreen()
	print gameTitle + '\nHello ' + name + ', welcome to the Quiz.\n'
	loop = True
	while loop == True:
		userInput = raw_input('''Please select a game difficulty by typing it in.\n\nYour choices are easy / medium / hard.\n\n: ''').lower()
		if userInput == 'easy' or userInput == 'medium' or userInput == 'hard':
			clearScreen()
			print gameTitle + '\nYou have selected ' + userInput + '!\n\nGood Luck ' + name + '!'
			loop = False
			return userInput
		else:
			clearScreen()
			print gameTitle + '\nSorry ' + name + ', that is not a valid entry, please try again.\n'

# function that pulls game level data ---------------------------------------------------------------------------------
def setGameData(level):
	if level == 'easy':
		gameData = [easyText, easyAnswers]
	elif level == 'medium':
		gameData = [mediumText, mediumAnswers]
	else:
		level == 'hard'
		gameData = [hardText, hardAnswers]
	return gameData

# function that pulls the blanks from the game text -------------------------------------------------------------------
def findBlanks(index, word, gameText):
	for word in gameText:
		if word == gameBlanks[index]:
			return word
		else:
			return None

# function to replace blanks with the correct answer ------------------------------------------------------------------
def fillBlanks(index, gameText, userInput):
    replaced = []
    text = gameText.split()
    for word in text:
        replacement = findBlanks(index, word, gameText)
        if replacement == gameBlanks[index]:
            word = word.replace(replacement, userInput)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced


# function that plays the game ----------------------------------------------------------------------------------------
# def playGame():
	# level, attemptsLeft, index = setLevel(), 5, 0
	# gameText, gameAnswers = setGameData(level)[0], setGameData(level)[1]
	# while attemptsLeft > 0:
	# 	timeDelay()
	# 	if index != 4:
	# 		print gameTitle + "\nThis is the " + level + " quiz. You have " + str(attemptsLeft) + " guesses left for this quiz.\n\n" + gameText
	# 		userInput = raw_input("\nPlease type you answer for " + gameBlanks[index] + ": ").lower()
	# 		if userInput == gameAnswers[index].lower():
	# 			print "\nThat's right!"
	# 			index += 1
	# 		else:
	# 			print "\nSorry " + name + ", that is incorrect, please try again."
	# 			attemptsLeft = attemptsLeft - 1
	# 	else:
	# 		clearScreen()
	# 		print gameTitle + "\n" + gameText + "\n\nWay to go " + name + ", you finished the quiz with " + str(attemptsLeft) + " attempts left!!!"
	# 		return
	# clearScreen()
	# print gameTitle + "\nThis is the " + level + " quiz. You have " + str(attemptsLeft) + " guesses left for this quiz.\n\n" + gameText + '\n\nSorry ' + name + ', you answered incorrectly too many times. Game Over!'

# test function -------------------------------------------------------------------------------------------------------
def playGame():
	level, attemptsLeft, index, userInput = setLevel(), 5, 0, ""
	gameText, gameAnswers, blank = setGameData(level)[0], setGameData(level)[1], gameBlanks[index]
	while attemptsLeft > 0:
		timeDelay()
		if index < len(gameBlanks):
			print gameTitle + "\nThis is the " + level + " quiz. You have " + str(attemptsLeft) + " guesses left for this quiz.\n\n" + gameText
			userInput = raw_input("\nPlease type you answer for " + gameBlanks[index] + ": ").lower()
			if userInput == gameAnswers[index].lower():
				print "\nThat's right!"
				gameText = fillBlanks(index, gameText, userInput)
				index += 1
			else:
				print "\nSorry " + name + ", that is incorrect, please try again."
				attemptsLeft = attemptsLeft - 1
		else:
			clearScreen()
			print gameTitle + "\n" + gameText + "\n\nWay to go " + name + ", you finished the quiz with " + str(attemptsLeft) + " attempts left!!!"
			return
	clearScreen()
	print gameTitle + "\nThis is the " + level + " quiz. You have " + str(attemptsLeft) + " guesses left for this quiz.\n\n" + gameText + '\n\nSorry ' + name + ', you answered incorrectly too many times. Game Over!'


# Starts the Game -----------------------------------------------------------------------------------------------------
playGame()
