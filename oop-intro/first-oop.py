from random import randint

class Player:
    #Constructor that declares self and initialized empty dice list
    def __init__(self):
    self.dice = []

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3):
      self.dice.append(randint(1,6)) # rolls and appends roll to empty list

  def get_dice(self): # shares what the dice rolled
    return self.dice

  def cheat_roll(self);
    self.dice = []
    while sum(self.dice) <= 5:
        for i in range (3)
            self.dice.append(randint(1,6))
# create two separate player objects
player1 = Player()
player2 = Player()
# each object uses the roll method
player1.roll()
player2.roll()

print("Player 1 rolled" + str(player1.get_dice())) # each object uses the get_dice method
print("Player 2 rolled" + str(player2.get_dice()))

if sum(player1.get_dice()) == sum(player2.get_dice()):
  print("Draw!")
elif sum(player1.get_dice()) > sum(player2.get_dice()):
  print("Player 1 wins!")
else:
  print("Player 2 wins!")

