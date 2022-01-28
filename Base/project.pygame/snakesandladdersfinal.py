import pygame 
import random 
# -- Global Constants 
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0)
# -- Initialise PyGame
pygame.init() 
# -- Blank Screen 
size = (640,480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("My Window") 
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock() 

#game class
class game():
    def __init__(self):
        self.board = gameboard()
        self.gameloopflag = False
    
    def get_gameloopflag(self):
        return self.gameloopflag
    def play_game(self):
        for p in self.board.getplayerlist():
            #roll the dice
            r = self.board.dice.diceroll()
            p.pos = p.setposition(r)
            if p.pos > 100:
                p.pos = (100-(p.pos-100))
            #endif
            print(p.name, " is at ", p.pos, "after rolling", r)
            #end game if p.pos >= 100
            if p.pos == 100:
                self.gameloopflag = True
            #endif

            #check ladder
            for l in self.board.ladder_list:
                if p.pos == l.getstartposition():
                    p.pos = l.exitpos
                    print(p.name, " has reached a ladder. You are now at position ", p.pos)
                #end if

            #check snake
            for s in self.board.snake_list:
                if s.enterpos == p.pos:
                    p.pos = s.exitpos
                    print(p.name, " has angered a snake. You are now at position ", p.pos)
                #end if



        

#endclass


#gameboard class
class gameboard():
    def __init__(self):
        self.dice = dice(6)
        self.player_list = []
        #does this work - maybe should instantiate players outside class
        self.p1 = player(0, BLUE, "Momo")
        self.p2 = player(0, YELLOW, "Yuyu")
        self.player_list.append(self.p1)
        self.player_list.append(self.p2)
        self.snake_list = snake_list
        self.ladder_list = ladder_list
    #getter function for the playerlist
    def getplayerlist(self):
        return self.player_list
#end class

#gateways superclass
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

def createsnakes():
    f = open('snake.txt','r')
    data = f.read()
    f.close()
    t = data.split(",")
    for count in range (0,len(t)):            
        f = t[count].split(":")
        #instantiate snakes(enterpos, exitpos)
        snake = snakes(int(f[0]), int(f[1]))
        snake_list.append(snake)
    #next - change names to snakes

#snakes childclass
class snakes(gateways):
    pass

def createladders():
    f = open('ladder.txt','r')
    data = f.read()
    f.close()
    t = data.split(",")
    for count in range (0,len(t)):            
        f = t[count].split(":")
        ladder = ladders(int(f[0]), int(f[1]))
        ladder_list.append(ladder)
    #next
        
#ladder childclass
class ladders(gateways):
    pass


#end class

#player class
class player():
    def __init__(self, pos, colour, name):
        self.pos = pos
        self.colour = colour
        self.name = name
    #getter and setter functions for position of player(s)
    def setposition(self, rollnumber):
        return self.pos + rollnumber
    def getposition(self):
        return self.pos
#end class

#dice class
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
createladders()
createsnakes() 
g = game()


### -- Game Loop 
while not g.get_gameloopflag(): 
    g.play_game()
    
#End While - End of game loop 
pygame.quit()

#to do:
#solve the i/o creating snakes and ladders
#done loop
#solve when hits snake or ladder