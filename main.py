import pygame
import sys
import traceback#检错模块
from pygame.locals import *#导入pygame所有模块
import MyPlane
import enemy
import bullet
from random import *
import supply

pygame.init()
pygame.mixer.init()

bg_size = width, height = 901,897
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("飞机大战")
#背景图片
background = pygame.image.load("image/bg.png").convert()

#颜色
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

#时间模块
clock = pygame.time.Clock()

#载入游戏音乐
pygame.mixer.music.load("sound/bg_music.wave")#背景音乐
pygame.mixer.music.set_volume(0.1)
hit = pygame.mixer.Sound("sound/hit.wav")#击中音效
hit.set_volume(0.2)
winner = pygame.mixer.Sound("sound/winner.wav")#游戏胜利音乐
winner.set_volume(0.2)
big_enemy = pygame.mixer.Sound("sound/winner.wav")#大型敌机出现前的音效
big_enemy.set_volume(0.1)
big_die = pygame.mixer.Sound("sound/big_die.wav")#大型敌机被消灭的音效
big_die.set_volume(0.2)
up_level = pygame.mixer.Sound("sound/up_level.wav")#难度提升时的音效
up_level.set_volume(0.2)
bomb = pygame.mixer.Sound("sound/bomb.wav")#炸弹爆炸的声音
bomb.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")#补给到来的声音
supply_sound.set_volume(0.2)
get_supply = pygame.mixer.Sound("sound/get_supply.wav")#获得补给的音效
get_supply.set_volume(0.2)
menu_sound = pygame.mixer.Sound("sound/mune.wav")#选择菜单时的音效
menu_sound.set_volume(0.2)

def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)

#加快敌机速度
def inc_speed(target, inc):
    for each in target:
        each.speed += inc

#"关于"界面
def About():
    #娱乐图片
    about_fun_img = pygame.image.load("image/about_fun.JPG")
    about_fun_rect = about_fun_img.get_rect()
    #娱乐图片
    about_fun2_img = pygame.image.load("image/about_fun2.png")
    about_fun2_rect = about_fun2_img.get_rect()

    #返回按钮
    comeback1_img = pygame.image.load("image/comeback1.png").convert_alpha()#返回按钮
    comeback2_img = pygame.image.load("image/comeback2.png").convert_alpha()
    comeback_img = comeback1_img#设置默认图片
    comeback_rect = comeback1_img.get_rect()
    comeback_rect.left, comeback_rect.top = 901 - 100, 897 - 100
    
    about_font = pygame.font.Font("font/font.TTF", 35)
    Author_text = about_font.render("Author: 星星", True, WHITE)
    Email_text = about_font.render("E-mail: 18473465306@163.com", True, WHITE)
    Language_text = about_font.render("Language: Python", True, WHITE)
    Bgm_text = about_font.render("Bgm: 《Into The Battlefield》", True, WHITE)
    #This book is for academic exchanges and research learning, Do not used for commercial purposes. 
    Attention1_text = about_font.render("Attention: This game is for academic exchanges ", True, WHITE)
    Attention2_text = about_font.render("and research learning. Please do not", True, WHITE)
    Attention3_text = about_font.render("used for commercial purposes.", True, WHITE)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                #返回按钮
                if comeback_rect.collidepoint(event.pos):
                    comeback_img = comeback1_img
                else:
                    comeback_img = comeback2_img

            elif event.type == MOUSEBUTTONDOWN:
                #collidepoint(event.pos),自动检测鼠标是否停留在pos内，如果是则返回True
                if event.button == 1 and comeback_rect.collidepoint(event.pos):
                    menu_sound.play()
                    Menu()
                
        screen.blit(background, (0, 0))
        screen.blit(about_fun2_img, about_fun2_rect)
        screen.blit(comeback_img, comeback_rect)
        screen.blit(Author_text, (10, 90))
        screen.blit(Email_text, (10, 140))
        screen.blit(Language_text, (10, 190))
        screen.blit(Bgm_text, (10, 240))
        screen.blit(Attention1_text, (10, 290))
        screen.blit(Attention2_text, (205, 340))
        screen.blit(Attention3_text, (205, 390))
        screen.blit(about_fun_img, (0, 897 - about_fun_rect.height))
        
        pygame.display.flip()

        clock.tick(60)

#帮助界面
def Help():
    #背景图片
    help_fun_img = pygame.image.load("image/help_fun.jpg")
    help_fun_rect = help_fun_img.get_rect()
    #返回按钮
    comeback1_img = pygame.image.load("image/comeback1.png").convert_alpha()#返回按钮
    comeback2_img = pygame.image.load("image/comeback2.png").convert_alpha()
    comeback_img = comeback1_img#设置默认图片
    comeback_rect = comeback1_img.get_rect()
    comeback_rect.left, comeback_rect.top = 901 - 100, 897 - 100

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                #返回按钮
                if comeback_rect.collidepoint(event.pos):
                    comeback_img = comeback1_img
                else:
                    comeback_img = comeback2_img

            elif event.type == MOUSEBUTTONDOWN:
                #collidepoint(event.pos),自动检测鼠标是否停留在pos内，如果是则返回True
                if event.button == 1 and comeback_rect.collidepoint(event.pos):
                    menu_sound.play()
                    Menu()

        screen.blit(background, (0, 0))
        screen.blit(help_fun_img, (0, 0))
        screen.blit(comeback_img, comeback_rect)

        pygame.display.flip()

        clock.tick(60)

#菜单界面
def Menu():
    #娱乐图片1
    menu_fan_img = pygame.image.load("image/menu_fun.png").convert_alpha()#娱乐图片
    menu_fan_rect = menu_fan_img.get_rect()
    menu_fan_rect.left, menu_fan_rect.top = 0, 0
    #娱乐图片2
    menu_fan2_img = pygame.image.load("image/menu_fun2.png").convert_alpha()#娱乐图片
    menu_fan2_rect = menu_fan2_img.get_rect()
    menu_fan2_rect.left, menu_fan2_rect.top = 901 - menu_fan2_rect.width, 0
    
    #开始游戏按钮
    begin_game1_img = pygame.image.load("image/begin_game1.png").convert_alpha()#开始游戏按钮
    begin_game2_img = pygame.image.load("image/begin_game2.png").convert_alpha()
    begin_game_img = begin_game1_img
    begin_game_rect = begin_game1_img.get_rect()
    begin_game_rect.left, begin_game_rect.top = 264 + 350, 486 - 200

    #帮助按钮
    help1_img = pygame.image.load("image/help1.png").convert_alpha()#帮助按钮
    help2_img = pygame.image.load("image/help2.png").convert_alpha()
    help_img = help1_img
    help_rect = help1_img.get_rect()
    help_rect.left, help_rect.top = 264 + 350, 424 + 0

    #关于按钮
    about1_img = pygame.image.load("image/about1.png").convert_alpha()#关于按钮
    about2_img = pygame.image.load("image/about2.png").convert_alpha()
    about_img = about1_img
    about_rect = about1_img.get_rect()
    about_rect.left, about_rect.top = 264 + 350, 424 + 150

    #鼠标解除按钮音效
    is_sound = True
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #检测鼠标是否移动到暂停游戏按钮
            elif event.type == MOUSEMOTION:
                #开始游戏按钮
                if begin_game_rect.collidepoint(event.pos):
                    begin_game_img = begin_game2_img
                else:
                    begin_game_img = begin_game1_img
                #帮助按钮
                if help_rect.collidepoint(event.pos):
                    help_img = help1_img
                else:
                    help_img = help2_img
                #关于按钮
                if about_rect.collidepoint(event.pos):
                    about_img = about1_img
                else:
                    about_img = about2_img

            elif event.type == MOUSEBUTTONDOWN:
                #collidepoint(event.pos),自动检测鼠标是否停留在pos内，如果是则返回True
                if event.button == 1 and about_rect.collidepoint(event.pos):
                    menu_sound.play()
                    About()
                elif event.button == 1 and begin_game_rect.collidepoint(event.pos):
                    menu_sound.play()
                    main()
                elif event.button == 1 and help_rect.collidepoint(event.pos):
                    menu_sound.play()
                    Help()
                
        screen.blit(background, (0, 0))
        screen.blit(menu_fan2_img, menu_fan2_rect)
        screen.blit(menu_fan_img, (0, 0))
        screen.blit(begin_game_img, begin_game_rect)
        screen.blit(help_img, help_rect)
        screen.blit(about_img, about_rect)
        
        pygame.display.flip()

        clock.tick(60)

def main():
    #pygame.mixer.music.play(重复次数,开始时间),这里重复次数会加上原来的一次,开始时间如果为1.0的话,表示从音乐的第2秒开始播放.
    pygame.mixer.music.play(-1)#这里设置-1表示无限循环

    #生成我方飞机
    me = MyPlane.MyPlane(bg_size)
    #生成敌方飞机
    enemies = pygame.sprite.Group()#建立一个组

    #生成敌方小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)
    #生成敌方中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 4)
    #生成敌方大型飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 2)
    

    #生成子弹
    bullet1 = []
    bullet1_index = 0#用于索引
    BULLET1_MUN = 6#6颗子弹
    for i in range(BULLET1_MUN):
        bullet1.append(bullet.Bullet1(me.rect.midtop))#midtop是顶部中央的意思

    #增强弹药
    bullet2 = []
    bullet2_index = 0#用于索引
    BULLET2_MUN = 12#12颗子弹
    for i in range(BULLET2_MUN // 2):
        bullet2.append(bullet.Bullet2((me.rect.centerx - 33, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx + 30, me.rect.centery)))

    # 中弹图片索引
    e1_des_index = 0
    e2_des_index = 0
    e3_des_index = 0
    me_des_index = 0

    #统计得分
    score = 0
    score_font = pygame.font.Font("font/font.TTF", 36)#定义字体

    #标志是否暂停游戏
    paused = False
    #加载暂停图片
    stopping_img = pygame.image.load("image/stopping.png").convert_alpha()
    stopping_rect = stopping_img.get_rect()
    stopping_rect.left, stopping_rect.top = width / 2 - stopping_rect.width / 2, height / 2 - stopping_rect.height / 2
    stop1_img = pygame.image.load("image/stop1.png").convert_alpha()
    stop2_img = pygame.image.load("image/stop2.png").convert_alpha()
    begin1_img = pygame.image.load("image/begin1.png").convert_alpha()
    begin2_img = pygame.image.load("image/begin2.png").convert_alpha()
    stop_rect = stop1_img.get_rect()
    begin_rect = begin1_img.get_rect()
    paused_rect = stop1_img.get_rect()
    stop_rect.left, stop_rect.top = width - stop_rect.width - 10, 10
    begin_rect.left, begin_rect.top = width - begin_rect.width - 10, 10
    pause_img = stop1_img#设置默认图片

    #设置难度级别，默认难度1
    level = 1

    #全屏炸弹
    bomb_img = pygame.image.load("image/boom.jpg").convert_alpha()
    bomb_rect = bomb_img.get_rect()
    bomb_font = pygame.font.Font("font/font.TTF", 48)
    bomb_num = 3#炸弹数量

    #每30秒发放一个补给56
    bullet_supply = supply.Bullet_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    #定时器
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)

    #弹药增强定时器
    DOUBLE_BULLET_TIME = USEREVENT + 1
    #标志是否使用增强弹药
    is_double_bullet = False

    #生命数量
    life_img = pygame.image.load("image/life.png").convert_alpha()
    life_rect = life_img.get_rect()
    life_num = 3
    
    running = True
    switch_image = True#飞机图片切换
    delay = 100#人工干预延迟

    #解除我方无敌状态计时器
    INVINCIBLE_TIME = USEREVENT + 2

    #用于重复打开文件
    record_file = False

    #用于游戏结束界面
    gameover_font = pygame.font.Font("font/font.TTF", 48)
    gameover_font1 = pygame.font.Font("font/font.TTF", 35)
    again_img = pygame.image.load("image/again.png").convert_alpha()#再来一次按钮
    again_rect = again_img.get_rect()
    gameover_img = pygame.image.load("image/gameover.png").convert_alpha()#结束游戏按钮
    gameover_rect = gameover_img.get_rect()
    again_rect.left, again_rect.top = 318 + 65, 424 + 200
    gameover_rect.left, gameover_rect.top = 318, 424 + 300

    #标志是否超过历史最高分
    is_congratulate = False

    #返回主菜单按钮
    comeback1_img = pygame.image.load("image/comeback1.png").convert_alpha()#返回按钮
    comeback2_img = pygame.image.load("image/comeback2.png").convert_alpha()
    comeback_img = comeback1_img#设置默认图片
    comeback_rect = comeback1_img.get_rect()
    comeback_rect.left, comeback_rect.top = 901 - 100, 897 - 100

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #检测玩家是否按下了暂停按钮
            elif event.type == MOUSEBUTTONDOWN:
                if life_num:
                    #collidepoint(event.pos),自动检测鼠标是否停留在pos内，如果是则返回True
                    if event.button == 1 and paused_rect.collidepoint(event.pos):
                        paused = not paused
                        if paused:
                            pygame.time.set_timer(SUPPLY_TIME, 0)#定时器暂停
                            pygame.mixer.music.pause()#背景音乐暂停
                            pygame.mixer.pause()#所有其他音乐特效暂停
                        else:
                            pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)#定时器开始
                            pygame.mixer.music.unpause()#背景音乐开始
                            pygame.mixer.unpause()#所有其他音乐特效开始

                        
                if life_num == 0:
                    
                    #检测玩家是否按下了退出游戏按钮
                    if event.button == 1 and gameover_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

                    elif event.button == 1 and again_rect.collidepoint(event.pos):
                        main()

                    elif event.button == 1 and comeback_rect.collidepoint(event.pos):
                        menu_sound.play()
                        Menu()
                    

            #检测鼠标是否移动到暂停游戏按钮
            elif event.type == MOUSEMOTION:
                if life_num == 0:
                    if event.type == MOUSEMOTION:
                            if comeback_rect.collidepoint(event.pos):
                                comeback_img = comeback1_img
                            else:
                                comeback_img = comeback2_img
                else:
                    if paused_rect.collidepoint(event.pos):
                        if paused:
                            pause_img = begin2_img
                            paused_rect = begin_rect
                        else:
                            pause_img = stop2_img
                            paused_rect = stop_rect
                    else:
                        if paused:
                            pause_img = begin1_img
                            paused_rect = begin_rect
                        else:
                            pause_img = stop1_img
                            paused_rect = stop_rect

            #引爆炸弹
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False

            #规定时间发放补给56
            elif event.type == SUPPLY_TIME:
                supply_sound.play()
                if choice([False, True]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
                    
            #检测是否为增强弹药时间
            elif event.type == DOUBLE_BULLET_TIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)#关闭定时器
            #无敌时间
            elif event.type == INVINCIBLE_TIME:
                me.invincible = False
                pygame.time.set_timer(INVINCIBLE_TIME, 0)

        #根据玩家得分增加难度
        #提升到难度2
        if level == 1 and score >= 300:
            level = 2
            up_level.play()
            #增加3架小敌机，2架中敌机和1架大敌机
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            #提升敌机的速度
            inc_speed(small_enemies, 1)
        #提升到难度3
        elif level == 2 and score >= 800:
            level = 3
            up_level.play()
            #增加5架小敌机，3架中敌机和1架大敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 1)
            #提升敌机的速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        #提升到难度4
        elif level == 3 and score >= 1500:
            level = 4
            up_level.play()
            #增加5架小敌机，3架中敌机和2架大敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            #提升敌机的速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
            inc_speed(big_enemies, 1)
        #提升到难度5
        elif level == 4 and score >= 2500:
            level = 5
            up_level.play()
            #增加5架小敌机，3架中敌机和2架大敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            #提升敌机的速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
            inc_speed(big_enemies, 1)
        
        screen.blit(background,(0,0))#显示背景
        
        if paused:
            #显示暂停时的界面
            screen.blit(stopping_img, stopping_rect)
            screen.blit(pause_img, paused_rect)
            #显示分数,Ture表示不显示锯齿
            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
            screen.blit(score_text, (10, 5))#在页面左上角显示分数

        if life_num and not paused:
            #检测键盘事件
            key_pressed = pygame.key.get_pressed()#包涵所有键盘事件的布尔值

            #飞机移动
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()

            #绘制炸弹补给并检测玩家是否获得补给56
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, me):#检测我方飞机是否与补给非透明部分碰撞
                    get_supply.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            #绘制子弹补给并检测玩家是否获得补给56
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, me):#检测我方飞机是否与补给非透明部分碰撞
                    bullet_supply.active = False
                    get_supply.play()
                    is_double_bullet = True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 18 * 1000)
                
                
            #发射子弹
            if not(delay % 10):
                #播放子弹的声音
                if is_double_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((me.rect.centerx - 33, me.rect.centery))
                    bullets[bullet2_index + 1].reset((me.rect.centerx + 30, me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % BULLET2_MUN
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % BULLET1_MUN

            #检测子弹是否击中敌机
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            e.hit = True
                            e.energy -= 1
                            if e in mid_enemies or big_enemies:
                                if not e.energy:
                                    e.active = False
                            else:
                                e.active = False
            
            #绘制大型敌机
            for each in big_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        #绘制被打到的画面
                        screen.blit(each.image_hit, each.rect)
                        each.hit= False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)

                    #绘制血槽
                    pygame.draw.line(screen, BLACK, (each.rect.left ,each.rect.top - 5),(each.rect.right, each.rect.top - 5), 2)
                    #当生命大于30%时显示绿色血条，否则显示红色
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5),
                                     2)
                    
                    #即将出现在画面中出现的音效
                    if each.rect.bottom == -50:
                        big_enemy.play(-1)
                else:
                    #毁灭
                    if not(delay % 3):
                        if e3_des_index == 0:
                            big_die.play()#播放死亡音效
                        screen.blit(each.destroy_images[e3_des_index], each.rect)
                        e3_des_index = (e3_des_index + 1) % 6
                        if e3_des_index == 0:
                            big_enemy.stop()
                            score += 100
                            each.reset()
                        

            #绘制中型敌机
            for each in mid_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        #绘制被打到的画面
                        screen.blit(each.image_hit, each.rect)
                        each.hit= False
                    else:
                        screen.blit(each.image, each.rect)

                    #绘制血槽
                    pygame.draw.line(screen, BLACK, (each.rect.left ,each.rect.top - 5),(each.rect.right, each.rect.top - 5), 2)
                    #当生命大于30%显示绿色,否则显示红色
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5),
                                     2)
                    
                else:
                    #毁灭
                    if not(delay % 3):
                        if e2_des_index == 0:
                            big_die.play()#播放死亡音效
                        screen.blit(each.destroy_images[e2_des_index], each.rect)
                        e2_des_index = (e2_des_index + 1) % 4
                        if e2_des_index == 0:
                            score += 60
                            each.reset()

            #绘制小型敌机
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    #毁灭
                    #big_die.play()#播放死亡音效
                    if not(delay % 3):
                        screen.blit(each.destroy_images[e1_des_index], each.rect)
                        e1_des_index = (e1_des_index + 1) % 4
                        if e1_des_index == 0:
                            score += 10
                            each.reset()

            #检测我方飞机是否被撞,并自定义碰撞类型
            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down and not me.invincible:
                me.active = False
                for e in enemies_down:
                    e.active = False
            
            #绘制我方飞机
            if me.active:
                screen.blit(me.image, me.rect)
            else:
                #毁灭
                #big_die.play()#播放死亡音效
                if not(delay % 3):
                    if me_des_index == 0:
                        big_die.play()
                    screen.blit(me.destroy_images[me_des_index], me.rect)
                    me_des_index = (me_des_index + 1) % 5
                    if me_des_index == 0:
                        life_num -= 1
                        me.reset()
                        pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)

            #绘制剩余炸弹数量
            bomb_text = bomb_font.render("x %d" % bomb_num, True, WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_img, (10, height - 10 - bomb_rect.height))
            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))

            #绘制生命数量
            if life_num:
                for i in range(life_num):
                    screen.blit(life_img, (width - 10 - (i + 1)*life_rect.width, height - 10 - life_rect.height))

            #显示分数,Ture表示不显示锯齿
            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
            screen.blit(score_text, (10, 5))#在页面左上角显示分数

            #绘制暂停按钮
            #print(paused_rect)
            screen.blit(pause_img, (797, 10))

            #控制延迟切换图片
            if not(delay % 5):
                switch_image = not switch_image

            delay -= 1
            if not delay:
                delay = 100

        #绘制游戏结束界面
        elif life_num == 0:
            #背景音乐停止
            pygame.mixer.music.stop()
            #停住全部音效
            pygame.mixer.stop()
            #停止发放补给
            pygame.time.set_timer(SUPPLY_TIME, 0)

            if not record_file:
                record_file = True
                #读取历史最高分
                with open("record.txt", "r") as f:
                    record_score = int(f.read())
                if score > record_score:
                    img_num = randint(1, 322)
                    img_num1 = "image2/" + str(img_num) + ".jpg"
                    #print(img_num1)
                    with open(img_num1,"rb") as g:
                        img_data = g.read()
                    with open("img_num1.jpg", "wb") as g:
                        g.write(img_data)
                    score_best = gameover_font.render("Best Score: %s" % str(score), True, WHITE)
                    congratulate = gameover_font1.render("Congratulations on your record!", True, WHITE)
                    is_congratulate = True#标志是否超过历史最高分
                    con_rect = congratulate.get_rect()
                    con_rect.left, con_rect.top = 264 - 50, 486 - 200
                    #print(con_rect.left, con_rect.top)264 486
                    #将记录保存到文件中
                    with open("record.txt", "w") as f:
                        f.write(str(score))
                else:
                    score_best = gameover_font.render("Best Score: %s" % str(record_score), True, WHITE)
                gameover_text = gameover_font.render("Game over!" ,True, WHITE)
                gameover_text_rect = gameover_text.get_rect()
                gameover_text_rect.left, gameover_text_rect.top = 318, 424
            #print(gameover_text_rect.left, gameover_text_rect.top)318 424
            your_score = gameover_font.render("Your Score: %s" % str(score), True, WHITE)
            #绘制结束画面
            if is_congratulate:
                screen.blit(congratulate, con_rect)
            screen.blit(again_img, again_rect)
            screen.blit(gameover_img, gameover_rect)
            screen.blit(score_best,(20,20))
            screen.blit(your_score,(20,80))
            screen.blit(gameover_text, gameover_text_rect)
            screen.blit(comeback_img, comeback_rect)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    try:
        Menu()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
