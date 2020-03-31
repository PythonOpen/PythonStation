from PlaneFighting import actor, sky, bigPlane, smallPlane, honeyBee, heroPlane, bullet, config
import time
import tkinter
import random as rd


# 创建天空背景
def create_sky(root, canvas):
    sky_1 = sky.Sky(root, canvas,
                    config.initial_anchor_sky_1,
                    config.initial_anchor_sky_x_1,
                    config.initial_anchor_sky_y_1, "Sky01")

    sky_2 = sky.Sky(root, canvas, tkinter.SW, sky_1.nw[0], sky_1.nw[1], "Sky02")

    tmp_canvas_img = canvas.create_image(sky_1.anchor_x,
                                         sky_1.anchor_y,
                                         anchor=sky_1.anchor,
                                         image=sky_1.bg_image,
                                         tags=sky_1.bg_image_tags)

    sky_1.set_canvas_image(tmp_canvas_img)
    tmp_canvas_img = canvas.create_image(sky_2.anchor_x,
                                         sky_2.anchor_y,
                                         anchor=sky_2.anchor,
                                         image=sky_2.bg_image,
                                         tags=sky_2.bg_image_tags)
    sky_2.set_canvas_image(tmp_canvas_img)
    return [sky_1, sky_2]


# 移动的天空，模拟前行
def move_sky(canvas, sky_1, sky_2):
    # 若sky_1已消失在窗口范围后，从重新移动到sky_2的上方
    if sky_1.nw[1] >= config.window_boundary_row - sky_1.steps[1]:
        canvas.move(sky_1.bg_image_tags, 0, -(config.image_sky_height+sky_1.nw[1]))
        sky_1.update_positions(0, -(config.image_sky_height+sky_1.nw[1]))
    # 若sky_2已消失在窗口范围后，从重新移动到sky_1的上方
    elif sky_2.nw[1] >= config.window_boundary_row - sky_2.steps[1]:
        canvas.move(sky_2.bg_image_tags, 0, -(config.image_sky_height+sky_2.nw[1]))
        sky_2.update_positions(0, -(config.image_sky_height+sky_2.nw[1]))
    # 正常移动
    else:
        sky_1.exec_move()
        sky_2.exec_move()


# 创建大飞机
def create_big_plane(root, canvas, enemy_list):
    # 大飞机
    # x轴初始值为随机数
    x = rd.randint(0, config.window_boundary_col - config.image_bigplane_width)
    big_plane = bigPlane.BigPlane(root, canvas, tkinter.SW, x, 0, "BigPlane")
    tmp_canvas_img = canvas.create_image(big_plane.anchor_x,
                                         big_plane.anchor_y,
                                         anchor=big_plane.anchor,
                                         image=big_plane.bg_image,
                                         tags=big_plane.bg_image_tags)
    big_plane.set_canvas_image(tmp_canvas_img)
    enemy_list.insert(0, big_plane)
    config.total_number_bigplane += 1


# 创建小飞机
def create_small_plane(root, canvas, enemy_list):
    # 小飞机
    # x轴初始值为随机数
    x = rd.randint(0, config.window_boundary_col - config.image_samllplane_width)
    small_plane = bigPlane.BigPlane(root, canvas, tkinter.SW, x, 0, "SmallPlane")
    tmp_canvas_img = canvas.create_image(small_plane.anchor_x,
                                         small_plane.anchor_y,
                                         anchor=small_plane.anchor,
                                         image=small_plane.bg_image,
                                         tags=small_plane.bg_image_tags)
    small_plane.set_canvas_image(tmp_canvas_img)
    enemy_list.insert(0, small_plane)
    config.total_number_smallplane += 1


# 创建小蜜蜂
def create_honeybee(root, canvas, enemy_list):
    # 小蜜蜂
    # x轴初始值为随机数
    x = rd.randint(0, config.window_boundary_col - config.image_bee_width)
    bee = honeyBee.HoneyBee(root, canvas, tkinter.SW, x, 0, "HoneyBee")
    tmp_canvas_img = canvas.create_image(bee.anchor_x,
                                         bee.anchor_y,
                                         anchor=bee.anchor,
                                         image=bee.bg_image,
                                         tags=bee.bg_image_tags)
    bee.set_canvas_image(tmp_canvas_img)
    enemy_list.insert(0, bee)
    config.total_number_bee += 1


# 创建英雄机
def create_hero(root, canvas, lives):
    hero = heroPlane.HeroPlane(root, canvas,
                               config.initial_anchor_hero,
                               config.initial_anchor_hero_x,
                               config.initial_anchor_hero_y,
                               "HeroPlane01", lives)
    tmp_canvas_img = canvas.create_image(hero.anchor_x,
                                         hero.anchor_y,
                                         anchor=hero.anchor,
                                         image=hero.bg_image,
                                         tags=hero.bg_image_tags)
    hero.set_canvas_image(tmp_canvas_img)
    return hero


# 创建子弹
def create_bullet_tags(root, canvas, anchor, x, y, tags):
    blt = bullet.Bullet(root, canvas, anchor, x, y, tags)
    tmp_canvas_img = canvas.create_image(blt.anchor_x,
                                         blt.anchor_y,
                                         anchor=blt.anchor,
                                         image=blt.bg_image,
                                         tags=blt.bg_image_tags)
    blt.set_canvas_image(tmp_canvas_img)
    return blt


# 从英雄机头部位置发射子弹
def create_bullet(root, canvas, mother, tag_id):
    # 每帧子弹
    blt_1 = create_bullet_tags(root, canvas,
                               tkinter.CENTER,
                               mother.nw[0]+mother.width/2,
                               mother.nw[1],
                               "BulletMid"+str(tag_id))
    return blt_1


# 创建敌机
def create_enemys(root, canvas):
    # 敌机列表中插入新敌机
    enemy_list = []
    create_big_plane(root, canvas, enemy_list)
    create_small_plane(root, canvas, enemy_list)
    create_honeybee(root, canvas, enemy_list)
    return enemy_list


# 移动敌机
def move_enemy(root, canvas, enemy):
    enemy_list = enemy
    # global ENEMY_DEAD_INDEX

    for item in enemy_list:
        if item.state is config.life_status_alive:
            item.exec_move()
        else:
            item.errors_happened()
        # else:
        #     dead_image = item.get_dead_images()[ENEMY_DEAD_INDEX]
        #     print("ENEMY_DEAD_INDEX: ", ENEMY_DEAD_INDEX)
        #     canvas.create_image(item.nw[0], item.nw[1],
        #                         anchor=tkinter.NW,
        #                         image=dead_image,
        #                         tags="PlayDeath")
        #     root.update()
        #     ENEMY_DEAD_INDEX += 1
