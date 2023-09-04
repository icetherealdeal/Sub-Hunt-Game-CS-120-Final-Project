# Sub manager
# The submanager is the liaison between the various subs and the game engine
# By: Isaac Nguyen & Lura Ajdini
from submarine import Submarine
from random import random
from depthcharge import DepthCharge
#EXTRA CREDIT: depthcharge undraws once making contact with sub

class SubManager:
   def __init__(self, win):
      # Remember the window for later
      self.win = win
      self.makeProb = .0125  # Probability that a sub will be created each
                             # time around the event loop (if a lane is empty)
      # Create a list with the same number of entries and you have lanes
      # Set the entries to None for now
      self.subs = [None]*6
      
   def moveSubs(self, timeStep):
      # For each lane:
      #    If it has a sub move it and then delete it if it
      #                 has moved offscreen
      #    If the lane is empty decide whether to create a new sub
      for i in range(6):
         if self.subs[i] == None:
            if random() < self.makeProb:
               self.subs[i] = self.makeSub(i)
         else:
            self.subs[i].move(1)
            if self.subs[i].offScreen():
               self.subs[i].undraw()
               self.subs[i] = None

   def makeSub(self, lane):
      # Optional helper function to create a sub in the given lane
      # Using the Submarine constructor
      return Submarine(lane, self.win)

   def checkHit(self, dcList):
      score = 0
      for sub in self.subs:
         if sub != None:
            subP1X = sub.submarines.getP1().getX()
            subP2X = sub.submarines.getP2().getX()
            subP1Y = sub.submarines.getP1().getY()
            subP2Y = sub.submarines.getP2().getY()

            for depthcharge in dcList:
               dcCX = depthcharge.center.getX()
               dcCY = depthcharge.center.getY()
               if dcCX > subP1X and dcCX < subP2X and dcCY > subP1Y and dcCY < subP2Y:
                  sub.submarines.undraw()
                  sub = None
                  depthcharge.undraw()
                  score = score + 20
            
      score = score + 0
      return score
         
      
if __name__=="__main__":
   from subhuntGUI import GUI
   from subhuntgame import Game
   gui = GUI()
   myGame = Game(gui)
   myGame.play()
