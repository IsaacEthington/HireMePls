import random, string, statistics

from collections import Counter
from datetime import datetime

'''
This is a very basic simulation of a board game called 'Camel Up'.
I just did this because I wanted to see if it was broken.It's not too bad, but I still won using stats from this.
The game involves 'betting' on the winner or loser of a Camel race.
The camels can stack up on top of each other, and camels under them will move them.
This adds an element of uncertainty, as it is feasible for the losing camel to get lucky and ride the backs to victory.

This is just a simulation of the stacking and moving to get some basic statistics. 

In the real game, players have limited additional choices that can also affect the game.


ngames(number) will simulate n games, and give statistics about them.
gstats() Prints statistics stuff regarding the winners and losers and initial positions.
These run via command. 

'''


def rollColor():
    roll = [random.choice(colors) , randint(1, 3)]
    colors.remove(roll)
    return roll;

def avg(a):
    return float(sum(a))/len(a)

def reset():
    i = 0
    while i < 5:
            camels[i].reset()
            i = i+1
def firstTurn():
    i = 0;

    resetColors()

    i = 0
    while len(colors) > 0:
        #pick a color        
        roll = random.choice(colors)
        colors.remove(roll)
        space = random.randint(1,3)
        camels[roll].startingSpace = space
        camels[roll].currSpace = space
        camels[roll].startingHeight = 1
        camels[roll].currHeight = 1
        camels[roll].rolls = []
        camels[roll].rolls.append(space)
        
        j = 0;
       # print(camels[roll].name)
              
        #Figure out current Height 5 is top; and Position -- (1st, 2nd, 3rd...)
        while j < 5:
            if(j == roll):
                j = j
                #skip our guy
            else:
                if space == camels[j].startingSpace:
                    camels[roll].currHeight = camels[roll].currHeight + 1#height starts at 1 and goes up. if last to go, then can be 5
            j = j+1
        camels[roll].startingHeight = camels[roll].currHeight
    setPositions()
    i = 0
    while i < 5:
        camels[i].startingPos = camels[i].currPos
        i = i+1


def turn():
    resetColors()
    play = True
    while len(colors) > 0 and play:
        roll = random.choice(colors)
        colors.remove(roll)
        move = random.randint(1,3)
        #first check for future height
        i = 0
        rollheight = 1
        camels[roll].rolls.append(move)

        
        while i < 5:
            if camels[i].currSpace == camels[roll].currSpace + move:
                rollheight += 1
            i = i +1
            
        i = 0
        #check for dudes on top     
        while i < 5:
            #perhaps adding them to a list is bettwe, but lets do this easy loop instead
            if (camels[i].currSpace == camels[roll].currSpace) and (camels[i].currHeight > camels[roll].currHeight):                    
                camels[i].currSpace += move
                camels[i].currHeight = (camels[i].currHeight - camels[roll].currHeight) + rollheight
            i += 1
        camels[roll].currSpace += move
        camels[roll].currHeight = rollheight

        if camels[roll].currSpace >=16:
            play = False            
    setPositions()
    return play


    
    

            
def setPositions():
    i = 0
    while i < 5:
        camels[i].currPos = 1;
        i = i+1
    
    i = 0;
    while i < 5:
        j = 0;
        while j < 5:
            if j == i:
                j = j
            higherPos = (camels[i].currSpace < camels[j].currSpace) or ((camels[i].currSpace == camels[j].currSpace) and (camels[i].currHeight < camels[j].currHeight))
            if (higherPos):
                camels[i].currPos = camels[i].currPos + 1
                                
            j = j+1
        i = i+1;
                
        

           
def resetColors():
    colors.append(0)    
    colors.append(1)
    colors.append(2)
    colors.append(3)
    colors.append(4)

class games:
    
    def __init__(self):
        self.firstPlaceStartingHeight = []
        self.firstPlaceStartingSpace = []
        self.firstPlaceStartingPosition = []
        
        self.secondPlaceStartingHeight = []
        self.secondPlaceStartingSpace = []
        self.secondPlaceStartingPosition =[]
        
        self.lastPlaceStartingHeight =[]
        self.lastPlaceStartingSpace = []
        self.lastPlaceStartingPosition = []

        self.gamelengths = []

        


class camel:
    
    def __init__(self):
        self.name = 'name'
        self.startingHeight = -1
        self.startingSpace = -1
        self.startingPos = -1  
        self.currPos = -1
        self.currSpace = -1
        self.currHeight = 1
        self.rolls = []
    def reset(self):
        self.name = self.name
        self.startingHeight = -1
        self.startingSpace = -1
        self.startingPos = -1  
        self.currPos = -1
        self.currSpace = -1
        self.currHeight = 1
        self.rolls = []

def printCamel(c):
    print ('Name: ',c.name)
    print ('Starting Height: ',c.startingHeight)
    print ('Starting Space: ',c.startingSpace)
    print ('Starting Position', c.startingPos)
    print ('Current Position', c.currPos)
    print ('Current Space', c.currSpace)
    print ('Current Height', c.currHeight)
    print (c.rolls)
    

def printCamels():
    i = 0
    while (i < 5):
        print()
        printCamel(camels[i])
        i = i+1

def ngames(n):
    start=datetime.now()
    i = 0;
    while i < n:
        game()
        i = i+1
    print (datetime.now()-start)

    
def game():
    j = 0
    firstTurn()
    while(turn()):
        j = j+1
    #save winners and losers
    i = 0
    while i < 5:
        if (camels[i].currPos == 1):
            g.firstPlaceStartingHeight.append(camels[i].startingHeight)
            g.firstPlaceStartingSpace.append(camels[i].startingSpace)
            g.firstPlaceStartingPosition.append(camels[i].startingPos)
        if (camels[i].currPos == 2):
            g.secondPlaceStartingHeight.append(camels[i].startingHeight)
            g.secondPlaceStartingSpace.append(camels[i].startingSpace)
            g.secondPlaceStartingPosition.append(camels[i].startingPos)
        if (camels[i].currPos == 5):
            g.lastPlaceStartingHeight.append(camels[i].startingHeight)
            g.lastPlaceStartingSpace.append(camels[i].startingSpace)
            g.lastPlaceStartingPosition.append(camels[i].startingPos)
        i = i+1
    g.gamelengths.append(j)
    return j

def nturns(n):
    i = 1
    while (game() != n):
        i = i+1
    return i

def gprint():
    print("In First Place")
    print("Starting Height")
    print(g.firstPlaceStartingHeight)
    print("Starting Space")
    print(g.firstPlaceStartingSpace)
    print("Starting Position")
    print(g.firstPlaceStartingPosition)

    print("In Second Place")
    print("Starting Height")
    print(g.secondPlaceStartingHeight)
    print("Starting Space")
    print(g.secondPlaceStartingSpace)
    print("Starting Position")
    print(g.secondPlaceStartingPosition)


    print("In Last Place")
    print("Starting Height")
    print(g.lastPlaceStartingHeight)
    print("Starting Space")
    print(g.lastPlaceStartingSpace)
    print("Starting Position")
    print(g.lastPlaceStartingPosition)

def gstats():

    

    a1 = g.firstPlaceStartingHeight
    a2 = g.firstPlaceStartingSpace
    a3 = g.firstPlaceStartingPosition

    b1 = g.secondPlaceStartingHeight
    b2 = g.secondPlaceStartingSpace
    b3 = g.secondPlaceStartingPosition

    c1 = g.lastPlaceStartingHeight
    c2 = g.lastPlaceStartingSpace
    c3 = g.lastPlaceStartingPosition

    
    print(len(a1), "Games simulated")
    print(Counter(g.gamelengths).most_common())
    print("\nIn First Place")
    print("Starting Height")
    print("avg: ", statistics.mean(a1), "mode", statistics.mode(a1), "median: ",statistics.median(a1), "Standard Deviation: ", statistics.stdev(a1))
    print(Counter(a1).most_common())
    print("Starting Space")
    print("avg: ", statistics.mean(a2), "mode", statistics.mode(a2),"median: ",statistics.median(a2), "Standard Deviation: ", statistics.stdev(a2))
    print(Counter(a2).most_common())
    print("Starting Position")
    print("avg: ", statistics.mean(a3), "mode", statistics.mode(a3),"median: ",statistics.median(a3), "Standard Deviation: ", statistics.stdev(a3))
    print(Counter(a3).most_common())

    print("\nIn Second Place")
    print("Starting Height")
    print("avg: ", statistics.mean(b1), "mode", statistics.mode(b1),"median: ",statistics.median(b1), "Standard Deviation: ", statistics.stdev(b1))
    print(Counter(b1).most_common())
    print("Starting Space")
    print("avg: ", statistics.mean(b2), "mode", statistics.mode(b2),"median: ",statistics.median(b2), "Standard Deviation: ", statistics.stdev(b2))
    print(Counter(b2).most_common())
    print("Starting Position")
    print("avg: ", statistics.mean(b3), "mode", statistics.mode(b3),"median: ",statistics.median(b3), "Standard Deviation: ", statistics.stdev(b3))
    print(Counter(b3).most_common())



    print("\nIn Last Place")
    print("Starting Height")
    print("avg: ", statistics.mean(c1), "mode", statistics.mode(c1),"median: ",statistics.median(c1), "Standard Deviation: ", statistics.stdev(c1))
    print(Counter(c1).most_common())
    print("Starting Space")
    print("avg: ", statistics.mean(c2), "mode", statistics.mode(c2),"median: ",statistics.median(c2), "Standard Deviation: ", statistics.stdev(c2))
    print(Counter(c2).most_common())
    print("Starting Position")
    print("avg: ", statistics.mean(c3), "mode", statistics.mode(c3),"median: ",statistics.median(c3), "Standard Deviation: ", statistics.stdev(c3))
    print(Counter(c3).most_common())

    
    
          

print("Main Program")
c1 = camel()
c2 = camel()
c3 = camel()
c4 = camel()
c5 = camel()

c1.name = 'Red'
c2.name = 'Yellow'
c3.name = 'Green'
c4.name = 'Blue'
c5.name = 'White'
camels = [c1, c2, c3, c4, c5]

    
origList = [0,1,2,3,4]
colors = origList

space = 0
height= 1
init = [space, height]

g = games()


