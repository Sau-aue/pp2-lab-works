import pygame,sys  # sys needed for sys.exit() as if player decides to leave
import time, random 
from pygame.locals import * # helps to shorten constantas as pygame.QUIT,pygame.K_LEFT

pygame.init()

FPS = 60
FramesPerSecond=pygame.time.Clock()

#set display
width = 600
height = 700 
screen= pygame.display.set_mode((width,height))
pygame.display.set_caption("Yo this is my game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                





pygame.quit()
FramesPerSecond.tick(FPS)