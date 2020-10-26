import pygame
import sys


size = width, height = 800, 600
black = 0, 0, 0


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill(black)

        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == "__main__":
    main()