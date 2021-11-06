import pygame

import my_plane
from setting import Setting
import sys
import enemy_airplane


class PlaneWar:
    """class that management game behaviors"""

    def __init__(self):
        """initialize game"""
        self.setting = Setting()
        pygame.init()
        self.screen = pygame.display.set_mode((self.setting.screen_width,
                                               self.setting.screen_height))
        pygame.display.set_caption("plane war")
        self.background = pygame.image.load("images/planewar.jpg").convert()

    def add_small_enemy_plane(self, group1, group2, num):
        for i in range(num):
            e1 = enemy_airplane.SmallEnemyPlane((self.setting.screen_width,
                                                 self.setting.screen_height))
            group1.add(e1)
            group2.add(e1)

    def add_mid_enemy_plane(self, group1, group2, num):
        for i in range(num):
            e2 = enemy_airplane.MidEnemyPlane((self.setting.screen_width,
                                               self.setting.screen_height))
            group1.add(e2)
            group2.add(e2)

    def add_big_enemy_plane(self, group1, group2, num):
        for i in range(num):
            e3 = enemy_airplane.BigEnemyPlane((self.setting.screen_width,
                                               self.setting.screen_height))
            group1.add(e3)
            group2.add(e3)

    def start(self):
        mp = my_plane.MyPlane(bg_size=(self.setting.screen_width,
                                       self.setting.screen_height))

        enemies = pygame.sprite.Group()

        small_enemies_plane = pygame.sprite.Group()
        self.add_small_enemy_plane(small_enemies_plane, enemies, 15)

        mid_enemies_plane = pygame.sprite.Group()
        self.add_mid_enemy_plane(mid_enemies_plane, enemies, 4)

        big_enemies_plane = pygame.sprite.Group()
        self.add_big_enemy_plane(big_enemies_plane, enemies, 2)

        life_value = 3
        running = True
        delay = 100
        while running:
            if life_value:
                # draw enemy mainframe
                key_press = pygame.key.get_pressed()
                if key_press[pygame.K_w]:
                    mp.moveUp()
                if key_press[pygame.K_s]:
                    mp.moveDown()
                if key_press[pygame.K_a]:
                    mp.moveLeft()
                if key_press[pygame.K_d]:
                    mp.moveRight()

                for each in big_enemies_plane:
                    if each.active:
                        each.move()
                        if each.hit:
                            self.screen.blit(each.image_hit, each.rect)
                            each.hit = False
                        else:
                            if switch_plane:
                                self.screen.blit(each.image1, each.rect)
                            else:
                                self.screen.blit(each.image2, each.rect)

                    # 用于切换图片
                    if not (delay % 11):
                        switch_plane = not switch_plane

                    delay -= 1
                    if not delay:
                        delay = 100

                    pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

    def run_game(self):
        """game main_circle"""
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    else:
                        self.start()


if __name__ == "__main__":
    pw = PlaneWar()
    pw.run_game()
    pw.start()
