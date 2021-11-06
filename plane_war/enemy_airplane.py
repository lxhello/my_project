from random import randint

import pygame
from setting import Setting


class SmallEnemyPlane(pygame.sprite.Sprite):
    """Small enemy aircraft"""

    def __init__(self, bg_size):
        super(SmallEnemyPlane, self).__init__()
        self.setting = Setting()

        self.image = pygame.image.load("images/enemy1.png").convert()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images/enemy1_down1.png").convert_alpha(),
            pygame.image.load("images/enemy1_down2.png").convert_alpha(),
            pygame.image.load("images/enemy1_down3.png").convert_alpha(),
            pygame.image.load("images/enemy1_down4.png").convert_alpha(),
        ])
        self.image_hit = pygame.image.load("images/enemy2_hit.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.speed = self.setting.small_plane_speed
        self.mask = pygame.mask.from_surface(self.image)
        self.reset()
        self.energy = self.setting.small_plane_energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.setting.small_plane_speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)
        self.active = True
        self.energy = self.setting.small_plane_energy


class MidEnemyPlane(pygame.sprite.Sprite):
    """mid enemy aircraft"""

    def __init__(self, bg_size):
        super(MidEnemyPlane, self).__init__()
        self.setting = Setting()

        self.image = pygame.image.load("images/enemy2.png").convert()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images/enemy2_down1.png").convert_alpha(),
            pygame.image.load("images/enemy2_down2.png").convert_alpha(),
            pygame.image.load("images/enemy2_down3.png").convert_alpha(),
            pygame.image.load("images/enemy2_down4.png").convert_alpha(),
        ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.reset()
        self.speed = self.setting.big_mid_plane_speed
        self.energy = self.setting.mid_plane_energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.setting.big_mid_plane_speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)
        self.active = True
        self.energy = self.setting.mid_plane_energy


class BigEnemyPlane(pygame.sprite.Sprite):
    """big enemy aircraft"""

    def __init__(self, bg_size):
        super(BigEnemyPlane, self).__init__()
        self.setting = Setting()

        self.image1 = pygame.image.load("images/enemy3_n1.png").convert()
        self.image2 = pygame.image.load("images/enemy3_n2.png").convert()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images/enemy3_down1.png").convert_alpha(),
            pygame.image.load("images/enemy3_down2.png").convert_alpha(),
            pygame.image.load("images/enemy3_down3.png").convert_alpha(),
            pygame.image.load("images/enemy3_down4.png").convert_alpha(),
            pygame.image.load("images/enemy3_down5.png").convert_alpha(),
            pygame.image.load("images/enemy3_down6.png").convert_alpha(),
        ])
        self.image_hit = pygame.image.load("images/enemy3_hit.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.mask = pygame.mask.from_surface(self.image1)
        self.appear = False
        self.reset()
        self.speed = self.setting.big_mid_plane_speed
        self.energy = self.setting.big_plane_energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.setting.small_plane_speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)
        self.active = True
        self.energy = self.setting.small_plane_energy
