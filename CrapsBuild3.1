#Author: Rudy Faile #Version Date: 3/15/16
import random
import time
from datetime import date
#----------------Display build version and local time---------------------
today = date.today()
build_version = 3.1
current_time = time.asctime( time.localtime( time.time()) )
print ("Build Version:", str(build_version),"\nTime:", str(current_time), "\n\n")
#-------------------------------------------------------------------------

class Game:
    ''' Constructs the game '''
    money = 1000
    bet = 0
    odds_amount = 0
    dice = []
    point = []
    payout = 0
    loss = 0 

    def __init__ (self):
        self.Game = Game
        print ("*** Welcome to Craps ***\n\n")

    def rules(self):
        rules = Game.ask_yes_no("Do you want to see the rules? [Yes/No]:")
        if rules == 'y' or rules == 'yes':
            print ("\nRules:\n")
            print ('''In this version of craps you have the option of making
a 'pass line bet' which is the most basic bet in craps.
You will begin with a bankroll of $1,000. Upon making 
a pass line bet, the come out roll will occur. If the 
dice land on '7' or '11', you win. If the dice land on 
'2' or '3' or '12', you lose. If the dice lands on any 
other number, that number will become the point. If you 
establish a point you will have the options to take odds
on that point, up to a maximum of 5x your pass line bet
which will pay out more than even money depending on 
which number is the point (4,10 pays 2 to 1) 
(5,9 pays 3 to 2) (6,8 pays 6 to 5)''')
        else:
            pass

    def ask_yes_no(question):
        response = None
        while response not in ("y", "n", "yes", "no"):
            response = input(question).lower()
        return response							
		
    def roll_dice(self):
        input ("\nPress Enter to Roll the Dice:")
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        Game.dice = die1 + die2
        print ("\nThe first die is:  %s" %die1)
        print ("The second die is: %s" %die2)
        print ("\n \t\t ** Your Roll is: %s **\n" % Game.dice)
        return Game.dice	

    def come_out_roll(self):
        Game.dice = Game.roll_dice(self)
        if Game.dice == 7 or Game.dice == 11:
            print ("WINNER! %s! Pay the line!" % (Game.dice ) )
            Game.money = Game.money + Game.bet + Game.bet
            print ("You win your initial bet of $%s and now have $%s total money!" % (Game.bet, Game.money) ) 
            Game.betting_options(self) 
        elif Game.dice == 2 or Game.dice == 3 or Game.dice == 12:
            print ("Craps, %s, you lose" % (Game.dice) )
            Game.money = Game.loss 
            print ("You lose your initial bet of $%s and now have $%s total money." % (Game.bet, Game.money) ) 
            Game.are_you_broke(self)
            Game.betting_options(self)
        else:
            print ("""\t\t\t************************
                   **** The Point is""", Game.dice,"""****
                   ************************\n""")
            Game.point = Game.dice
            Game.odds_yes_no(self)

    def streaming_roll(self):
        Game.dice = Game.roll_dice(self)
        if Game.dice == Game.point:
            print ("*** WINNER! %s! Pay the Line!! ***" % Game.point)
            if Game.odds_amount > 0:
                print ("You win your initial bet of $%s and the odds bet of $%s" % (Game.bet, Game.odds_amount) ) 
                Game.odds_payout(self) 
                Game.money = Game.money + Game.payout
                print ("\nFor a total of: $%s" % Game.payout)
                print ("\nYou now have:  $%s" % Game.money)
                Game.betting_options(self)
            else:
                Game.money = Game.money + Game.bet + Game.bet
                print ("You win your initial bet of $%s and now have $%s" % (Game.bet, Game.money) ) 
                Game.betting_options(self)
        elif Game.dice == 7:
            print ("""Seven out! Line Away....\n
                Oh, dear. Big Red. Better Luck Next time.\n\n""")
        else:
            Game.streaming_roll(self)


    def odds_yes_no(self):
        print ("\nYou have the option to take odds on the %s (Recommended)." % Game.dice)
        odds = Game.ask_yes_no("Take Odds? [Yes/No]:")
        if odds == "y" or odds == "yes":
            Game.odds_calculation(self)
        else:
            print ("You choose not to take odds.")
            Game.odds_amount = 0
            Game.streaming_roll(self)

    def odds_calculation(self):
        while True:
            try:
                Game.odds_amount = int(input("How much would you like to lay in odds? (Maximum of 5x your pass line bet)"))
                break
            except ValueError:
                print ("It must be a number")
        if Game.odds_amount > Game.bet * 5:
            print ("You cannot lay more than 5x your bet as odds")
            Game.odds_calculation(self)
        elif Game.odds_amount > Game.money:
            print ("You don't have enough money.")
            Game.odds_calculation(self)
        else:
            print ("You have layed $%s on the %s behind your initial bet of $%s \n" % (Game.odds_amount, Game.dice, Game.bet ) ) 
            Game.streaming_roll(self)

    def odds_payout(self):
        if Game.point == 4 or Game.point == 10:
            Game.payout = Game.odds_amount + Game.odds_amount + Game.odds_amount
        elif Game.point == 5 or Game.point == 9:
            Game.payout = Game.odds_amount + Game.odds_amount + (Game.odds_amount / 2) 
        elif Game.point == 6 or Game.point == 8:
            Game.payout = Game.odds_amount + (Game.odds_amount / 2) 

    def are_you_broke(self):
        if Game.money <= 0:
            Game.game_over(self)
        else:
            pass

    def betting_options(self):
        while True:
            try: 
                Game.bet = int(input("\nHow much would you like to wager on the pass line?  Wager: ") )
                break
            except ValueError:
                print ("It must be a number. Do not use letters or special characters.")
        if Game.bet > Game.money:
            print ("You don't have that much") 
            Game.betting_options(self)
        elif Game.bet <= 0:
            print ("You cannot wager nothing.")
            Game.betting_options(self)
        else:
            Game.loss = Game.money - Game.bet #for use later if player loses before Game.money is modified by the new calculation.
            Game.money = Game.money - Game.bet
            print ("\nYou wager $%s on the Pass Line and have $%s Remaining.\n" % (Game.bet, Game.money) )
            Game.come_out_roll(self)

    def game_over(self):
        print ("You are Broke!\n")
        again = Game.ask_yes_no("Do you want to play again? [Yes/No]:")
        if again == 'y' or again == 'yes':
            print ("\nResetting Player Money...........")
            Game.money = 1000
            Game.bet = 0
            Game.payout = 0 
            Game.dice = []
            Game.point = []
            print ("Money = $1,000")
            Game.betting_options(self)
        else:
            exit()


player1 = Game()
player1.rules()
player1.betting_options()

