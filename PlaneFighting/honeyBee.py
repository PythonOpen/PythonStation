from PlaneFighting import config
from PlaneFighting import actor
import tkinter as tk
import random


class HoneyBee(actor.Actor):
    """
    小蜜蜂
    """

    def __init__(self, root, canvas, position, x, y, tags):
        super(HoneyBee, self).__init__(root, canvas, position, x, y, tags,
                                         config.image_bee_width,
                                         config.image_bee_height, True)

        # 移动者的移动步长
        self.steps = [random.choice([-1, 1])*config.step_length_bee_x, config.step_length_bee_y]

        # 移动方向，向下,左/右运动
        self.move_direction = [-1, 0, 1]
        # 移动着加载背景图像
        self.bg_image_fullname = config.images_path + config.filename_bee + config.filename_suffix

        self.bg_image = tk.PhotoImage(file=self.bg_image_fullname)

    def exec_move(self):
        if self.nw[0] < config.window_boundary_col\
                or self.ne[0] > config.window_boundary_col - self.steps[0]:
            # 左右碰壁时x轴反向
            x = self.steps[0] * self.move_direction[0]
            y = self.steps[1] * self.move_direction[1]
        if self.nw[1] < config.window_boundary_row:
            # Y轴边界之内正常移动
            x = self.steps[0] * self.move_direction[1]
            y = self.steps[1] * self.move_direction[2]
            self.base_move(self.bg_image_tags, x, y)
        else:
            # Y轴边界之外错误处理
            self.base_move(self.bg_image_tags, 0, -config.window_boundary_row)

    # 获取死亡图片
    def get_dead_images(self):
        img = []
        if self.do_dead_play:
            for i in self.dead_image_index:
                image_fullname = config.images_path + config.filename_bee + str(i) + config.filename_suffix
                image = tk.PhotoImage(file=image_fullname)
                img.append(image)
            return img
