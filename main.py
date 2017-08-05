
#Author:  Rudy Faile 
#Version: 4.0
#Date:    08/02/17
import random
import time
from datetime import date
#----------------Display build version and local time---------------------
today = date.today()
build_version = 4.0
current_time = time.asctime( time.localtime( time.time()) )
print ("\n\nBuild Version:", str(build_version),"\nTime:", str(current_time), "\n\n")
#-------------------------------------------------------------------------

class Game:

	#Global Variables
	bankRoll = 0
	currentWager = 0
	lose = False
	point = 0 
	oddsAmount = 0

	def __init__(self):
		self.Game = Game

	def welcome(self):
		print ("***Welcome to Craps***")

	def rules(self):
		displayRules = Game.ask_yes_no("Would you like to see the rules?")
		if displayRules == 'y' or displayRules == 'yes':
			print ("Rules Go Here")
			input ("Press any key to continue.")
		else:
			pass
		Game.bankRoll = 1000
		print('You have been assigned an initial bankroll of $1,000, good luck!')
		

	def comeOutRoll(self):
		print ("How Much Would you Like to Wager on the Pass Line?")
		print ("Current Bankroll: $", Game.bankRoll)
		Game.currentWager = int(input("Wager: $"))
		input ("Press any key to roll the dice.")
		Game.point = Game.dice(self)
		print ('The roll is:', Game.point)
		if Game.point == 2 or Game.point == 3 or Game.point == 12:
			print ("Craps,",Game.point,"Craps... Line Away.")
			Game.bankRoll == Game.bankRoll - Game.currentWager
			print ("You Lose your bet of $", Game.currentWager, "and now have a total of $", Game.bankRoll)
		elif Game.point == 7 or Game.point == 11:
			print ("Winner,",Game.point,"!! Pay the Line!")
			Game.bankRoll == Game.bankRoll + Game.currentWager
			print ("You Win your bet of $", Game.currentWager, "and now have a total of $", Game.bankRoll)
		else:
			Game.secondPhase(self)
			#should i subtract the current wager from the bankroll here i wonder?


	def secondPhase(self):
		print ("The point is:", Game.point)
		print ("Would you like to Take odds on your",Game.point,"?")
		odds = Game.ask_yes_no("Take odds? : ")
		if odds == 'y' or odds =='yes':
			print ("How much you would like would you like to bet behind your", Game.point,"? (Up to 5x): ")
			oddsAmount = int(input("Odds Bet: $"))
			if oddsAmount > game.currentWager * 5:
				print("The Maximum amount of odds you can place behind the", Game.point,"is $", game.currentWager * 5)
				input("Press any key to try again.")
				Game.secondPhase(self)
			else:
				Game.oddsAmount = oddsAmount
				Game.streaming_roll(self)
				#put something here to not let them be able to bet more than they have in the bank
		else:
			Game.oddsAmount = 0
			input("Press any key to roll the dice.")
			Game.streaming_roll(self)


	def streaming_roll(self):
		stream = Game.dice(self)
		if stream == Game.point:
			print ("Winner! You Rolled the point of", Game.point)
			print ("You win your initial bet of", Game.currentWager,"plus your odds bet of", Game.oddsAmount)
			Game.odds(Game.point)
			print ("Total Win: $",Game.currentWager,"(initial wager pays 1:1) and $",Game.oddsAmount,"from your odds on the", Game.point)
			Game.bankRoll += Game.currentWager
			Game.bankRoll += Game.oddsAmount
			print ("Total Bankroll:", Game.bankRoll)
			input("Press Any Key to Continue.")
		elif stream == 7:
			print ("Oh dear, big red. Seven OUT, line away.")
			print ("You lose your initial bet of", Game.currentWager,"plus your odds bet of", Game.oddsAmount)
			Game.odds(Game.point)
			print ("Total Loss: $",Game.currentWager,"(initial wager) and $",Game.oddsAmount,"from your odds on the", Game.point)
			Game.bankRoll -= Game.currentWager
			Game.bankRoll -= Game.oddsAmount
			print ("Total Bankroll: $", Game.bankRoll)
			input("Press Any Key to Continue.")
		else:
			input ("Press any key to roll again.")
			Game.streaming_roll(self)


	def dice(self):
		die1 = random.randint(1,6)
		die2 = random.randint(1,6)
		dice = die1 + die2
		print ("You roll a", die1,"and", die2,"for a total of", dice)
		return dice

	def checkBroke(self):
		if Game.bankRoll <= 0:
			lose = True
		else:
			pass

	def loseGame(self):
		print ('Oh dear, you are out of money.')
		Game.bankRoll = 0 
		Game.currentWager = 0 
		playAgain = Game.ask_yes_no("Would You like to play again?")
		if playAgain == 'y' or playAgain == 'yes':
			intro = False
		else:
			quit()

	def ask_yes_no(question):
		response = None
		while response not in ("y", "n", "yes", "no"):
			response = input(question).lower()
			return response 

	def odds(calculation):

		if calculation == 4 or calculation == 10:
			Game.oddsAmount = (Game.oddsAmount * 2) + Game.oddsAmount
		elif calculation == 5 or calculation == 9:
			Game.oddsAmount = (Game.oddsAmount * 2) - (Game.oddsAmount / 2)
		elif calculation == 6 or calculation ==8:
			Game.oddsAmount = (Game.oddsAmount % 5) + Game.oddsAmount
		else:
			pass


'''
gameflow

welcome user / explain rules
phase one - assign money
phase two - Place bet / Come out Roll
phase three - Result of Come out Roll / Bet payoff, either assign point or redo come out roll - do they have money to continue?
phase four -  Point Phase of the game - Shooter either wins or loses
phase five - check if broke, restart phase two
'''
if __name__ == '__main__':
	game = Game()
	intro = True
	phase1 = True
	while intro:
		game.welcome()
		game.rules()
		intro = False
	while phase1:
		game.comeOutRoll()
	input('done')





