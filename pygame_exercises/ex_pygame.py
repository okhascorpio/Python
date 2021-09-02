# clear screen at Run
import pygame
import random
from os import system
system("cls")

clock = pygame.time.Clock()
global winX, winY
winX = 595
winY = 800
# Title and icon
pygame.display.set_caption('PYGAME EXERCISE')
icon = pygame.image.load('Exercise with pygame/spaceship.png')
pygame.display.set_icon(icon)

# Draw a window
screen = pygame.display.set_mode((winX, winY))

# Background
backgroundImg = pygame.image.load('Exercise with pygame/background2.jpg')


def background():
    screen.blit(backgroundImg, (0, 0))


# Player
playerImg = icon
#global player_rect
player_rect = playerImg.get_rect()
player_height = playerImg.get_height()
player_width = playerImg.get_width()
playerX = winX/2-player_width/2
playerY = winY-30-player_height
playerX_change = 0  # +1 for right -1 for left
playerX_rate = 20  # multply by this to increase playerX_change speed
# Define Player


def player(x, y):
    global player_rect
    player_rect = playerImg.get_rect(topleft=(x, y))
    screen.blit(playerImg, (x, y))


# Enemy
number_of_enemies = 4
enemyImg = []
enemy_rect = []
enemy_height = []
enemy_width = []
enemyX = []
enemyY = []
enemyY_rate = []

for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load('Exercise with pygame/asteroid2.png'))
    enemy_rect.append(enemyImg[i].get_rect())
    enemy_height.append(enemyImg[i].get_height())
    enemy_width.append(enemyImg[i].get_width())
    enemyX.append(random.randint(0, winX-enemy_width[i]))
    enemyY.append(-1)
    enemyY_rate.append(1)  # change this to change speed

# Define Enemy


def enemy(x, y, i):
    global enemy_rect
    enemy_rect[i] = enemyImg[i].get_rect(topleft=(x, y))
    screen.blit(enemyImg[i], (x, y))


def enemy_reset(i):
    global enemyX, enemyY
    enemyX[i] = random.randint(0, winX-enemy_width[i])
    enemyY[i] = -1*random.randint(45, 100)
    #print(enemyY)
    enemy(enemyX[i], enemyY[i],i)


# Bullet
bulletImg = pygame.image.load('Exercise with pygame/bullet.png')
bullet_height = bulletImg.get_height()
bullet_width = bulletImg.get_width()
bulletX = playerX
bulletY = playerY
bulletY_rate = 10  # change this to change speed
bullet_rect = bulletImg.get_rect()
bullet_fired_flag = False

# Define bullet


def bullet(x, y):
    global bullet_rect
    bullet_rect = bulletImg.get_rect(topleft=(x, y))
    screen.blit(bulletImg, (x, y))


def bullet_reset():
    global bulletX, bulletY, bullet_fired_flag
    bulletX = playerX
    bulletY = playerY
    bullet(bulletX, bulletY)
    bullet_fired_flag = False


running = True
while running:
    pygame.display.update()  # Needed in every screen to update

# Quit out of the window with close button on top
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # print(event.key,pygame.K_RIGHT)
                playerX_change = 1*playerX_rate
            if event.key == pygame.K_LEFT:
                playerX_change = -1*playerX_rate

            if event.key == pygame.K_SPACE and bullet_fired_flag == False:
                bulletX = playerX+bullet_width/2
                bullet_fired_flag = True
                # bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Fill color in screen
    # screen.fill((50, 30, 30))  # or use hex as ('#ffffffff')

    background()

    if bullet_fired_flag:
        bullet(bulletX, bulletY)
        bulletY -= bulletY_rate
        # bullet_fired_flag = False
    if bulletY < 0:
        bullet_reset()

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= winX-player_width:
        playerX = winX-player_width

    player(playerX, playerY)

# Enemy movement
    for i in range(number_of_enemies):
        if enemyY[i] < winY:
            enemyY[i] += enemyY_rate[i]
            enemy(enemyX[i], enemyY[i],i)
        if enemyY[i] >= winY:
            enemy_reset(i)
        print(i)

# Collission Test
        if bullet_rect.colliderect(enemy_rect[i]):
            print('Boom')
            bullet_reset()
            enemy_reset(i)

    clock.tick(60)
