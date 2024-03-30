import pygame

from player import Player
from salabai import Salabai

window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()



background = pygame.transform.scale(pygame.image.load("background.png"), (700, 500))


roma = Player(100, 100, 50, 50, "sprite1 (1).png", 2)
salabai = Salabai(100, 100, 50, 50, "sprite2.png", 2)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    window.blit(background, (0, 0))
    roma.draw(window)
    roma.move()
    salabai.draw(window)
    salabai.move()

    pygame.display.flip()
    fps.tick(60)