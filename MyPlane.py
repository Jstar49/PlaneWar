import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("image/me.png").convert_alpha()#我方飞机图片
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("image/me_des_1.png").convert_alpha(), pygame.image.load("image/me_des_2.png").convert_alpha(),\
                                    pygame.image.load("image/me_des_3.png").convert_alpha(),pygame.image.load("image/me_des_4.png").convert_alpha(),\
                                    pygame.image.load("image/me_des_5.png").convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        #我方飞机出现的位置
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height-64
        self.speed = 10#我方飞机速度
        self.active = True#存活状态
        self.invincible = False#设置无敌状态
        #设置一个mask,在进行碰撞检测时去掉surface对象透明的部分
        self.mask = pygame.mask.from_surface(self.image)

    def moveUp(self):#向上移动
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):#向下移动
        if self.rect.bottom < self.height - 60 :
            self.rect.top += self.speed
        else:
            #self.rect.bottom = self.height
            self.rect.bottom = self.height - 60

    def moveLeft(self):#向左移动
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):#向右移动
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height-64
        self.active = True
        self.invincible = True
