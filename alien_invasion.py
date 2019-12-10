import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    aline_settings = Settings()
    screen = pygame.display.set_mode((
        aline_settings.screen_width,
        aline_settings.screen_height
    ))
    #设置窗口标题
    pygame.display.set_caption("Aline_invasion")
    #创建一个飞船
    ship = Ship(screen,aline_settings)
    #创建一个子弹编组
    bullets = Group()
    #主循环
    while True:
        #调用检查事件函数
        gf.check_events(aline_settings,screen,ship,bullets)
        #调用飞船移动函数
        ship.update()
        #调用子弹移动函数
        bullets.update()
        #调用更新屏幕函数
        gf.update_screen(aline_settings,screen,ship,bullets)


run_game()