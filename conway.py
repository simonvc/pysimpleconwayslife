from random import choice
import code
# import psyco # Uncommenting these lines makes the simulation run about 2x as fast 
# psyco.full()

class World:
  def __init__(self, size_x=80, size_y=80):
    self.size=(size_x,size_y)
    self.world={}
    for pos in self.scope():
      self.world[pos]=0

  def scope(self):
    return ((x,y) for x in range(self.size[0]) for y in range(self.size[1]))

  def get(self, pos):
    """ Takes a tuple and returns 0/1. Cells outside our grid are considered dead. """
    try:
      return self.world[pos]
    except KeyError:
      return 0

  def near(self, pos): #todo continuation
    """Return the number of adjacent cells that are Alive, ignoring the cell itself"""
    cells_around=[ # These are the cells around our hero, ignoring the center.
        (-1,-1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0),  (1, 1)
        ]
    adjacent=[(cell[0]+pos[0], cell[1]+pos[1]) for cell in cells_around]
    #todo store a list of cells where near=0 and skip them next time
    count_near=sum( [self.get(cell) for cell in adjacent] )
    return count_near

  def conway(self, pos):
    """Applies the conway rule, returning either 0 or 1 depending on the number of neighbours alive"""
    if self.get(pos): #if the cell is alive 
      return [0, 0, 1, 1, 0, 0, 0, 0, 0][self.near(pos)] #it stays alive if 2 or 3 neighbours are alive 
    else: #if the cell is dead 
      return [0, 0, 0, 1, 0, 0, 0, 0, 0][self.near(pos)]# it comes alive if exactly 3 neighbours are alive

  def update(self):
    newworld={}
    for pos in self.world:
      newworld[pos]=self.conway(pos)
    self.world=newworld

  def randomize(self):
    for pos in self.world:
      self.world[pos]=choice([1,0])

# End World Definition


def add_pattern(world, pattern, pos):
  positions=[p.split(",") for p in pattern.split(" ")]
  for x,y in positions:
    world.world[(int(x)+pos[0],int(y)+pos[1])]=1

if "__main__" in __name__:
  #run test
  print("You may want to run 'python pshow.py' for visual output if you have pyglet installed")
  import unittest
  from conwaytests import ConwayTestCase
  unittest.main()
