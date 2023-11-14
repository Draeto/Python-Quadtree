import pygame
import quadtree

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ## TODO importation du quadtree depuis quadtree.py puis création de l'interface graphique

    screen.fill("white")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
