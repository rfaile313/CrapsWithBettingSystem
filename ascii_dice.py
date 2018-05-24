import time
import random

dice1 = """
__________
|         |
|         |
|    O	  |
|         |
|_________|"""

dice2 = """
__________
|         |
|      O  |
|    	  |
|  O      |
|_________|"""

dice3 = """
__________
|         |
|      O  |
|    O	  |
|  O      |
|_________|"""

dice4 = """
__________
|         |
|  O   O  |
|    	  |
|  O   O  |
|_________|"""

dice5 = """
__________
|         |
|  O   O  |
|    O	  |
|  O   O  |
|_________|"""

dice6 = """
__________
|         |
|  O   O  |
|  O   O  |
|  O   O  |
|_________|"""

dice = (dice1, dice2, dice3, dice4, dice5, dice6)

# Seconds that the dice animation will be shown
animation_duration_time = 10
time_end = time.time() + animation_duration_time


def roll_dice():
    while time.time() < time_end:
        print(random.choice(dice))


time.sleep(1)
