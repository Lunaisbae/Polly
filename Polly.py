# Author: Luna Brown
#

# Modules
import sys
import time


# Time delay variables
delay1 = 1
delay2 = 0.55
delay3 = 0.08


# Dialogue choice functions
def whoAreYou():
  print()
  print("I am an AI designed by Flock Technologies with the purpose of assisting in menial tasks, and having human like interactions with my users.")
  moreInfo()

def moreInfo():
 moreInfo = input("""
 What else would you like to know?

 (1) Who created you?
 (2) What is Flock Technologies?
 (3) Close Polly
  : """)

 if moreInfo == '1':
   creator()

 if moreInfo == '2':
   infoFlock()

 if moreInfo == '3':
   print("closing")



def creator():
  print()
  print("I was created by a man named Orion Bouwman, on June 23rd 2037.")

  print()
  goBack = input("""
  (any key) back
  : """)
  moreInfo()


def infoFlock():
  print()
  print("FLock technologies was a company founded by **** ***** in 2020.")
  time.sleep(delay2)
  print("The headquarters are located in Rotterdam, with the current CEO being Otis Booles.")
  time.sleep(delay2)
  print("Flock Technologies goal is to drive artificial intelligence into the future.")
  time.sleep(delay1)

  print()
  goBack = input("""
  (any key) back
  : """)
  moreInfo()



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

time.sleep(delay2)

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

