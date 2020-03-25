"""
项目分析：
- 构成：
    - 蛇 Snake
    - 食物 Food
    - 世界 World

- 蛇和食物属于整个世界
    class World:
        self.snake
        self.food
    - 上面代码不太友好
    - 我们用另外一个思路分析

- 我们的分析思路
    - 食物是一个独立的事物
    - 蛇也可以人为是一个独立的事物
    - 世界也是，但世界负责显示
"""
import threading
from tkinter import *
import random
import time
import queue


class Food:
    """
    功能:
        1.出现在画面的某一个地
        2.一旦被吃，则增加蛇的分数
    """

    def __init__(self, queue):
        """
        自动产生一个食物
        """
        self.queue = queue
        self.position = None
        self.expos = None
        self.new_food()

    def new_food(self):
        """
        功能：产生一个食物
        产生一个食物的过程就是随机产生一个食物坐标的过程
        :return:
        """
        # 注意横纵作表产生的范围
        # 温故知识点:random.randrange(a, b, c)随机产生a<= number <b间隔为c的数字的整数，c默认是1
        x = random.randrange(5, 490, 10)
        y = random.randrange(5, 290, 10)
        # 需要注意的是，我们的游戏屏幕一般不需要把他设置成正方形

        self.position = x, y  # position存放食物的位置
        self.expos = x - 5, y - 5, x + 5, y + 5
        # 队列，就是一个不能够随意访问的内部元素，只能从头弹出一个元素并只能
        # 从队尾追加元素的list
        # 把一个食物产生的消息放入队列
        # 我的定义是:消息是一个dict，k代表消息类型，v代表此类型的数据
        self.queue.put({"food": self.expos})


class Snake(threading.Thread):
    """
    蛇的功能：
        1.蛇能动，由我们的上下左右按键控制
        2.蛇每次动，都需要重新计算蛇头的位置
        3.检测是否游戏完事的功能
    """

    def __init__(self, world, queue):
        threading.Thread.__init__(self)
        self.world = world
        self.queue = queue
        self.daemon = True
        self.points_earned = 0
        self.snake_points = [(495, 55), (485, 55), (465, 55), (455, 55)]
        self.food = Food(self.queue)
        # 设置初始运动方向
        self.direction = 'Left'
        self.start()

    def run(self):
        """
        一旦启用多线程调用此函数
        要求蛇一直都在跑
        :return:
        """
        if self.world.is_game_over:
            self._delete()

        while not self.world.is_game_over:
            self.queue.put({"move": self.snake_points})
            time.sleep(0.2)
            self.move()

    def move(self):
        """
        负责蛇的移动
        1.重新计算蛇头的作表
        2.当蛇头跟食物相遇，则加分，重新生成食物，通知world，加分
        3.否则，蛇需要动
        :return:
        """
        new_snake_point = self.cal_new_position()  # 重新计算蛇头位置

        # 蛇头位置跟食物位置位置相同
        if self.food.position == new_snake_point:
            self.points_earned += 1  # 得分加1
            self.queue.put({"points_earned": self.points_earned})
            # 生成新的食物
            self.food.new_food()
        else:
            # 需要注意蛇的信息的保存方式
            # 每次移动是删除存放蛇的尾部位置，并且在前面追加
            self.snake_points.pop(0)
            # 判断程序是否退出，因为新的蛇可能撞墙
            self.check_game_over(new_snake_point)
        self.snake_points.append(new_snake_point)

    def cal_new_position(self):
        """
        计算新的 蛇头的位置
        :param self:
        :return:
        """
        last_x, last_y = self.snake_points[-1]
        if self.direction == "Up":  # direction负责储存蛇移动的方向
            new_snake_point = last_x, last_y - 10  # 每次移动的跨度是10像素
        elif self.direction == 'Down':
            new_snake_point = last_x, last_y + 10
        elif self.direction == 'Left':
            new_snake_point = last_x - 10, last_y
        elif self.direction == 'Right':
            new_snake_point = last_x + 10, last_y

        return new_snake_point

    def key_pressed(self, e):
        # keysym是按键的名称
        self.direction = e.keysym

    def check_game_over(self, snake_point):
        """
        判断的依据是蛇头是否和墙相撞
        :param snake_point:
        :return:
        """
        x, y = snake_point[0], snake_point[1]
        if not -5 < x < 505 or not -5 < y < 305 or snake_point in self.snake_points:
            self.queue.put({'game_over': True})


class World(Tk):
    """
    用来模拟曾格格游戏画板
    """

    def __init__(self, queue):
        Tk.__init__(self)

        self.queue = queue
        self.is_game_over = False

        # 定义画布
        self.canvas = Canvas(self, width=500, height=300, bg='gray')
        self.canvas.pack()

        # 画出蛇和食物
        self.snake = self.canvas.create_line((0, 0), (0, 0), fill="black", width=10)
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill="#FFCC4C", outline='#FFCC4C')
        self.points_earned = self.canvas.create_text(450, 20, fill='white', text='SCORE: 0')
        self.queue_handler()

    def queue_handler(self):
        try:
            while True:
                task = self.queue.get(block=False)
                if task.get("game_over"):
                    self.game_over()
                elif task.get("move"):
                    # 生成组成蛇的所有点的列表
                    points = [x for point in task['move'] for x in point]
                    # 重新绘制蛇
                    self.canvas.coords(self.snake, *points)
                # 同理，还需要处理食物，得分
                elif task.get("food"):
                    self.canvas.coords(self.food, *task['food'])
                elif task.get("points_earned"):
                    # 显示最新得分
                    self.canvas.itemconfigure(self.points_earned, text='SCORE: ' +
                                              str(task['points_earned']))
                    self.queue.task_done()

        except queue.Empty:  # 爆出队列为空异常
            if not self.is_game_over:
                # after的含义是，在多少毫秒后调用后面的函数
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        """
        游戏结束，清理现场
        """
        self.is_game_over = True
        self.canvas.create_text(250, 100, fill='white', text='Game Over')
        Button(self.canvas, width=5, height=1, text='Quit', command=self.destroy).place(x=200, y=130)
        Button(self.canvas, width=5, height=1, text='Again', command=self.again).place(x=260, y=130)

    def again(self):
        self.destroy()
        main()


def main():
    q = queue.Queue()
    world = World(q)
    world.title("傻傻的贪吃蛇")
    snake = Snake(world, q)
    # 对该类实行监测按键事件
    world.bind('<Key-Left>', snake.key_pressed)
    world.bind('<Key-Right>', snake.key_pressed)
    world.bind('<Key-Up>', snake.key_pressed)
    world.bind('<Key-Down>', snake.key_pressed)
    world.mainloop()


if __name__ == "__main__":
    main()
