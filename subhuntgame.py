# subhunt game
# By: Isaac Nguyen & Lura Ajdini
from destroyer import Destroyer
from submanager import SubManager
from depthcharge import DepthCharge
from graphics import *
#EXTRA CREDIT: depth charges allowed per time is 4. can reload once
#depthcharge hits the bottom

class Game:
   def __init__(self, gui):
      self.gui = gui
      self.depthcharges = []
      
   def play(self):
      fps = 60            # Frames per second
      timeRemaining = 30  # Seconds in game
      score = 0           # Initial score
      self.d = Destroyer(self.gui.win) #instance of Destroyer
      self.sm = SubManager(self.gui.win)

      #  MAIN EVENT LOOP, everything happens from here!!
      while timeRemaining > 0:

         # LOTS OF OTHER STUFF WILL GO HERE LATER
         k = self.gui.win.checkKey()
         if k == "Left":
            self.d.moveLeft()
         elif k == "Right":
            self.d.moveRight()
         elif k == "q":
            break
         elif k == "p":
            self.gui.win.getKey()
         elif k == "space":
            if len(self.depthcharges) < 4:
               self.depthcharges.append(DepthCharge(self.d.shipCenter(), self.gui.win))
         
         self.sm.moveSubs(1)
   
         

         dc = []
         for d in self.depthcharges:
            d.move(0.2)
            if d.pastBottom():
               d.undraw()
            else:
               dc.append(d)
         self.depthcharges = dc
            
         self.sm.checkHit(self.depthcharges)


         # Temporary scoring to test GUI scoring update
         score = score + self.sm.checkHit(self.depthcharges)
         self.gui.updateScore(score)

         # Update the time remaining  (this can stay)
         timeRemaining = timeRemaining - 1/fps
         self.gui.updateTimer(timeRemaining) #comment this out for now
         
         # Update screen and control loop speed 
         update(fps)


      self.gui.close()



if __name__=="__main__":
   from subhuntGUI import GUI
   gui = GUI()
   myGame = Game(gui)
   myGame.play()
