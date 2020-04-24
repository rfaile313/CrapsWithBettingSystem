# Author:  Rudy Faile
# Version: 4.2.0
# Date:    08/02/17
# License: MIT

import random
import ascii_dice
import ask_user as au

class Game:
    # Attributes
    __bank_roll = 1000
    __current_wager = 0
    __lost = False
    __point = 0
    __odds_amount = 0
    __keep_playing = True

    def __init__(self, __bank_roll=1000):  # We may add an option to choose initial money later
        self.Game = Game
        self.__bank_roll = __bank_roll

    def start(self):
        self.welcome()
        self.rules()
        while(self.__keep_playing):
            self.come_out_roll()
            self.keep_playing()

    @staticmethod
    def welcome():
        print("***Welcome to Craps***")

    @staticmethod
    def rules():

        if not au.ask_yes_no("Would you like to see the rules? (Yes/No)"):
            #TODO: rules don't work
            input("Press any key to continue.")
        else:
            print("\n1. Place a bet.\r\n2. Roll the dice.\r\n3. Get a 7 or 11, you win, get a 2, 3, or 12, you lost, "
                  "game over.\r\n4. Any other number, that's your point.\r\n5. Keep rolling until...\r\n6. ...you "
                  "repeat your point, and you win, game over.\r\n7. ...you get a 7, and you lost, game over.\n")

        print('You have been assigned an initial bankroll of $1,000, good luck!')

    def come_out_roll(self):
        self.check_broke()
        print("How Much Would you Like to Wager on the Pass Line?")
        print("Current Bankroll: ${}".format(self.__bank_roll))

        # Ask for user input
        bet = au.ask_for_value("Wager: $")
        while (bet > self.__bank_roll):
            bet = au.ask_for_value(
                "You don't have enough money for that! Please, enter a valid amount: ")

        self.__current_wager = bet

        input("Press any key to roll the dice.")
        self.__point = ascii_dice.dice()

        print('The roll is:', self.__point)

        if self.__point == 2 or self.__point == 3 or self.__point == 12:
            print("Craps,", self.__point, "Craps... Line Away.")
            self.__bank_roll = self.__bank_roll - self.__current_wager
            print("You lost your bet of $", self.__current_wager,
                  "and now have a total of $", self.__bank_roll)

        elif self.__point == 7 or self.__point == 11:
            print("Winner,", self.__point, "!! Pay the Line!")
            self.__bank_roll = self.__bank_roll + self.__current_wager
            print("You Win your bet of $", self.__current_wager,
                  "and now have a total of $", self.__bank_roll)

        else:
            self.second_phase()

    def second_phase(self):
        print("The __point is:", self.__point)
        print("Would you like to Take odds on your", self.__point, "?")

        take_odds = au.ask_yes_no("Take odds? (yes or no) : ")
        if not take_odds:
            self.__odds_amount = 0
            input("Press any key to roll the dice.")
            self.streaming_roll()
        else:
            print("How much you would like would you like to bet behind your",
                  self.__point, "? (Up to 5x): ")
            __odds_amount = au.ask_for_value("Odds Bet: $")

            if __odds_amount > self.__current_wager * 5:
                print("The Maximum amount of odds you can place behind the",
                      self.__point, "is $", self.__current_wager * 5)
                input("Press any key to try again.")
                self.second_phase()
            else:
                self.__odds_amount = __odds_amount
                self.streaming_roll()

        #self.keep_playing()

    
                # TODO: put something here to not let them be able to bet more than they have in the bank

    def streaming_roll(self):
        stream = ascii_dice.dice()

        if stream == self.__point:
            print("Winner! You Rolled the __point of", self.__point)
            print("You win your initial bet of", self.__current_wager,
                  "plus your odds bet of $", self.__odds_amount)
            self.odds(self.__point)
            print("Total Win: $", self.__current_wager, "(initial wager pays 1:1) and $", self.__odds_amount,
                  "from your odds on the", self.__point)
            self.__bank_roll += self.__current_wager
            self.__bank_roll += self.__odds_amount
            print("Total Bankroll: $", self.__bank_roll)
            input("Press Any Key to Continue.")
        elif stream == 7:
            print("Oh dear, big red. Seven OUT, line away.")
            print("You lost your initial bet of", self.__current_wager,
                  "plus your odds bet of $", self.__odds_amount)
            print("Total Loss: $", self.__current_wager, "(initial wager) and $", self.__odds_amount, "from your odds on the",
                  self.__point)
            self.__bank_roll -= self.__current_wager
            self.__bank_roll -= self.__odds_amount
            print("Total Bankroll: $", self.__bank_roll)
            input("Press Any Key to Continue.")
        else:
            input("Press any key to roll again.")
            self.streaming_roll()

    def check_broke(self):
        if self.__bank_roll <= 0:
            __lost = True
            self.__lost_game()

    def __lost_game(self):
        print('Oh dear, you are out of money.')
        self.__bank_roll = 0
        self.__current_wager = 0

        if au.ask_yes_no("Would You like to play again?"):
            exit(0)
            game = Game()
            game.start()
        else:
            quit(0)

    def odds(self, calculation):
        if calculation == 4 or calculation == 10:
            self.__odds_amount *= 2 / 1
        elif calculation == 5 or calculation == 9:
            self.__odds_amount *= 3 / 2
        elif calculation == 6 or calculation == 8:
            self.__odds_amount *= 6 / 5
        else:
            pass
        self.__odds_amount = int(round(self.__odds_amount))

    def keep_playing(self):
        self.__keep_playing = au.ask_to_keep_playing()
        if not self.__keep_playing:
            print('Thanks for playing! See ya!')
            exit(0)
            