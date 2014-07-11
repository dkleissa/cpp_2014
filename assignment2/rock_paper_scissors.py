# Import the random module
import random

# Fill in the missing code! 
# Sections labeled TODO need to be completed before the program will run


################
#  Functions   #
################
def throw():
	# TODO: get a random number between 1 and 3
	choice = 

	# TODO: Write an if statement that REASSIGNS the variable 'choice' equal to:
	# 'rock' if choice == 1
	# 'paper' if choice == 2
	# 'scissors' if choice == 3


	print "The computer picked %s" % (choice)
	return choice

def check_choice(choice):

	# TODO: You need to write an if statement that returns True when the player has
	# entered a valid string ('rock', 'paper', 'scissors')
	# If they did not enter a valid string it should return False and print the valid things:
	# print "Invalid input. Type either \'rock\', \'paper\', \'scissors\', or \'quit\'"


def evaluate(choice):

	# Get the computer's choice
	computer_choice = throw()

	# TODO: Make a complex if statement to evaluate the user and compute choices
	# If the choices are equal, print "It is a tie, Try again!"
	# Otherwise, decide if the user won or lost, and print "You win!" or
	# "You lose!"


################
# Main Program #
################


# Print instructions for the game
print 'It is time for some rock, paper, scissors!'
print 'Type your choice as either \'rock\', \'paper\', or \'scissors\''
print 'Type \'quit\' to end the game!'

# Game loop
while True:
	# Print a blank line to make things look nicer
	print "" 

	# TODO: Ask the user to make a choice
	player_choice = 

	# TODO: Make sure the text the player entered is all lowercase
	player_choice = 
	
	# TODO: Add an IF statement to check if the user wants to quit
	# If they do, break out of the loop

	# Check the player's choice to make sure they typed something valid
	# If they did (check_choice returns True) then evaluate their choice
	if check_choice(player_choice) == True:
		evaluate(player_choice)
	
	
# TODO: Say Good bye!

