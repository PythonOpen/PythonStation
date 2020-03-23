'''TKinter项目实战-屏保
# 项目分析
- 屏保可以自己启动，也可以手动启动
- 一旦敲击键盘或者移动鼠标后，或者其他的引发事件，则停止
- 如果屏保是一幅画的话，则没有画框
- 图像的动作是随机的，具有随机性，可能包括颜色，大小，运动方向，变形等
- 整个事件的构成：
    - ScreenSaver:
        - 需要一个canvas, 大小与屏幕一致，没有边框
    - Ball
        - 颜色，大小，多少，运动方向，变形等随机
        - 球能动，可以被调用'''
import random
import tkinter

class RandomBall:
    '''
    定义一个球的类
    '''
    item = None

    def __init__(self, canvas, scrnwidth, scrnheight):
        '''canvas: 画布，所有的内容都应该在画布上呈现出来，此处通过此变量传入
        scrnwidth/scrnheight: 屏幕宽高'''
        self.canvas = canvas
        # 球出现的初始位置要随机
        # xpos表示位置的x坐标
        self.xpos = random.randint(120, int(scrnwidth)-120)
        # ypos表示位置的y坐标
        self.ypos = random.randint(120, int(scrnheight)-120)

        # 定义球的运动速度
        # 模拟运动：不断的擦掉原来画，然后在一个新的地方再重新绘制
        # 此处xvelocity模拟的是x轴方向运动
        self.xvelocity = random.randint(4, 20)

        # 此处yvelocity模拟的是y轴方向运动
        self.yvelocity = random.randint(4, 20)

        #  定义屏幕的大小
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight

        # 球的大小随机
        # 此处球的大小用半径表示
        self.radius = random.randint(20, 120)

        # 定义颜色
        # RGB表示法：三个数字，每个数字的值是0-255之间，表示红绿蓝三个颜色的大小
        # 在某些系统中，之间用英文单词表示也可以， 比如red, green
        # 此处用lanbda表达式
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())

    def create_ball(self):
        '''用构造函数定义的变量值，在canvas上画一个球'''
        # tkinter没有画圆形函数
        # 只有一个画椭圆的函数，画椭圆需要定义两个坐标
        # 在一个长方形内画椭圆，我们只需要定义长方形左上角和右下角就好
        # 求两个坐标的方法是，圆心的坐标，则圆心坐标加减去半径左右下上的坐标
        # 左上角坐标
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        # 右下角坐标
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius

        # 根据两个对角坐标进行画圆
        # fill表示填充颜色
        # outline是外围边框颜色
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        # 移动球的时候，需要控制球的方向
        # 每次移动后，球都是一个新的坐标
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        # 判断球是否撞墙
        # 撞墙了就要回头
        # 在画布上挪动图画
        # 注意撞墙的算法判断
        if self.xpos + self.radius >= self.scrnwidth or self.xpos - self.radius <= 0:
            # 撞到左右墙
            self.xvelocity = - self.xvelocity
        if self.ypos + self.radius >= self.scrnheight or self.ypos - self.radius <= 0:
            # 撞到上下墙
            self.yvelocity = - self.yvelocity
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)

class ScreenSaver:
    '''定义屏保的类,可以被启动'''
    balls = list()

    def __init__(self):
        # 每次启动球的数量随机
        self.num_balls = random.randint(6, 20)
        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)

        # 任何鼠标移动都需要取消
        self.root.bind('<Motion>', self.my_quit)
        # 同理，按动任何键盘都需要退出屏保
        self.root.bind('<KeyPress>', self.my_quit)

        # 得到屏幕大小规格
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        # 创建画布，包括画布的归属，规格
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()
        # self.son_root = tkinter.Toplevel(self.root, width=w/10, height=h/6)
        # self.son_root.withdraw()
        # self.btn1 = tkinter.Button(self.son_root, text="确定", command=self.destroy)
        # self.btn2 = tkinter.Button(self.son_root, text="取消", command=self.stay)
        # self.btn1.place(x=int(w/12/3), y=int(h/8/2))
        # self.btn2.place(x=int(w*2/12/3), y=int(h/8/2))
        # self.son_root.protocol("WM_DELETE_WINDOW", self.stay)

        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, scrnwidth=w, scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()

        # after是200毫秒后启动一个函数，需要启动的函数为第二个参数。
        self.canvas.after(200, self.run_screen_saver)

    def my_quit(self, e):
        # 此处只是利用了事件处理机制
        # 实际上并不关心事件的类型
        # 作业(把带#号的代码注释掉即可)：
        # 此屏保扩展成，一旦捕获事件，则屏保不退出
        # 显示一个button, Button上显示事件类型，点击Button后屏保才退出
        self.root.destroy()
        # self.son_root.wm_deiconify()

    # def destroy(self):
    #     self.root.destroy()
    #
    # def stay(self):
    #     self.son_root.withdraw()

if __name__ == "__main__":
    # 启动屏保
    ScreenSaver()
