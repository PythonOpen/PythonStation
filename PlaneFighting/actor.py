import tkinter
import time
from PlaneFighting import config
"""
完成对飞行物基类的初始化工作
"""


class Actor(object):
    """所有移动者的基本类"""
    def __init__(self, root, canvas, position, x, y, tags, w, h, play):
        """
        :param root:
        :param canvas:
        :param position:
        :param x:
        :param y:
        :param tags:
        :param w:
        :param h:
        :param play: 是否播放死亡动画
        """
        # 窗口及画布
        self.root = root
        self.canvas = canvas
        # 移动者的状态
        self.state = config.life_status_alive
        # 移动者加载背景图像的锚点及对应坐标
        # 默认图片加载到左上角
        self.anchor = position
        self.anchor_x = x
        self.anchor_y = y
        self.width = w
        self.height = h
        # 加载图片的标签
        self.bg_image_tags = tags
        # 击落移动者播放的死亡图像
        self.do_dead_play = play
        self.dead_image_index = [0, 1, 2, 3, 4]
        self.lives_num = 1
        # 当前图片四个角的坐标
        self.nw = self.get_anchor_nw_position()
        self.ne = self.get_anchor_ne_position()
        self.sw = self.get_anchor_sw_position()
        self.se = self.get_anchor_se_position()
        self.center = self.get_anchor_center_position()
        # 画布上图像下标
        self.canvas_img_index = 0

    # 获取左上角坐标值
    def get_anchor_nw_position(self):
        if self.anchor == tkinter.NW:
            return [self.anchor_x, self.anchor_y]
        elif self.anchor == tkinter.NE:
            return [self.anchor_x-self.width, self.anchor_y]
        elif self.anchor == tkinter.SW:
            return [self.anchor_x, self.anchor_y-self.height]
        elif self.anchor == tkinter.SE:
            return [self.anchor_x-self.width, self.anchor_y-self.height]
        elif self.anchor == tkinter.CENTER:
            return [self.anchor_x-self.width/2, self.anchor_y-self.height/2]
        else:
            return [0, 0]

    # 获取右上角坐标值
    def get_anchor_ne_position(self):
        if self.anchor == tkinter.NW:
            return [self.anchor_x+self.width, self.anchor_y]
        elif self.anchor == tkinter.NE:
            return [self.anchor_x, self.anchor_y]
        elif self.anchor == tkinter.SW:
            return [self.anchor_x, self.anchor_y+self.height]
        elif self.anchor == tkinter.SE:
            return [self.anchor_x, self.anchor_y-self.height]
        elif self.anchor == tkinter.CENTER:
            return [self.anchor_x+self.width/2, self.anchor_y-self.height/2]
        else:
            return [0, 0]

    # 获取左下角坐标值
    def get_anchor_sw_position(self):
        if self.anchor == tkinter.NW:
            return [self.anchor_x, self.anchor_y+self.height]
        elif self.anchor == tkinter.NE:
            return [self.anchor_x-self.width, self.anchor_y+self.height]
        elif self.anchor == tkinter.SW:
            return [self.anchor_x, self.anchor_y]
        elif self.anchor == tkinter.SE:
            return [self.anchor_x-self.width, self.anchor_y]
        elif self.anchor == tkinter.CENTER:
            return [self.anchor_x-self.width/2, self.anchor_y+self.height/2]
        else:
            return [0, 0]

    # 获取右下角坐标值
    def get_anchor_se_position(self):
        if self.anchor == tkinter.NW:
            return [self.anchor_x+self.width, self.anchor_y+self.height]
        elif self.anchor == tkinter.NE:
            return [self.anchor_x, self.anchor_y+self.height]
        elif self.anchor == tkinter.SW:
            return [self.anchor_x+self.width, self.anchor_y]
        elif self.anchor == tkinter.SE:
            return [self.anchor_x, self.anchor_y]
        elif self.anchor == tkinter.CENTER:
            return [self.anchor_x-self.width/2, self.anchor_y-self.height/2]
        else:
            return [0, 0]

    def get_anchor_center_position(self):
        if self.anchor == tkinter.NW:
            return [self.anchor_x+self.width/2, self.anchor_y+self.height/2]
        elif self.anchor == tkinter.NE:
            return [self.anchor_x-self.width/2, self.anchor_y+self.height/2]
        elif self.anchor == tkinter.SW:
            return [self.anchor_x+self.width/2, self.anchor_y-self.height/2]
        elif self.anchor == tkinter.SE:
            return [self.anchor_x-self.width/2, self.anchor_y-self.height/2]
        elif self.anchor == tkinter.CENTER:
            return [self.anchor_x, self.anchor_y]
        else:
            return [0, 0]

    # 获取画布上的图片
    def get_canvas_image(self):
        return self.canvas_img_index

    # 删除画布上的图片
    def del_canvas_image(self, tags):
        self.canvas.delete(tags)

    # 指定对象的移动
    def base_move(self, tags, x, y):
        self.canvas.move(tags, x, y)
        self.update_positions(x, y)

    # 更新坐标值
    def update_positions(self, x, y):
        for i in [self.nw, self.ne, self.se, self.sw, self.center]:
            i[0] += x
            i[1] += y

    # 设置当前生命之
    def set_lives_num(self, num):
        self.lives_num = num

    # 更改生命状态
    def update_life_status(self):
        self.lives_num -= 1
        if self.lives_num <= 0:
            self.state = config.life_status_dead
        else:
            self.state = config.life_status_alive
