import pygame 
import random 

BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0)

class game():
    def __init__(self):
        self.board = gameboard()
        #self.gameloopflag = gameloopflag
    def play_game():
        #for...
#endclass

class gameboard():
    def __init__(self):
        self.dice = dice(6)
        self.player_list = []
        p1 = player(0, BLUE)
        p2 = player(0, YELLOW)
        self.player_list.add(p1) # do you need to define the player_list as smth first
        self.player_list.add(p2)
        self.snake_list = snake_list
        self.ladder_list = ladder_list
#end class

class gateways():
    def __init__(self, enterpos, exitpos):
        self.enterpos = enterpos
        self.exitpos = exitpos
    #getter functions for start and end positions of gateways
    def getstartposition(self):
        return self.enterpos
    def getendposition(self):
        return self.exitpos
#end class

#when create a snake in main program
#s = snake()
#s.end = 12
#s.start = 32
#s_list.append(s)

class snakes(gateways):
    def __init__(self):
        super().__init__() #this takes attributes from the parent class
        def createladders():
            f = open('snake.txt','r')
            data = f.read()
            f.close()
            t = data.split(",")
            for c in t:            
                f = t(c).split(":")
                #instantiate snakes(enterpos, exitpos)
                snake = snakes(f(0), f(1))
                snake_list.append(snake)
            #next - change names to snakes
#end class

class ladders(gateways):
    def __init__(self):
        super().__init__(self)
    def createladders():
        f = open('ladder.txt','r')
        data = f.read()
        f.close()
        t = data.split(",")
        for c in t:            
            f = t(c).split(":")
            ladder = ladders(f(0), f(1))
            ladder_list.append(ladder)
        #next

#end class

class player():
    def __init__(self, pos, colour):
        self.pos = pos
        self.colour = colour
    #getter and setter functions for position of player(s)
    def setposition(self):
        return self.pos
    def getposition(self):
        return self.pos
#end class

class dice():
    def __init__(self, numberoffaces):
        self.numberoffaces = numberoffaces 
    def diceroll(self):
        #roll the dice
        result = random.randrange(1, self.numberoffaces)
        #return the result
        return result 
    #end procedure
#end class

#Initialise global variables
snake_list = []
ladder_list = []


#next steps:
    #create snake list from I/O values
    #do public play game_()
    







