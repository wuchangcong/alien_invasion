import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, aline_settings, screen, ship, bullets):
    '''响应按键按下'''
    # 控制飞船移动
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    # 发射子弹
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(aline_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    '''响应按键松开'''
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False


def check_events(aline_settings, screen, ship, bullets):
    '''监视鼠标和键盘事件'''
    for event in pygame.event.get():
        # 关闭窗口
        if event.type == pygame.QUIT:
            sys.exit()
        # 根据按键行为调用对应函数
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, aline_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(aline_settings, screen, ship, bullets):
    '''更新屏幕上的图像，并切换到新的屏幕'''
    # 每次循环都重绘屏幕
    screen.fill(aline_settings.bg_color)
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
