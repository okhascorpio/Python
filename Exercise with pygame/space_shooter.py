# clear screen at Run
from pygame import surface
from os import system
import random
import pygame
from pygame.constants import K_LEFT, K_RIGHT
from pygame import mixer
pygame.init()

system("cls")
clock = pygame.time.Clock()

global winX, winY
winX = 600
winY = 800

#

# Title and icon ###################################################################
pygame.display.set_caption('PYGAME EXERCISE')
icon = pygame.image.load('pygame_exercises/data/spaceship.png')
pygame.display.set_icon(icon)

# Draw a window
screen = pygame.display.set_mode((winX, winY))

# Background #######################################################################
backgroundImg = pygame.image.load('pygame_exercises/data/background2.jpg')

# Background sound
Bullet_sound=mixer.Sound('pygame_exercises/data/laser.wav')
Explossion_sound=mixer.Sound('pygame_exercises/data/explosion.wav')
mixer.music.load('pygame_exercises/data/lazarus.wav')
mixer.music.play(-1)

def background():
    screen.blit(backgroundImg, (0, 0))

# Items on screen ###################################################################
class Item():

    def __init__(self, Path, X, Y, xRate, yRate, dir):
        self.Img = pygame.image.load(Path)
        self.rect = self.Img.get_rect()
        self.H = self.Img.get_height()
        self.W = self.Img.get_width()
        self.X = X
        self.Y = Y
        self.dir = dir  # change direction +1 or -1
        self.xRate = xRate    # rate at which it moves along x-axis
        self.yRate = yRate    # rate at which it moves along y-axis

    def drawItem(self, x, y):
        self.rect = self.Img.get_rect(topleft=(x, y))
        #self.rect = self.Img.get_rect(center=(self.W/2,self.H/2))
        #screen.blit(self.Img, (x, y))
        screen.blit(self.Img, self.rect)


# define background ################################################################
background = Item('pygame_exercises/data/background2.jpg', 0, 0, 0, 0, 0)



# define Player ####################################################################
Player = Item('pygame_exercises/data/spaceship.png',winX/2-32, winY-70, 1, 0, 0)
def move_player(dir):
    
    Player.dir = dir
    Player.X += Player.xRate*Player.dir
    if Player.X < 0:
        Player.X = 0
    if Player.X > winX-Player.W:
        Player.X = winX-Player.W
    Player.drawItem(Player.X, Player.Y)

# define bullet ####################################################################
Bullet = Item('pygame_exercises/data/bullet.png', winX/2-16, winY-75, 0, 1, 0)
def reset_bullet():
    global Bullet_state
    Bullet_state = False
    Bullet.dir = 0
    Bullet.X = Player.X
    Bullet.Y = Player.Y+5
    Bullet.drawItem(Bullet.X, Bullet.Y)
   


def fire_bullet():
    Bullet.dir = -1
    Bullet.drawItem(Bullet.X, Bullet.Y)
    Bullet.Y += Bullet.yRate*Bullet.dir
    

# define List of enemies ###########################################################
enemies = []
numOfenemies = 3
for i in range(numOfenemies):
    y = random.randint(-70, -30)
    x = random.randint(0, 550)
    r = random.randint(1, 6)*0.2
    enemy = Item('pygame_exercises/data/rock.png', x, y, 0, r, 1)
    enemies.append(enemy)

# Animation of dead enemy #########################################################
def Boom(i):
    enemies[i].Img = pygame.image.load('pygame_exercises/data/explosion1.png')
    enemies[i].dir = -1
    Explossion_sound.play()

# Re spawn enemy ##################################################################
def respawn_enemy(i):
    enemies[i].Img = pygame.image.load('pygame_exercises/data/rock.png')
    enemies[i].Y = random.randint(-300, -30)
    enemies[i].X = random.randint(0, 550)
    enemies[i].yRate += 0.2
    Bullet.yRate += 0.2
    Player.xRate += 0.2
    enemies[i].drawItem((enemies[i].X), (enemies[i].Y))
    
# Move enemy #######################################################################

def move_enemy(i):
    enemies[i].Y += enemies[i].yRate*enemies[i].dir
    enemies[i].drawItem((enemies[i].X), (enemies[i].Y))
    




# Game Over Text ####################################################################
game_over_font=pygame.font.Font('freesansbold.ttf',60)
Game_Over= game_over_font.render('GAME OVER',True,(255,255,255))
Game_Over_Rect=Game_Over.get_rect(center=(winX/2,winY/2))
def game_over():
    screen.blit(Game_Over,Game_Over_Rect)


# Scores Text ###########################################################
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
def show_score(x,y):
    score= font.render('score : '+str(score_value),True,(0,255,0))
    screen.blit(score,(x,y))


# Main game loop ####################################################################
player_alive = True
Bullet_state = False
running = True

while running:
    clock.tick(120)
    pygame.display.update()
    background.drawItem(0, 0)

    # Quit out of the window with close button on top ###############################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    # Check key inputs ##############################################################
        if event.type == pygame.KEYDOWN and player_alive:
            if event.key == pygame.K_LEFT:
                Player.dir = -1

            if event.key == pygame.K_RIGHT:
                Player.dir = 1

            if event.key == pygame.K_SPACE and Bullet_state == False:
                Bullet.X = Player.X+Bullet.W/2
                Bullet_state = True
                Bullet_sound.play()          
        if event.type == pygame.KEYUP and player_alive:
            if event.key == K_LEFT or event.key == K_RIGHT:
                Player.dir = 0
    # event check ended ############################################################

    # Fire Bullets #################################################################          
    if Bullet_state:
        if Bullet.Y > 0:
            fire_bullet()
            
        else:
            reset_bullet()

    # move player ##################################################################
    move_player(Player.dir)

    # move enemies #################################################################
    for i in range(numOfenemies):
            if enemies[i].Y <= winY:
                #enemies[i].Y += enemies[i].yRate*enemies[i].dir
                move_enemy(i)

            # if enemy goes down the screen #######################################    
            elif enemies[i].Y >= winY and player_alive:
                score_value-=1
                if player_alive: respawn_enemy(i)

            # Bullet Collission ###################################################
            if enemies[i].Y+enemies[i].H<Player.Y:  
                if Bullet.rect.colliderect(enemies[i].rect): 
                    score_value+=1
                    y = enemies[i].Y
                    Boom(i)
                    reset_bullet()

            # Animate dead enemy ##################################################
            if enemies[i].dir == -1:
                if enemies[i].Y <= y-20:
                    enemies[i].dir = 1
                    respawn_enemy(i)

            # Player Enemy Collission ###############################################
            if Player.rect.colliderect(enemies[i].rect) and player_alive: 
                player_alive=False 
                Player.Img = pygame.image.load('pygame_exercises/data/explosion.png')
                Explossion_sound.play()
            # Game Over #############################################################
            if not player_alive:
                game_over()    

    # Show Score ####################################################################
    show_score(textX,textY)