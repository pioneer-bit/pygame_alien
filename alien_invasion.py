# Author:丁泽盛
# data:2020/10/5 14:58

import sys
import pygame
from pygame_alien.settings import Settings
from pygame_alien.ship import Ship
from pygame_alien.alien import Alien
import pygame_alien.game_functions as gf
from pygame.sprite import Group
from pygame_alien.game_stats import Gamestats
from  pygame_alien.button import Button
from pygame_alien.scoreboard import Scoreboard
def run_game():

    pygame.init()  #初始化游戏背景设置
    pygame.display.set_caption('Alien Invasion')
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_height))  # 创建显示窗口

    # 创建一个用于存储游戏统计信息的实例
    stats = Gamestats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)

    play_button = Button(ai_settings, screen, 'Play')
   #创建一艘飞船
    ship=Ship(ai_settings,screen)
    # #创建一个外星人
    # alien=Alien(ai_settings,screen)
    #创建一群外星人
    aliens=Group()
    #一个用于存储子弹的编组
    bullets=Group()
    gf.creat_fleet(ai_settings,screen,ship,aliens)
    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,stats,sb,aliens,bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)


run_game()
