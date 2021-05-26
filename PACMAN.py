import pygame
from Colors import *


move_r = [pygame.image.load('Characters/Pacman_1_R.png'), pygame.image.load('Characters/Pacman_2_R.png'), pygame.image.load('Characters/Pacman_3_R.png'), pygame.image.load('Characters/Pacman_4_R.png'),
          pygame.image.load('Characters/Pacman_5.png'), pygame.image.load('Characters/Pacman_4_R.png'), pygame.image.load('Characters/Pacman_3_R.png'), pygame.image.load('Characters/Pacman_2_R.png'), pygame.image.load('Characters/Pacman_1_R.png')]


def change_animation(s, rotate, anim_count):
    if rotate != s:
        rotate = s
        anim_count += 1
    else:
        anim_count += 1
    return rotate, anim_count


class Pacman:
    def __init__(self):
        self.step = 5
        self.rotate = 'R'
        self.image = move_r[0]
        self.rect = self.image.get_rect()

        self.rect.x = width // 2
        self.rect.y = height // 2
        self.x_shift = self.step
        self.y_shift = self.step
        self.anim_count = 0

    def animation(self):
        if self.anim_count > 7:
            self.anim_count = 0
        if self.rotate == 'R':
            self.image = move_r[self.anim_count]
        if self.rotate == 'D':
            self.image = pygame.transform.rotate(move_r[self.anim_count], 270)
        if self.rotate == 'U':
            self.image = pygame.transform.rotate(move_r[self.anim_count], 90)
        if self.rotate == 'L':
            self.image = pygame.transform.rotate(move_r[self.anim_count], 180)

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
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or keys[pygame.K_RIGHT]:
                move_right = True
                self.rotate, self.anim_count = change_animation('R', self.rotate, self.anim_count)
            if event.key == pygame.K_a or keys[pygame.K_LEFT]:
                move_left = True
                self.rotate, self.anim_count = change_animation('L', self.rotate, self.anim_count)
            if event.key == pygame.K_s or keys[pygame.K_DOWN]:
                move_up = True
                self.rotate, self.anim_count = change_animation('D', self.rotate, self.anim_count)
            if event.key == pygame.K_w or keys[pygame.K_UP]:
                move_down = True
                self.rotate, self.anim_count = change_animation('U', self.rotate, self.anim_count)

        if move_right:
            self.x_shift = self.step
        if move_left:
            self.x_shift = -self.step
        if move_up:
            self.y_shift = self.step
        if move_down:
            self.y_shift = -self.step
        self.rect.x += self.x_shift
        self.rect.y += self.y_shift

    def draw(self, screen):
        screen.blit(self.image, self.rect)
