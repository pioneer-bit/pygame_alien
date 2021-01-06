# Author:丁泽盛
# data:2020/10/5 15:03

#创建设置类
class Settings():
    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕设置
        self.screen_width=1000
        self.screen_height=600
        self.bg_color=(230,230,230)

        #飞船的速度
        self.ship_speed_factor = 1.5
        #
        self.ship_limit =3

        #子弹设置
        self.bullet_speed_factor = 0.4
        self.bullet_width = 670
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed=99

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 1

        #方向参数,1表示向右移动 -1表示向左移动
        self.fleet_direction = 1

        #计分
        self.alien_points=50

