# _*_ coding: utf-8 _*_
# 导入模块
import random
import pygame

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 刷新的帧率
FRAME_PER_SEC = 60

# 创建定时器的常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 英雄的速度间隔
SPEED_INTERVAL    = 3

# 英雄发射子弹时间
HERO_FIRE_EVENT = pygame.USEREVENT+1
'''
飞机大战游戏精灵
'''


class CameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


'''
 背景类
'''
class Background(CameSprite):

    def __init__(self,is_alt = False):
        # 1.调用父类方法实现精灵的创建
        super().__init__("./images/background.png")
        # 2.判断是否交替图像，如果是，需要
        if is_alt:
            self.rect.y =  -self.rect.height


    def update(self):
        # 1.调用父类的方法实现
        super().update()

        # 2.判断是否移除屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

"""
    敌机类
"""
class Enemy(CameSprite):
    def __init__(self):
        # 1. 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")
        # 2. 指定敌机的初始随机速度 1-3
        self.speed = random.randint(1,3)
        # 3. 指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x =SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)
    def update(self):
        # 1. 调用父类方法，保持垂直方向的飞行
        super().update()
        # 2. 判断是否飞出屏幕，如果是，需要从精灵族删除敌机

        if self.rect.y >= SCREEN_RECT.height:

            print("飞出屏幕，需要从精灵组删除")
            self.kill()
    def __del__(self):
        print("敌机挂了 %s" % self.rect)

"""
    英雄类
"""
class Hero(CameSprite):
    def __init__(self):
        # 1. 调用父类方法
        super().__init__("./images/me1.png",0)
        # 2. 指定敌英雄的位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom  = SCREEN_RECT.bottom-120


        # 3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right


    def fire(self):
        print("发射子弹...")
        for i in (0,1,2):

            #1. 创建子弹精灵
            bullet = Bullet()
            #2. 设置精灵的位置

            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            #3. 将精灵添加到精灵组

            self.bullets.add(bullet)



'''
    子弹精灵
'''
class Bullet(CameSprite):
    def __init__(self):
        # 调用父类方法，设置子弹图片，设置子弹图片，设置初始速度
        super().__init__("./images/bullet1.png",-2)


    def update(self):
        # 调用父类方法，让子弹沿垂直方向飞行
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()


    def __del__(self):
        print("子弹被销毁")