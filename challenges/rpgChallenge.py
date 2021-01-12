#!/usr/bin/python3
""" Co-author: Gina Y Villegas
This game will allow you to move through the map
and prove your strength or smarts """
import random

def showInstructions():
  #print a main menu and the commands
  print('''
Smarter or Stronger Challenge 
==========================================
In life, you have to be smart or strong.
As you navigate through the game, you 
can choose math facts or exercise to earn 
inventory and beat the monster
==========================================

Commands:
  go [direction]
  get [math] or get [exercise]
  q to quit
''')



def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []
# an inventory which is available to earn
availableInventory = ['cookie', 'magic potion', 'key', 'extra life']
#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'north' : 'Pantry'
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room'
            }
         }
# math questions and answers in a dictionary
mathFacts = {
        '11 squared  = ' : '121',
        'Square root of 121' : '11',
        '125 / 5 = ' : '25',
        ' (9 * 8)/2 = ' : '32',
        '(18/6) * 120' : '360'
        }

# exercises to perform in lieu of math
exercise = ['60-second plank', '15 crunches', '15 squats', '15 lunges', '10 pushups']

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    # they can answer a math question to earn inventory
    if  move[1] == 'math':
      # ask the random math question 
      key = random.choice(list(mathFacts))
      # and store the answer for comparison
      rightAnswer = mathFacts[key]
      # get player answer
      playerAnswer = input(f'{key}')
      # and compare
      if playerAnswer == rightAnswer:
          # generate a random inventory item 
          prize = random.choice(list(availableInventory))
          #add the item to their inventory
          inventory += prize
          #display a helpful message
          print(prize + ' got!')
          #delete the item from the room
          availableInventory.remove(prize)
      #otherwise, if the item isn't there to get
      else:
          #tell them they can't get it
          print('You might have to be stronger...do 5 pushups')
    elif move[1] == 'exercise':
        print(random.choice(exercise))

  # Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
  
  ## If a player enters a room with a monster BUT HAS A COOKIE
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'cookie' in inventory:
    print('The monster takes your cookie and runs away! Whew!')
    del rooms[currentRoom]['item']
    inventory.remove('cookie')

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
