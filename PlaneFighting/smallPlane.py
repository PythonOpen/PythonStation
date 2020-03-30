from PlaneFighting import config
from PlaneFighting import actor
import tkinter as tk


class SmallPlane(actor.Actor):
    """
    移动的敌机 - 小飞机
    """

    def __init__(self, root, canvas, position, x, y, tags):
        super(SmallPlane, self).__init__(root, canvas, position, x, y, tags,
                                         config.image_smallplane_width,
                                         config.image_smallplane_height, True)

        # 移动者的移动步长
        self.steps = [config.step_length_smallplane_x, config.step_length_smallplane_y]

        # 移动方向，向下
        self.move_direction = [0, 1]
        # 移动着加载背景图像
        self.bg_image_fullname = config.images_path +\
                                 config.filename_smallplane +\
                                 config.filename_suffix

        self.bg_image = tk.PhotoImage(file=self.bg_image_fullname)

    def exec_move(self):
        if self.nw[1] < config.window_boundary_row:
            # Y轴边界之内正常移动
            x = self.steps[0] * self.move_direction[0]
            y = self.steps[1] * self.move_direction[1]
            self.base_move(self.bg_image_tags, x, y)



