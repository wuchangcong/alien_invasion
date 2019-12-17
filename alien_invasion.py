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
    pygame.display.set_caption("Aline invasion")
    #创建一个飞船
    ship = Ship(screen,aline_settings)
    #创建一个子弹编组
    bullets = Group()
    #创建一个外星人编组
    alines = Group()
    #创建外星人群
    gf.create_fleet(aline_settings,screen,ship,alines)
    #主循环
    while True:
        #调用检查事件函数
        gf.check_events(aline_settings,screen,ship,bullets)
        #调用飞船移动函数
        ship.update()
        #调用子弹更新函数
        gf.update_bullets(aline_settings,screen,ship,alines,bullets)
        #调用外星人更新函数
        gf.update_alines(aline_settings,alines)
        #调用更新屏幕函数
        gf.update_screen(aline_settings,screen,ship,alines,bullets)

run_game()