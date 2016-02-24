#Simple Craps Player v2.0 with betting
#Author: Rudy Faile
#Date: 1/31/16

import random
player_money = 1000

def greeting():
    print("""
 $$$$$$\                                               
$$  __$$\                                              
$$ /  \__| $$$$$$\  $$$$$$\   $$$$$$\   $$$$$$$\       
$$ |      $$  __$$\ \____$$\ $$  __$$\ $$  _____|      
$$ |      $$ |  \__|$$$$$$$ |$$ /  $$ |\$$$$$$\        
$$ |  $$\ $$ |     $$  __$$ |$$ |  $$ | \____$$\       
\$$$$$$  |$$ |     \$$$$$$$ |$$$$$$$  |$$$$$$$  |      
 \______/ \__|      \_______|$$  ____/ \_______/       
                             $$ |                      
                             $$ |                      
                             \__|                      
            $$\                                        
            $$ |                                       
            $$$$$$$\  $$\   $$\                        
            $$  __$$\ $$ |  $$ |                       
            $$ |  $$ |$$ |  $$ |                       
            $$ |  $$ |$$ |  $$ |                       
            $$$$$$$  |\$$$$$$$ |                       
            \_______/  \____$$ |                       
                      $$\   $$ |                       
                      \$$$$$$  |                       
                       \______/                        
      $$$$$$$\                  $$\                    
      $$  __$$\                 $$ |                   
      $$ |  $$ |$$\   $$\  $$$$$$$ |$$\   $$\          
      $$$$$$$  |$$ |  $$ |$$  __$$ |$$ |  $$ |         
      $$  __$$< $$ |  $$ |$$ /  $$ |$$ |  $$ |         
      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |         
      $$ |  $$ |\$$$$$$  |\$$$$$$$ |\$$$$$$$ |         
      \__|  \__| \______/  \_______| \____$$ |         
                                    $$\   $$ |         
                                    \$$$$$$  |         
                                     \______/ 
    """)
    input ("Press Enter to begin")

def make_bet():
    global player_money
    global bet_amount
    print ("Money =", '$',player_money)
    while True:
        try:
            bet_amount = bet_amount = int(input("How much would you like to wager on the pass line?"))
            break
        except ValueError:
            print ("Try again")
            make_bet()
    if bet_amount > player_money:
        print("You don't have that much!")
        make_bet()
    else:
        player_money = player_money - bet_amount
        print ("You wager $", bet_amount,"on the Pass Line and have $", player_money,"left in your bankroll,good luck!")
                
      

def roll_dice():
    
    input ("Press Enter to roll the dice:")

    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    print ("\nFirst Die =", die1)
    print ("Second Die =", die2,"\n")
    print ("Your Roll is", die1 + die2,"\n")
    
    dice = die1 + die2
    return dice

def come_out_roll():
    global point
    global dice
    dice = roll_dice()
    print ("\t\t** Come out Roll **\n")
    if dice == 7 or dice == 11:
        print ("** Winner,",dice,"- Pay the Line! **\n")
        point = None
        come_out_win()
        come_out_roll()
    elif dice == 2 or dice == 3 or dice == 12:
        print ("Craps,",dice,"! Pay the Don'ts...\n")
        point = None
        come_out_loss()
        come_out_roll()
    else:
        if dice == 4 or dice == 5 or dice == 6 or dice == 8 or dice == 9 or dice == 10:
            print ("""\t\t\t************************
                        **** The Point is""", dice,"""****
                        ************************\n""")
            point = dice
            odds_yes_no()
            return point

def streaming_roll():
    global player_money
    global odds_amount
    dice = roll_dice()
    if dice == point:
        print ("*** WINNER", dice, "Pay the Line! ***\n\n")
        if odds_amount > 0:
            odds_payout()
            print ("You win your initial bet of $", bet_amount,"and the odds bet of $",odds_amount)
            payout = odds_bet + bet_amount + player_money
            player_money = payout + player_money
            print ("For a total of: $",payout,"!")
            print ("You now have:   $",player_money)
        else:
            print ("You won your initial bet of", player_money,"and now have",player_money + player_money)
            player_money = player_money + player_money
    elif dice == 7:
        print ("""Seven out! Line Away....\n
               Oh, dear. Big Red. Better Luck Next time.\n\n""")
        if odds_amount <= 0:
            player_money = player_money - bet_amount
            are_you_broke()
            print ("You lost your bet and have", player_money,"remaining")
        elif odds_amount >= 0:
            player_money = player_money - bet_amount - odds_amount
            are_you_broke()
            print ("You lost your bet and have $", player_money,"remaining")
        else:
            game_over()
    else:
        streaming_roll()

def ask_yes_no(question):
    response = None
    while response not in ("y", "n", "yes", "no"):
        response = input(question).lower()
    return response

def odds_yes_no():
    print ("You have the option to take odds on the", point,"(Recommended).")
    odds = ask_yes_no("Take Odds? [Yes/No]")
    if odds == "y" or odds == "yes":
        odds_calculation()
    else:
        print ("You choose not to take odds.")
        odds_amount = 0
        pass

def odds_calculation():
    global odds_amount
    odds_amount = int(input("How much would you like to lay in odds? (Maximum of 5x your pass line bet)"))
    if odds_amount > bet_amount * 5:
        print ("You cannot lay more than 5x your bet as odds")
        odds_calculation()
    elif odds_amount > player_money:
        print ("You don't have enough money.")
        odds_calculation()
    else:
        print ("You have layed $",odds_amount,"on the",point,"behind your initial bet of $", bet_amount)
        return odds_amount
    
def odds_payout():
    global odds_bet
    odds_bet = ''
    if point == 4:
        odds_bet = odds_amount + odds_amount + odds_amount
        return odds_bet
    elif point == 5:
        odds_bet = odds_amount + odds_amount + (odds_amount / 2)
        return odds_bet
    elif point == 6:
        odds_bet = odds_amount + (odds_amount / 2)
        return odds_bet
    elif point == 8:
        odds_bet = odds_amount + (odds_amount / 2)
        return odds_bet
    elif point == 9:
        odds_bet = odds_amount + odds_amount + (odds_amount / 2)
        return odds_bet
    elif point == 10:
        odds_bet = odds_amount + odds_amount + odds_amount
        return odds_bet    


              
def come_out_loss():
    global player_money
    global bet_amount
    if dice == 2 or dice == 3 or dice == 12:
        loss = player_money - bet_amount
        player_money = loss
        if player_money > 0:
            print ("You lose your pass line bet and now have $",player_money,"remaining")
            make_bet()
        else:
            print ("\t\tYou're broke!!")
            game_over()

def come_out_win():
    global player_money
    global bet_amount
    if dice == 7 or dice == 11:
        win = player_money + bet_amount + bet_amount
        player_money = win
        print ("You win your pass line bet and now have $",player_money)
        make_bet()
        
    
def again():
    again = ask_yes_no("Do you want to play again? Yes/No: ")
    if again == "y" or again == "yes" and player_money > 0:
        main()
        

def are_you_broke():
    if player_money <= 0:
        print ("\t\tYou're broke!!")
        game_over()
    else:
        pass

def game_over():
    global player_money
    print ('''
   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|
  ''')
    loser = ask_yes_no("Restart game and restore chips to $1,000? [Yes/No]:")
    if loser == "y" or loser == "yes":
        player_money = 1000
        main()
    else:
        player_money = 1000
        pass
              
def main():
    greeting()
    make_bet()
    come_out_roll()
    streaming_roll()
    are_you_broke()
    again()
    
main()



input ("\nPress any Key to exit")
