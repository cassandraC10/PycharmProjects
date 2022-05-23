import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("space invaders")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10,20,30))
    pygame.display.update()
