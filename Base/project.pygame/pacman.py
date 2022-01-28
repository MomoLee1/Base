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
pygame.display.set_caption("My Window") 
# -- Exit game flag set to false 
done = False

map = [[1,1,1,1,1,1,1,1,1,1], 
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1], 
[1,1,0,1,1,1,1,1,0,1], 
[1,0,0,0,0,0,1,0,0,1],
[1,0,1,1,1,0,1,0,0,1],
[1,0,1,1,1,0,1,0,0,1], 
[1,0,1,1,1,0,1,0,0,1], 
[1,0,0,0,0,0,0,0,0,1], 
[1,1,1,1,1,1,1,1,1,1]]

class Game:
    def __init__(self):
        #create object: player
        self.player = Player(RED, 10, 10, 20, 20)
   
 
    def playgame(self):
        pass
## -- Define the class tile which is a sprite 
class Tile(pygame.sprite.Sprite): 
    # Define the constructor for tile 
    def __init__(self, color, width, height, x_ref, y_ref): 
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        self.rect = self.image.get_rect() 
        # Set the position of the player attributes
        self.rect.x = x_ref 
        self.rect.y = y_ref

## -- Define the class player which is a sprite 
class Player(pygame.sprite.Sprite): 
    # Define the constructor for tile 
    def __init__(self, color, width, height, x_ref, y_ref): 
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(RED) 
        self.rect = self.image.get_rect() 
        # Set the position of the player attributes
        self.rect.x = x_ref 
        self.rect.y = y_ref
        self.speedx = 0
        self.speedy = 0
    def player_set_speed(self, valx, valy):
        if valx > 0:
            if self.rect.x < 630:
                self.speedx = valx
        elif valx < 0:
            if self.rect.x > 0:
                self.speedx = valx
        else: 
            self.speedx = valx
        self.speedy = valy

        #end procedure
    # Class update function - runs for each pass through the game loop 
    def update(self): 
        if event.type == pygame.KEYDOWN: # - a key is down 
            if event.key == pygame.K_LEFT: # - if the left key pressed
                self.player_set_speed(-3, 0) # speed set to -3
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
                self.player_set_speed(3, 0) # speed set to 3
            elif event.key == pygame.K_UP: # - if the right key pressed
                self.player_set_speed(0, 3) # speed set to 3
            elif event.key == pygame.K_DOWN: # - if the right key pressed
                self.player_set_speed(0, -3) # speed set to 3   
        elif event.type == pygame.KEYUP: # - a key released 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                self.player_set_speed (0, 0) # speed set to 0


         #-- Check for collisions between pacman and wall tiles 
        player_hit_list = pygame.sprite.spritecollide(self, wall_list, False)
        for foo in player_hit_list: #if there's a hitlist then pacman can't move
            self.player_set_speed(0, 0) 
            self.rect.x = self.old_x
            self.rect.y = self.old_y
        #Run update function for all sprites
        self.old_x = self.rect.x
        self.old_y = self.rect.y

        self.rect.x = self.rect.x + self.speedx # this should be after controls? Edit for space invaders
        self.rect.y = self.rect.y - self.speedy

    #End Procedure
    #dont need for event for this update funciton because we have allspriteslist in main loop with the pygame for loop already connected to it
#now just need to add sth to loop, then change it for y values

# Create a list of all sprites 
all_sprites_list = pygame.sprite.Group() 
 
# Create a list of tiles for the walls 
wall_list = pygame.sprite.Group()
 
# Create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(10): 
 for x in range (10): 
    if map[y][x] == 1: # why does this flip the screen back?
        my_wall = Tile(BLUE, 20, 20, x*20, y *20) 
        wall_list.add(my_wall) 
        all_sprites_list.add(my_wall)

g = Game()
all_sprites_list.add(g.player)


# -- Manages how fast screen refreshes 
clock = pygame.time.Clock() 

### -- Game Loop 
while not done: 
     # -- User input and controls
    for event in pygame.event.get(): #ask/find out what this does exactly #or use: event = pygame.event.poll()
        if event.type == pygame.QUIT: 
            done = True 
        #End If
    #Next event
    
        
    all_sprites_list.update()    # why do i not need a for event for pacman to move?? - is it bc already got all the events happening in the for event...
    # -- Game logic goes after this comment
    # -- Screen background is BLACK 
    screen.fill (BLACK) 
    # -- Draw here 
    all_sprites_list.draw (screen)
    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()