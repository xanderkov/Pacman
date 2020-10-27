import pygame
from Colors import *


class Pacman:
    def __init__(self):
        self.step = 5
        self.image = pygame.image.load('Characters/Pacman.png')
        self.rect = self.image.get_rect()
        self.rect.x = width // 2
        self.rect.y = height // 2
        self.x_shift = self.step
        self.y_shift = self.step

    def check_borders(self):
        """
        Borders collision
        :return:
        """
        if self.rect.x > width - self.rect.width:
            self.rect.x = self.rect.width
        if self.rect.x < 0:
            self.rect.x = width - self.rect.width
        if self.rect.y > height - self.rect.height:
            self.rect.y = self.rect.height
        if self.rect.y < 0:
            self.rect.y = height - self.rect.height

    def move(self, event):
        """
        Pacman movement
        :return:
        """
        move_right = False
        move_left = False
        move_up = False
        move_down = False
        self.y_shift = 0
        self.x_shift = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_s:
                move_up = True
            if event.key == pygame.K_w:
                move_down = True
        if move_right:
            self.x_shift = self.step
            move_right = False
        if move_left:
            self.x_shift = -self.step
            move_left = False
        if move_up:
            self.y_shift = self.step
            move_up = False
        if move_down:
            self.y_shift = -self.step
            move_down = False
        self.rect.x += self.x_shift
        self.rect.y += self.y_shift

    def draw(self, screen):
        screen.blit(self.image, self.rect)
