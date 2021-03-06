import pygame 
import random 

#initialise colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0)

#game class
class game():
    def __init__(self):
        self.board = gameboard()
        #self.gameloopflag = gameloopflag
    
    
    def play_game(self):
        for p in self.board.getplayerlist():
            #roll the dice
            r = self.board.dice.diceroll()
            p.pos = p.setposition(r)
            print(p.name, " is at ", p.pos)
            #end game if p.pos >= 100
            if p.pos >= 100:
                pygame.quit()
            #endif

            #check ladder
            for l in self.board.ladder_list:
                if l.enterpos == p.pos:
                    p.pos = l.exitpos
                    print("You have reached a ladder. You are now at position ", p.pos)
                #end if

            #check snake
            for s in self.board.snake_list:
                if s.enterpos == p.pos:
                    p.pos = s.exitpos
                    print("You have angered a snake. You are now at position ", p.pos)
                #end if



        

#endclass


#gameboard class
class gameboard():
    def __init__(self):
        self.dice = dice(6)
        self.player_list = []
        #does this work - maybe should instantiate players outside class
        self.p1 = player(0, BLUE, "Momo")
        self.p2 = player(0, YELLOW, "You")
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

#snakes childclass
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

#ladder childclass
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

    
g = game()
g.play_game()






