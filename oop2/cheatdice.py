from random import randint

class Player:
  def __init__(self):
    self.dice = []

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3):
      self.dice.append(randint(1,6))

  def get_dice(self):
    return self.dice

class Cheat_Swapper(Player):
  def cheat(self):
    self.dice[-1] = 6 # sets the last roll to 6 (even if it already was)

class Cheat_Loaded_Dice(Player):
  def cheat(self):
    i = 0
    while i < len(self.dice):
      if self.dice[i] < 6: # if i<3 and dice roll<6
        self.dice[i] += 1 # this adds 1 to the roll
      i += 1

class Cheat_Like_Brother(Player);
    def cheat(self):
        if sum(self.dice) < 10:
            sum(self.dice) += 2
