
import pygame
import random
from time import time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((900, 500))
playing = True

background = pygame.transform.scale(pygame.image.load("images/space bg.png"), (900, 500))
ship = pygame.transform.scale(pygame.image.load("images/yellow ship.png"), (100, 100))


ship_x = 450
ship_y = 380
ship_speed = 5


bullets = []
new_bullets = []
bullet_speed = 5
bullet_width = 9
bullet_height = 10
starttime = time()
totaltime = 0


while playing:
    
    totaltime = time()- starttime
    print(totaltime)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    
        if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    ship_x -= 10
                if event.key == K_RIGHT:
                    ship_x += 10 
    def spawn_bullets():
        global new_bullets
        x = random.randint(0, 880)
        d = pygame.Rect(x, 0, bullet_width, bullet_height)
        if int(totaltime) % 40 == 0:
            bullets.append(d)
            for b in bullets:
                pygame.draw.rect(screen, "white", b)
        
        # for i in range(random.randint(1,5)):
        #     for b in bullets:
        #         b.y += bullet_speed
            # if b.y < 500:
            #     new_bullets.append(b)
            
    # bullets = new_bullets
    

    
    ship_rect = pygame.Rect(ship_x, ship_y, 100, 100)
    # for b in bullets:
    #     if ship_rect.colliderect(b):
    #         print("Game Over!")
    #         playing = False

    
    screen.blit(background, (0, 0))
    screen.blit(ship, (ship_x, ship_y))
    if int(totaltime) % 40 == 0:
        print("hi")
        spawn_bullets()
        pygame.display.update()

    pygame.display.update()


