import pygame
import random
import time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((750, 500))
playing = True

background = pygame.transform.scale(pygame.image.load("images/space bg.png"), (750, 500))
ship = pygame.transform.scale(pygame.image.load("images/yellow ship.png"), (90, 85))
font = pygame.font.SysFont("Times New Roman", 20)

ship_x = 450
ship_y = 380
ship_speed = 5

bullets = []
bullet_speed = random.randint(1,3)
bullet_width = 9
bullet_height = 10
starttime = time.time()
totaltime = 0
gameover = False

last_bullet_time = time.time()

while playing:
    totaltime = time.time() - starttime
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                ship_x -= 10
            if event.key == K_RIGHT:
                ship_x += 10

    current_time = time.time()

    if current_time - last_bullet_time >= 1:
        if totaltime >= 7:  
            bullet_count = random.randint(2, 4)
            if totaltime >= 14:
                bullet_count = random.randint(4,6)
                if totaltime >= 18:
                    bullet_count = random.randint(6,9)
        else:
            bullet_count = 1

        for i in range(bullet_count):
            x = random.randint(0, 880)
            d = pygame.Rect(x, 0, bullet_width, bullet_height)
            bullets.append(d)

        last_bullet_time = current_time

    ship_rect = pygame.Rect(ship_x, ship_y, 90, 85)
    for b in bullets:
        b.y += bullet_speed
        if ship_rect.colliderect(b):
            gameover = True
            break

    screen.blit(background, (0, 0))

    for b in bullets:
        pygame.draw.rect(screen, "white", b)

    screen.blit(ship, (ship_x, ship_y))

    if gameover == True:
        screen.fill("black")
        text1 = font.render("GAME OVER !!!", True, "white")
        text2 = font.render("Press Q to quit", True, "white")

        screen.blit(text1, (320, 220))
        screen.blit(text2, (320, 250))

        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    playing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_q:
                        waiting = False
                        playing = False

        break

    pygame.display.update()
