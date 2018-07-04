# Steve Brylka IPND Lesson 3 Final Project
# Code Your Own Quiz

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

# Clears the screen at the start of the quiz to get rid of all the mess -----------------------------------------------
clearScreen()

# Game Data -----------------------------------------------------------------------------------------------------------
# game title string for use througout the program
gameTitle = "<Fill 'em In> - a quiz game about the band Tool coded in Python by Steve Brylka\n"
print gameTitle # prints the game title

# Easy Test variables:
easyText = '''Tool is an American rock band from Los Angeles, California. Formed in ___1___, the group's 
line-up includes drummer Danny Carey, guitarist ___2___, and vocalist Maynard James Keenan. 
Justin Chancellor has been the band's ___3___ since 1995, replacing their original ___3___ ___4___.'''
easyAnswers = ['1990', 'Adam Jones', 'bassist', "Paul D'Amour"]
easyBlanks = ['___1___', '___2___', '___3___', '___4___']

# Medium Test variables:
mediumText = '''The band emerged with a heavy metal sound on their first studio album, ___1___ (1993), 
and later became a dominant act in the alternative metal movement, with the release of their second album, 
___2___ in 1996. Their efforts to unify musical experimentation, visual arts, and a message of personal evolution 
continued, with ___3___ (2001) and the most recent album, ___4___ (2006), gaining the band critical acclaim, 
and commercial success around the world.  But before that, their first commercial release was ___5___ (1992).'''
mediumAnswers = ['Undertow', 'Aenima', 'Lateralus', '10,000 Days', 'Opiate']
mediaumBlanks = ['___1___', '___2___', '___3___', '___4___', '___5___']

# Hard Test variables:
hardText = '''A component of Tool's song repertoire relies on the use of unusual ___1___. Beyond this aspect of 
the band's sound, each band member experiments within his wide musical scope. ___2___ magazine described 
Chancellor's bass playing as having a "thick midrange tone, guitar-style techniques, and elastic versatility".
Completing the band's ___3___ section, drummer Carey uses polyrhythms, tabla-style techniques, and the incorporation 
of custom electronic drum pads to trigger samples, such as prerecorded tabla and octoban sounds. The band has named 
the group ___4___ as an influence on its development, but the most-publicized influence is progressive rock pioneer 
group ___5___. Other reported influences of the band include ___6___, Helmet, ___7___ and Jane's Addiction.'''
hardAnswers = ['time signatures', 'Bass Player', 'rhythm', 'Melvins', 'King Crimson', 'Rush', 'Faith No More']
hardBlanks = ['___1___', '___2___', '___3___', '___4___', '___5___', '___6___', '___7___']

# asks for the players name and welcomes them to the quiz -------------------------------------------------------------
name = raw_input('Please type your name: ')

# delay and clear screen function -------------------------------------------------------------------------------------
def timeDelay():
	import time
	delay = 1
	count = 1
	while count > 0:
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

# takes one input to determine what level to set the gameData variables to based on user input ------------------------
def setGameData(level):
	if level == 'easy':
		gameData = [easyText, easyAnswers, easyBlanks]
	elif level == 'medium':
		gameData = [mediumText, mediumAnswers, mediaumBlanks]
	else:
		level == 'hard'
		gameData = [hardText, hardAnswers, hardBlanks]
	return gameData

# takes 3 inputs and diplays the text when the player wins ------------------------------------------------------------
def playerWon(attemptsLeft, gameText):
	clearScreen()
	print gameTitle + "\nWay to go " + name + ", you finished the quiz with " + str(attemptsLeft) + " attempts left!!!\n\n" + gameText + "\n"

# takes 3 inputs and displays the text when the player looses ---------------------------------------------------------
def playerLost(level, attemptsLeft, gameText):
	clearScreen()
	print gameTitle + "\nThis is the " + level + " quiz. You have " + str(attemptsLeft) + " guesses left for this quiz.\n\n" + gameText + '\n\nSorry ' + name + ', you answered incorrectly too many times. Game Over!'

# main game function takes user input and checks if it's a valid answer and replaces the blank with answer
# from the gameAnswer list until the player successfully fills in the blanks, or fails the quiz -----------------------
def playGame():
	level, attemptsLeft, index = setLevel(), 5, 0
	gameText, gameAnswers, gameBlanks = setGameData(level)[0], setGameData(level)[1], setGameData(level)[2]
	while attemptsLeft > 0:
		timeDelay()
		if index < len(gameBlanks):
			print gameTitle + "\nThis is the " + level + " quiz. You have " + str(attemptsLeft) + " guesses left " + name + ".\n\n" + gameText
			userInput = raw_input("\nPlease type you answer for " + gameBlanks[index] + ": ").lower()
			if userInput == gameAnswers[index].lower():
				print "\nThat's right!"
				gameText, index = gameText.replace(gameBlanks[index], gameAnswers[index]), index + 1
			else:
				print "\nSorry " + name + ", that is incorrect, please try again."
				attemptsLeft -= 1
		else:
			playerWon(attemptsLeft, gameText)
			return
	playerLost(level, attemptsLeft, gameText)

# Starts the Game -----------------------------------------------------------------------------------------------------
playGame()
