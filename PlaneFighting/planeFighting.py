import tkinter

if __name__ == '__main__':
    root_window = tkinter.Tk()
    # 固定窗口大小
    root_window.resizable(width=False, height=False)
    # 创建画布
    window_canvas = tkinter.Canvas(root_window, width=480, height=600)
    window_canvas.pack()
    # 在画布是上面画一个图片
    # 三个步骤
    # 1.定义图片位置
    # 2.创建PhotoImage对象
    # 3.利用create_image函数把图片画上去
    bg_img_name = "./images/background.gif"
    bg_img = tkinter.PhotoImage(file=bg_img_name)
    # tags的作用是，以后我们使用创建好的image可以通过tags使用
    # 函数create_image（a, b, anchor=tkinter.CENTER...),a，b分别为图片放置的位置
    # CENTER表示图片的中心坐标为(a,b）
    window_canvas.create_image(240, 300, anchor=tkinter.CENTER,
                               image=bg_img, tags='bg')

    bg_img_name = "./images/bee.gif"
    bee_img = tkinter.PhotoImage(file=bg_img_name)
    window_canvas.create_image(0, 0, anchor=tkinter.CENTER,
                               image=bee_img, tags='bee')
    root_window.mainloop()
