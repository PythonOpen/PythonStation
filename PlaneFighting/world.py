import tkinter
import random as rd
import time
"""
蜜蜂从上向下运动
可以通过键盘上下左右控制
"""
# 步数
step = 0
direction = (1, 1)

x = 0
y = 10


def set_right(e):
    global x
    x += 20


def set_left(e):
    global x
    x -= 20


root_window = tkinter.Tk()
root_window.title("Python开源学习")

root_window.bind('<Key-Left>', set_left)
root_window.bind('<Key-Right>', set_right)
root_window.resizable(width=False, height=False)
# 创建画布
window_canvas = tkinter.Canvas(root_window, width=480, height=600)
window_canvas.pack()


def main():
    global x
    global y
    # 在画布是上面画一个图片
    # 三个步骤
    # 1.定义图片位置
    # 2.创建PhotoImage对象
    # 3.利用create_image函数把图片画上去
    bg_img_name = "../images/background.gif"
    bg_img = tkinter.PhotoImage(file=bg_img_name)
    # tags的作用是，以后我们使用创建好的image可以通过tags使用
    # 函数create_image（a, b, anchor=tkinter.CENTER...),a，b分别为图片放置的位置
    # CENTER表示图片的中心坐标为(a,b）
    window_canvas.create_image(240, 300, anchor=tkinter.CENTER,
                               image=bg_img, tags='bg')

    sp = "../images/smallplane.gif"
    sp_img = tkinter.PhotoImage(file=sp)
    window_canvas.create_image(50, 50, anchor=tkinter.CENTER,
                               image=sp_img, tags='sp')
    ap_move()

    root_window.mainloop()


def ap_move():
    global step
    global x
    global y
    y += 20
    print(x, y)
    window_canvas.move("sp", x, y)

    step += 1
    window_canvas.after(1000, ap_move)


if __name__ == '__main__':
    main()

