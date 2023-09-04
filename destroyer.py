# destroyer class
# By: Isaac Nguyen & Lura Ajdini

from graphics import *
# EXTRA CREDIT: destroyer stops at the boundaries of the window exactly
# the water line for the destroyer is at y = 150 and it can

class Destroyer:
   def __init__(self,win):
      # Set up some constants
      self.win = win
      self.step = 20                        # Pixels to move each move
      centerX = self.X = win.getWidth()/2   # Center of window

      # move right/left as long as self.X isn't passing a bounding point
      # Draw a destroyer centered in window
      # If it has more than one shape, put them in a list for ease of 
      # manipulation
      # self.marker = [r1, r2, r3, r4, l1, l2]
         #for obj in self.marker:
            #obj.move(self.step, 0)
      
      self.ship = Rectangle(Point(500,100), Point(700,150))
      self.ship.setFill("black")
      self.ship.setOutline("gray")
      self.ship.draw(self.win)
         
   def moveLeft(self):
      # Move destroyer one step left AND adjust centerX 
      dx, dy = 0, 0
      minX = 0
      cX = self.ship.getCenter().getX()
      if (cX - 100) >= minX:
         dx = self.step * -1
         self.ship.move(dx, 0)
      else:
         if (cX + 100) <= minX:
            dx = self.step
            self.ship.move(dx, 0)
      
   def moveRight(self):
      # Move destroyer one step right AND adjust centerX 
      dx, dy = 0, 0
      maxX = 1200
      cX = self.ship.getCenter().getX()
      if (cX + 100) <= maxX:
         dx = self.step
         self.ship.move(dx, 0)
      else:
          if (cX - 100) >= maxX:
            dx = self.step * -1
            self.ship.move(dx, 0)

   def shipCenter(self):
      
      center = Point(self.ship.getP2().getX() - 100, self.ship.getP2().getY())
      return center
      

      
if __name__=="__main__":
   from subhuntGUI import GUI
   from subhuntgame import Game
   gui = GUI()
   myGame = Game(gui)
   myGame.play()
