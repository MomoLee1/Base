from telnetlib import theNULL
import pygame 
# -- Global Constants 
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0)
RED = (255,0,0)
# -- Initialise PyGame
pygame.init() 
# -- Blank Screen 
size = (640,480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("Sunrise Islands") 
# -- Exit game flag set to false 
done = False

map = ...
#game class for game object
class Game:
    def __init__(self):
        #define game class attributes
        self.player = Player()
        self.platform = platformlist
        self.movingplatform = movingplatformlist
        self.jump_pad = jumppadlist
        self.portal = portallist
        self.lava = lavalist
        Lives = 3
        Level = 1
    #run game method
    def playgame()
        pass #for now
#Player class for player object
class Player:
    #define player class attributes
    def __init__(self):
        self.x_coord: 0
        self.y_coord: -480
        self.x_speed = 3
        self.y_speed = 3
        self.height = 7
        self.width = 3
    #player update x_speed method
    def player_update_x_speed(self):
    #player update y_speed method
    def player_update_y_speed(self):
    #player update function (method)
    def update_function(self):
        `#player movement controls`- still need to implement grav (basically y direction stuff)
         if event.type == pygame.KEYDOWN: # - a key is down 
            if event.key == pygame.K_LEFT: # - if the left key pressed
                self.player_update_x_speed(-3) # speed set to -3
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
                self.player_update_x_speed(3) # speed set to 3
            elif event.key == pygame.K_UP: # - if the right key pressed
                self.player_update_y__speed(3) # speed set to 3
            elif event.key == pygame.K_DOWN: # - if the right key pressed
                #if player is standing on a platform
                self.player_update_y_speed(-3) # speed set to 3 
                #implement gravity  
        elif event.type == pygame.KEYUP: # - a key released 
            if event.key == left:
				self.player_update_x_speed(0)
			elif event.key == right:
				self.player_update_x_speed(0)
			elif event.key == up:
				self.player_update_y_speed(0)
			elif event.key == down:
				self.player_update_y_speed(0) # change this to uncrouches
			#endif		
        #endif

    
#spikemonster class for spikemonster objects
class Spikemonster:
    #define Spikemonster class attributes
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.height = 7
        self.width = 3

#jumpmonster class for jumpmonster objects
class Jumpmonster:
    #define Jumpmonster class attributes
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.height = 7
        self.width = 3
        self.y_speed = 3


        
        
