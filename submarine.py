# Submarine class
# By: Isaac Nguyen & Lura Ajdini
from graphics import *
from random import random
from random import randrange
from depthcharge import DepthCharge

#EXTRA CREDIT: submarines move with random velocities

class Submarine:
   def __init__(self, y, win):
      # Remember a few window parameters
      self.rightEdge = win.width
      self.win = win
      # y is the depth of the sub so what lane each sub is in
      # x will randomly be (not quite) off-screen left or right

      # Create a submarine, it should have a 50-50 change of starting offscreen
      if random() < 0.5:
         self.velocity = randrange(1,7)
         self.submarines = Oval(Point(-100, 200+(y*100)-10), Point(0, 200+(y*100)+10))
         self.submarines.setFill("violet")
         self.submarines.setOutline("violet")
         self.submarines.draw(self.win)
      else:
         self.velocity = randrange(1,7)*-1
         self.submarines = Oval(Point(1200, 200+(y*100)-10), Point(1300, 200+(y*100)+10))
         self.submarines.setFill("lime")
         self.submarines.setOutline("lime")
         self.submarines.draw(self.win)
      # left and positive(l-to-r) velocity or offscreen right and negative
      # (r-to-l) velocity.  It should assign itself a point value based on depth.
      # It should assign itself a +/- velocity randomly but with in reasonable
      # limits and possibly based on depth 
      # If the sub has multiple pieces, put them in a list to save work
      
      
   def move(self, timeStep):
      # Move sub by timeStep*velocity
      self.submarines.move(timeStep*self.velocity, 0)

   def offScreen(self):
      # Return True if the sub has moved off-screen
      if self.velocity > 0: #Left to Right
         if self.submarines.getP1().getX() > 1200:
            return True
         else:
            return False
      else:
         if self.submarines.getP2().getX() < 0:
            return True
         else:
            return False
   
   def undraw(self):
      # Undraw all the pieces of the sub
      self.submarines.undraw()

   def points(self):
      if checkHit == True:
         points = points + 10

         
if __name__=="__main__":
   from subhuntGUI import GUI
   from subhuntgame import Game
   gui = GUI()
   myGame = Game(gui)
   myGame.play()
