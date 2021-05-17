import pygame
import sys
from Colors import *
from PACMAN import *

image = pygame.image.load('Characters/map.png')


def main():
    pacman = Pacman()
    pygame.init()
    screen = pygame.display.set_mode(size)
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        pacman.move(event)

        pacman.animation()
        pacman.check_borders()
        screen.fill(BLACK)
        pacman.draw(screen)
        pygame.display.flip()
        pygame.time.wait(30)
    sys.exit()


if __name__ == "__main__":
    main()