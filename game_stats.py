# Author:丁泽盛
# data:2020/10/6 14:57
class Gamestats():
    def __init__(self,ai_settings):

        self.ai_settings=ai_settings;
        self.reset_stats()
        # 控制游戏是否进行
        self.game_active =False

    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ships_left=self.ai_settings.ship_limit
        self.score=0