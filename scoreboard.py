# Author:丁泽盛
# data:2020/10/6 16:14
import pygame.font

class Scoreboard():
    def __init__(self,ai_settings,screen,stats):
        self.screen=screen
        self.screen_recr=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)

        self.prep_score()
    def prep_score(self):
        score_str = str(self.stats.score)
        print(score_str)
        self.score_image = self.font.render(score_str,True,self.text_color)

        self.score_rect =self.score_image.get_rect()
        self.score_rect.right = self.screen_recr.right - 20
        self.score_rect.top = 20
    def show_score(self):

        self.screen.blit(self.score_image,self.score_rect)