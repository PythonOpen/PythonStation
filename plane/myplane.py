import pygame


class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        # 创建英雄机图像对象，convert_alpha()为图像背景透明
        self.image1 = pygame.image.load("images/me1.png").convert_alpha()
        self.image2 = pygame.image.load("images/me2.png").convert_alpha()
        self.destroy_image = []
        # 创建英雄机撞毁后的图像对象
        self.destroy_image.extend([\
            pygame.image.load("images/me_destroy_1.png").convert_alpha(),\
            pygame.image.load("images/me_destroy_2.png").convert_alpha(),\
            pygame.image.load("images/me_destroy_3.png").convert_alpha(),\
            pygame.image.load("images/me_destroy_4.png").convert_alpha(),\
        ])
        self.active = True
        # get_rect是一个处理矩形图像的方法，返回值包含矩形的居中属性
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 设置飞机初始位置
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
        self.speed = 10
        """
        pygame.mask.Mask  ——   用于表示 2d 位掩码（遮罩）的 Pygame 对象
        用于快速实现完美的碰撞检测，Mask 可以精确到 1 个像素级别的判断。
        Surface 对象中透明的部分设置为 1，不透明部分设置为 0。
        """
        self.mask = pygame.mask.from_surface(self.image1)
        self.invincible = False

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def  reset(self):
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.active = True
        self.invincible = True
