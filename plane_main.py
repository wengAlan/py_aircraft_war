# _*_ coding: utf-8 _*_
# 导入模块

import pygame
from plane_sprites import *

"""
 飞机大战游戏
"""


class PlaneGame(object):
    # 初始化
    def __init__(self):
        print("初始化")
        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.精灵和精灵组的创建
        self.__create_sprites()
        # 4.设置定时器时间-创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    # 启动游戏
    def start_game(self):
        print("开始游...")
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self._event_handler()
            # 碰撞检测
            self._chceck_collide()
            # 更新精灵组
            self._update_sprite_group()
            # 更新显示
            pygame.display.update()

    # 精灵和精灵组的创建

    def __create_sprites(self):
        # 背景精灵
        bg1 = Background()
        bg2 = Background(True)

        # 背景精灵组
        self.back_group = pygame.sprite.Group(bg1,bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄
        self.hero =Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    # 事件监听

    def _event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame._game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机的精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # 使用键盘提供对应的按键索引值 1
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            print("向右")
            self.hero.speed = SPEED_INTERVAL

        elif keys_pressed[pygame.K_LEFT]:
            print("向左")
            self.hero.speed = -SPEED_INTERVAL
        else:
            self.hero.speed = 0


    # 碰撞检测
    def _chceck_collide(self):
        # 1 .子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        # 2 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

        # 3.判断列表时候有内容
        if len(enemies) > 0 :
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame._game_over()
    # 更新精灵组
    def _update_sprite_group(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    # 精灵和精灵组的创建
    @staticmethod
    def _game_over():
        print("游戏结束")
        pygame.quit()
        exit()


# 主程序
if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
