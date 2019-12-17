import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, alien_settings, screen, ship, bullets):
    '''响应按键按下'''
    # 控制飞船移动
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    # 发射子弹
    elif event.key == pygame.K_SPACE:
        fire_bullet(alien_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, ship):
    '''响应按键松开'''
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False


def check_events(alien_settings, screen, ship, bullets):
    '''监视鼠标和键盘事件'''
    for event in pygame.event.get():
        # 关闭窗口
        if event.type == pygame.QUIT:
            sys.exit()
        # 根据按键行为调用对应函数
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, alien_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(alien_settings, screen, ship, aliens, bullets):
    '''更新屏幕上的图像，并切换到新的屏幕'''
    # 每次循环都重绘屏幕
    screen.fill(alien_settings.bg_color)
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(alien_settings, screen, ship, aliens, bullets):
    '''子弹更新函数'''
    # 调用子弹移动函数
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(
        alien_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(alien_settings, screen, ship, aliens, bullets):
    # 检查是否击中外星人，击中就删除外星人和子弹
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # 删除现有子弹，并创建外星人
        bullets.empty()
        create_fleet(alien_settings, screen, ship, aliens)


def fire_bullet(alien_settings, screen, ship, bullets):
    '''开火'''
    if len(bullets) < alien_settings.bullet_allowed:
        new_bullet = Bullet(alien_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(alien_settings, screen, ship, aliens):
    '''创建外星人群'''
    # 创建一个外星人，并获取一行可以容纳的外星人数量
    alien = Alien(alien_settings, screen)
    number_aliens_x = get_number_aliens_x(alien_settings, alien.rect.width)
    number_row = get_number_rows(
        alien_settings, ship.rect.height, alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_row):
        for alien_number in range(number_aliens_x):
            create_alien(alien_settings, screen, aliens,
                         alien_number, row_number)


def get_number_aliens_x(alien_settings, alien_width):
    '''计算一行可以容纳多少外星人'''
    available_space_x = alien_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(alien_settings, screen, aliens, alien_number, row_number):
    '''创建一个外星人并放在当前行'''
    alien = Alien(alien_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(alien_settings, ship_height, alien_height):
    '''计算屏幕可以容纳多少行外星人'''
    available_space_y = (alien_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_alines(alien_settings, aliens):
    check_fleet_edges(alien_settings, aliens)
    aliens.update()


def check_fleet_edges(alien_settings, aliens):
    '''当外星人到达屏幕边缘时采取相应的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(alien_settings, aliens)
            break


def change_fleet_direction(alien_settings, aliens):
    '''改变外星人移动方向'''
    for alien in aliens.sprites():
        alien.rect.y += alien_settings.fleet_drop_speed
    alien_settings.fleet_direction *= -1
