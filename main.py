import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Busters")

icon = pygame.image.load("images/Galaxy (1).png")
background = pygame.image.load("images/mars.gif")
playerimg = pygame.image.load("images/Galaxy.png")
playerX = 370
playerY = 480
changeX = 0
changeY = 0

enemyimg = []
enemyX = []
enemyY = []
echangeX = []
echangeY = []
numenemy = 6
for i in range(numenemy):
    enemyimg.append(pygame.image.load("images/ufo (3).png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    echangeX.append(1)
    echangeY.append(0)

bulletimg = pygame.image.load("images/bullet.png")
bulletX = 0
bulletY = 480
bchangeX = 0
bchangeY = 1
bullet_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(i, x, y):
    screen.blit(enemyimg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def kill(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# pygame.display.set_icon(icon)

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -1
            if event.key == pygame.K_RIGHT:
                changeX = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, playerY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                changeX = 0
            if event.key == pygame.K_RIGHT:
                changeX = 0
    #         if event.key == pygame.K_SPACE:
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(numenemy):
        if enemyX[i] <= 0:
            echangeX[i] = 0.3
            enemyY[i] += 30
        elif enemyX[i] >= 736:
            echangeX[i] = -0.3
            enemyY[i] += 30

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bchangeY

    for i in range(numenemy):
        collision = kill(enemyX[i], enemyY[i], bulletX, bulletY)

        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

    playerX += changeX
    enemyX += echangeX

    player(playerX, playerY)
    for i in range(numenemy):
        enemy(enemyimg[i], enemyX[i], enemyY[i])
    pygame.display.update()
