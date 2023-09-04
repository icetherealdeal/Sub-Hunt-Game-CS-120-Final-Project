# Class for depth charges
# Phase four will introduce depth charges
# By: Isaac Nguyen and Lura Ajdini
from graphics import *

class DepthCharge:
   # A depthcharge starts at the point given and falls at a constant rate.
   def __init__(self, center, win):
      # Remember win
      self.win = win
      # Draw an icon. If it has multiple parts put them in a list 
      # to make life easy
      self.center = center
      x, y = self.center.getX(), self.center.getY()
      self.d = Rectangle(Point(x-3, y), Point(x+3, y+5))
      self.d.setFill("red")
      self.d.setOutline("red")
      self.d.draw(self.win)
      self.velocity = 28

      # Set velocity  
      # (units are pixels per second, unless you changed the coords

   def move(self, timeStep):
      # The depthcharge drops by timeStep*velocity
      self.d.move(0, timeStep*self.velocity)
      self.center.move(0, timeStep*self.velocity)

   def pastBottom(self):
      # Return True if the charge has dropped off the bottom of the screen
      if self.d.getP2().getY() > 750:
         return True
      else:
         return False
         
   def undraw(self):
      # Undraw the icon(s)
      self.d.undraw()
