# The GUI for the final project in CS120-01 Fall 2019
# The game is subhunt
# By: Isaac Nguyen and Lura Ajdini
from graphics import *

#EXTRA CREDIT: when clicking the screen, old text disappears and new text appears
#EXTRA CREDIT: added control help on the right side of the screen
#EXTRA CREDIT: tutorial text is bolded and set Face "courier"
#EXTRA CREDIT: different lane colors in a loop

class GUI:
   def __init__(self):
      # The window
      # Open a window (1200x800 max) using autoflush=False
      # (You may modify the next line)
      self.win = GraphWin("Submarine Hunt - CS120 Fall 2019",1200,800,autoflush=False)
      #self.win.setCoords(0, 800, 1200, 0)
      # Instructions,score,time Texts
      # Three to five text objects for score, time and instructions
      # Inital message should be "Click to Begin Game"

      self.score = Text(Point(1150, 50), "0")
      self.score.draw(self.win)

      self.points = Text(Point(1150, 30), "Points")
      self.points.draw(self.win)

      self.timer = Text(Point(50, 50), "")
      self.timer.draw(self.win)

      self.timerTitle = Text(Point(50, 30), "Time Remaining")
      self.timerTitle.draw(self.win)
      
      self.instructions = Text(Point(600, 50), "Click to begin game")
      self.instructions.setTextColor("magenta")
      self.instructions.draw(self.win)

      self.prompt = Text(Point(600, 70), "Bomb the submarines! You only have 4 bombs at a time.")
      self.prompt.setStyle("italic")

      self.tutorial1 = Text(Point(900, 50), "Lkey=left, Rkey=right")
      self.tutorial1.setStyle("bold")
      self.tutorial1.setFace("courier")
      self.tutorial1.draw(self.win)
      self.tutorial2 = Text(Point(900, 70), "P=pause, Q=quit, SPACE=drop bombs")
      self.tutorial2.setStyle("bold")
      self.tutorial2.setFace("courier")
      self.tutorial2.draw(self.win)

      self.countdown = Text(Point(600, 70), "10 seconds remaining! Destroy the submarines!")
      self.countdown.setTextColor("red")


      # Create lanes
      # Horizontal stripes below the water line to deliniate the sub "lanes"

      # Thicker line to delineate the water line/horizon
      laneColors = ["aqua","turquoise", "blue1", "blue2", "blue3", "blue4"]
      lc = 0
      for i in range(150, 651, 100):
         lane = Rectangle(Point(0, i), Point(1200,i+100))
         lane.setFill(laneColors[lc])
         lane.setOutline(laneColors[lc])
         lane.draw(self.win)
         lc = lc + 1
      laneBottom = Rectangle(Point(0, 750), Point(1200, 800))
      laneBottom.setFill("navy")
      laneBottom.setOutline("black")
      laneBottom.draw(self.win)
                          
      horizon = Line(Point(0, 150), Point(1200, 150))
      horizon.setOutline("red2")
      horizon.setWidth(1.5)
      horizon.draw(self.win)

      update()                 # Draw all your stuff
      

      if self.win.getMouse():
         self.prompt.draw(self.win)
         self.instructions.undraw()
         
      
   def close(self):
      # End gracefully as usual
      self.win.close()

   def updateScore(self, score):
      # Update the on-screen score
      self.score.setText(score)

   def updateTimer(self, time):
      # Update on-screen timer 
      self.timer.setText(int(time))
   
if __name__=="__main__":
   from subhuntgame import Game
   gui = GUI()
   myGame = Game(gui)
   myGame.play()
