import pygame
from random import *

#小型敌机
class SmallEnemy(pygame.sprite.Sprite):
    energy = 1
    
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("image/enemy1.png").convert_alpha()
        self.destroy_images = []#存放毁灭时的图片
        self.destroy_images.extend([pygame.image.load("image/en1_des_1.png").convert_alpha(), pygame.image.load("image/en1_des_2.png").convert_alpha(),\
                                    pygame.image.load("image/en1_des_3.png").convert_alpha(), pygame.image.load("image/en1_des_4.png").convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True#存活状态
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)
        self.energy = SmallEnemy.energy

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = SmallEnemy.energy
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)


#中型敌机
class MidEnemy(pygame.sprite.Sprite):
    energy = 8
    
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("image/enemy2.png").convert_alpha()
        self.image_hit = pygame.image.load("image/en2_des_0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.destroy_images = []#存放毁灭时的图片
        self.destroy_images.extend([pygame.image.load("image/en2_des_1.png").convert_alpha(), pygame.image.load("image/en2_des_2.png").convert_alpha(),\
                                    pygame.image.load("image/en2_des_3.png").convert_alpha(), pygame.image.load("image/en2_des_4.png").convert_alpha()])
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True#存活状态
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10 * self.height, -self.height)
        self.energy = MidEnemy.energy#血量
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10 * self.height, -self.height)

#大型敌机
class BigEnemy(pygame.sprite.Sprite):
    energy = 20 
    
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("image/enemy3.png").convert_alpha()
        self.image2 = pygame.image.load("image/enemy32.png").convert_alpha()
        self.image_hit = pygame.image.load("image/en3_des_0.png").convert_alpha()
        self.destroy_images = []#存放毁灭时的图片
        self.destroy_images.extend([pygame.image.load("image/en3_des_1.png").convert_alpha(), pygame.image.load("image/en3_des_2.png").convert_alpha(),\
                                    pygame.image.load("image/en3_des_3.png").convert_alpha(), pygame.image.load("image/en3_des_4.png").convert_alpha(),\
                                    pygame.image.load("image/en3_des_5.png").convert_alpha(), pygame.image.load("image/en3_des_6.png").convert_alpha()])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True#存活状态
        self.mask = pygame.mask.from_surface(self.image1)
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-15 * self.height, -5 *self.height)
        self.energy = BigEnemy.energy#血量
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-15 * self.height, -5 *self.height)

