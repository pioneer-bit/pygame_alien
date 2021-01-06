# Author:丁泽盛
# data:2020/10/5 15:55
import sys
import pygame
from time import sleep
from pygame_alien.bullet import Bullet
from pygame_alien.alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''键按下'''
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()

        #开火
    elif event.key == pygame.K_SPACE:
        #创建一颗子弹但并将其加入编组bullets中
        fire_bullet(ai_settings,screen,ship,bullets)
        # if len(bullets) < ai_settings.bullet_allowed:
        #     new_bullet = Bullet(ai_settings, screen, ship)
        #     bullets.add(new_bullet)

def check_keyup_events(event,ship):
    '''键抬起'''
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.reset_stats()
        stats.game_active=True

        aliens.empty()
        bullets.empty()
        creat_fleet(ai_settings,screen,ship,aliens,)
        ship.center_ship()


def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    '''更新屏幕上的图像，并切换到新屏幕'''
    #每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    aliens.draw(screen)

    #显示得分
    sb.show_score()
    #如果游戏处于非活动状态,就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    # alien.blieme()
    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,stats,sb,aliens,bullets):
    # 更新子弹的位置并消除已消失的子弹
    # 更新子弹的位置
    bullets.update()
    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            print(len(bullets))#用于确认子弹的确被删除

            #碰撞检测
    collisions  = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        stats.score += ai_settings.alien_points
        sb.prep_score()
    if len(aliens) == 0:
        #删除现有的子弹并新建一群外星人
        bullets.empty()
        creat_fleet(ai_settings,screen,ship,aliens)

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    '''响应被外星人撞到的飞船'''
    if stats.ships_left> 0:
        stats.ships_left -= 1
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人,并将飞船放到屏幕低端中央
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active =False

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    '''检查是否有外星人到达底端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船被撞倒一样处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break


def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    '''检查是否有外星人位于名目边缘,并更新整群外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    '''更新外星人群中所有外星人的位置'''
    aliens.update()
    #检测外星人与飞船相撞
    if pygame.sprite.spritecollideany(ship,aliens):
        print('Ship hit')
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)


def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(ai_settings ,ship_height,alien_height):
    '''计算屏幕可容纳多少行外星人'''
    available_space_y=(ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows =int(available_space_y/(2 * alien_height))
    return number_rows

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    # 创建一个外星人并将其放在当前行

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y= alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def creat_fleet(ai_settings,screen,ship,aliens):
    '''创建外星人群'''
    alien = Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    # 创建第一行外星人m
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x + 1):
            creat_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings,aliens):
    '''有外星人到达边缘时采取的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''将外星人下移,并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1