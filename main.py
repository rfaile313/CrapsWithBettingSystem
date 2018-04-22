# Author:  Rudy Faile
# Version: 4.0
# Date:    08/02/17
import random
import time
from datetime import date
import ascii_dice

# ----------------Display build version and local time---------------------
today = date.today()
build_version = 4.0
current_time = time.asctime(time.localtime(time.time()))
print("\n\nBuild Version:", str(build_version), "\nTime:", str(current_time), "\n\n")


# -------------------------------------------------------------------------

class Game:
    # Global Variables
    bank_roll = 0
    current_wager = 0
    lose = False
    point = 0
    odds_amount = 0

    def __init__(self):
        self.Game = Game

    @staticmethod
    def start():
        intro = True
        phase1 = True
        while intro:
            game.welcome()
            game.rules()
            intro = False
        while phase1:
            game.come_out_roll()
        input('done')

    @staticmethod
    def welcome():
        print("***Welcome to Craps***")

    @staticmethod
    def rules():

        if not Game.ask_yes_no("Would you like to see the rules?"):
            input("Press any key to continue.")
        else:
            print("\n1. Place a bet.\r\n2. Roll the dice.\r\n3. Get a 7 or 11, you win, get a 2, 3, or 12, you lose, "
                  "game over.\r\n4. Any other number, that's your point.\r\n5. Keep rolling until...\r\n6. ...you "
                  "repeat your point, and you win, game over.\r\n7. ...you get a 7, and you lose, game over.\n")

        Game.bank_roll = 1000
        print('You have been assigned an initial bankroll of $1,000, good luck!')

    @staticmethod
    def come_out_roll():
        print("How Much Would you Like to Wager on the Pass Line?")
        print("Current Bankroll: $", Game.bank_roll)

        # Ask for user input
        Game.current_wager = Game.ask_for_value("Wager: $")

        input("Press any key to roll the dice.")
        Game.point = Game.dice()

        print('The roll is:', Game.point)

        if Game.point == 2 or Game.point == 3 or Game.point == 12:
            print("Craps,", Game.point, "Craps... Line Away.")
            Game.bank_roll = Game.bank_roll - Game.current_wager
            print("You Lose your bet of $", Game.current_wager, "and now have a total of $", Game.bank_roll)

        elif Game.point == 7 or Game.point == 11:
            print("Winner,", Game.point, "!! Pay the Line!")
            Game.bank_roll = Game.bank_roll + Game.current_wager
            print("You Win your bet of $", Game.current_wager, "and now have a total of $", Game.bank_roll)

        else:
            Game.second_phase()

    @staticmethod
    def second_phase():
        print("The point is:", Game.point)
        print("Would you like to Take odds on your", Game.point, "?")

        take_odds = Game.ask_yes_no("Take odds? : ")
        if 'y' or 'yes' not in take_odds:
            Game.odds_amount = 0
            input("Press any key to roll the dice.")
            Game.streaming_roll()
        else:
            print("How much you would like would you like to bet behind your", Game.point, "? (Up to 5x): ")
            odds_amount = Game.ask_for_value("Odds Bet: $")

            if odds_amount > Game.current_wager * 5:
                print("The Maximum amount of odds you can place behind the", Game.point, "is $", game.current_wager * 5)
                input("Press any key to try again.")
                Game.second_phase()
            else:
                Game.odds_amount = odds_amount
                Game.streaming_roll()

                # TODO: put something here to not let them be able to bet more than they have in the bank

    @staticmethod
    def streaming_roll():
        stream = Game.dice()

        if stream == Game.point:
            print("Winner! You Rolled the point of", Game.point)
            print("You win your initial bet of", Game.current_wager, "plus your odds bet of $", Game.odds_amount)
            Game.odds(Game.point)
            print("Total Win: $", Game.current_wager, "(initial wager pays 1:1) and $", Game.odds_amount,
                  "from your odds on the", Game.point)
            Game.bank_roll += Game.current_wager
            Game.bank_roll += Game.odds_amount
            print("Total Bankroll: $", Game.bank_roll)
            input("Press Any Key to Continue.")
        elif stream == 7:
            print("Oh dear, big red. Seven OUT, line away.")
            print("You lose your initial bet of", Game.current_wager, "plus your odds bet of $", Game.odds_amount)
            print("Total Loss: $", Game.current_wager, "(initial wager) and $", Game.odds_amount, "from your odds on the",
                  Game.point)
            Game.bank_roll -= Game.current_wager
            Game.bank_roll -= Game.odds_amount
            print("Total Bankroll: $", Game.bank_roll)
            input("Press Any Key to Continue.")
        else:
            input("Press any key to roll again.")
            Game.streaming_roll()

    @staticmethod
    def dice():
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice = die1 + die2
        print("You roll a", die1, "and", die2, "for a total of", dice)
        print(ascii_dice.dice[die1 - 1])
        print(ascii_dice.dice[die2 - 1], '\n')

        return dice

    @staticmethod
    def check_broke():
        if Game.bank_roll <= 0:
            lose = True

    def lose_game(self):
        print('Oh dear, you are out of money.')
        Game.bank_roll = 0
        Game.current_wager = 0

        if Game.ask_yes_no("Would You like to play again?"):
            intro = False
        else:
            quit(0)

    def ask_yes_no(question):
        response = None

        expected_responses = ('no', 'n', 'yes', 'y')

        while response not in expected_responses:
            response = input(question).lower()

            # Error message
            if response not in expected_responses:
                print('Wrong input please <yes/no>')

        if response is 'yes' or 'y':
            return True
        else:
            return False

    def ask_for_value(question):
        """The solution for asking for a integer value without using exceptions """

        answer = ""

        while not answer.isdigit():
            answer = input(question)

            # Error message
            if not answer.isdigit():
                print("Input must be a number!")
            else:
                # Cast for answer
                return int(answer)

        return answer

    def odds(calculation):
        if calculation == 4 or calculation == 10:
            Game.odds_amount *= 2 / 1
        elif calculation == 5 or calculation == 9:
            Game.odds_amount *= 3 / 2
        elif calculation == 6 or calculation == 8:
            Game.odds_amount *= 6 / 5
        else:
            pass
        Game.odds_amount = int(round(Game.odds_amount))


'''
gameflow

welcome user / explain rules
phase one - assign money
phase two - Place bet / Come out Roll
phase three - Result of Come out Roll / Bet payoff, either assign point or redo come out roll - do they have money to continue?
phase four -  Point Phase of the game - Shooter either wins or loses
phase five - check if broke, restart phase two.
'''

if __name__ == '__main__':

    try:
        game = Game()
        game.start()
    except KeyboardInterrupt:
        print('\nGamed ended by user!')
        # TODO: Maybe a little game summary here
        # This is a good idea, perhaps roll and win/loss history!
