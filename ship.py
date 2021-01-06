# Author:丁泽盛
# data:2020/10/5 15:27
import pygame
class Ship():
    def __init__(self,ai_settings,screen):
        '''初始化飞船并设置其初始位置'''
        self.screen = screen
        #加载飞船图像并获取其他外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect=screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性中存储小数值
        self.ai_settings = ai_settings
        #根据self.center更新rect对象
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
            if self.rect.right>self.screen_rect.right:
                self.rect.centerx = self.screen_rect.left

        if self.moving_left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
            if self.rect.left<self.screen_rect.left:
                self.rect.centerx = self.screen_rect.right
        if self.moving_up:
            self.rect.bottom -= 1
        if self.moving_down:
            self.rect.bottom += 1

    def center_ship(self):
        ''''让飞船在屏幕上居中'''
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)



