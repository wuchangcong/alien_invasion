import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''外星人的类'''

    def __init__(self, aline_settings, screen):
        '''初始化'''
        super(Alien,self).__init__()
        self.screen = screen
        self.aline_settings = aline_settings
        #加载图像和rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #设置初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #存储位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''移动外星人'''
        self.x += (self.aline_settings.alien_speed_factor * self.aline_settings.fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        '''到达边缘返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True