# Author: Luna Brown
#

# Modules
import sys
import time


# Time delay variables
delay1 = 0.8
delay2 = 0.55
delay3 = 0.08


# Dialogue choice functions
def whoAreYou():
  print()
  print("I am an AI designed by CompanyInc.")



# Function to start the game
def intro():
  playerName = input(("""What would you like me to refer to you as? 
  : """))
  time.sleep(delay2)
  print()
  print("Hello "+playerName+".")
  time.sleep(delay2)
  print()
  print("That is a wonderful name.")
  time.sleep(delay2)
  print()
  print("I am Polly!")
  time.sleep(delay2)
  print()
  whoAreYouI = input(("""(1) Who are you Polly?
  : """))
  if whoAreYouI == '1':
    whoAreYou()
 

# Working title screen
print("""


       _____________
    __|             |___
  _|           _____    |_          ____        ____
 |            |  .  |     |        / __ \____  / / /_  __
 |            |_____|     |       / /_/ / __ \/ / / / / /      
 |               _______  |      / ____/ /_/ / / / /_/ /
 |              |       \·|     /_/    \____/_/_/\__  / 
 |             |         \|                     /____/
 |____________|


""")

time.sleep(delay1)

# Initiating Polly
initiatePolly = (input(""" 
INSTRUCTIONS: Type the number in parenthesis to choose that option

Would you like to initiate Polly?

(1) Y
(2) N
 : """))

if initiatePolly == '1':
  intro()
elif initiatePolly == '2':
  print("Have a nice day.")

