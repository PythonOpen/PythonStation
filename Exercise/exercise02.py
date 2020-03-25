# Tkinter-计算器
"""
- 模拟系统的计算器功能
- 实现一个简单的具有加减法等操作的计算器
- 使用tkinter
- 操作步骤
    - 画GUI
    - 给每个空间配置相应的事件
    - 写逻辑代码
"""
# 第一步：画出图形界面
from tkinter import *
# 计算器上半部(显示部分)
root = Tk()
# 定义面板的大小
root.geometry('250x380')
root.title("Python开源学习")
# 定义面板
# bg代表背景颜色(background), #dddddd是十六进制表示颜色的一个串
frame_show = Frame(width=300, height=150, bg='#dddddd')
frame_show.pack()

# 定义顶部区域
# 定义一个字符串类，可实现一些特定功能
# anchor:定义控件的锚点，e代表右边
# font代表字体
sv = StringVar()
sv.set('00')
show_label = Label(frame_show, textvariable=sv,
                   bg='green', width=10, height=1,
                   font=('黑体', 20, 'bold'),
                   justify=LEFT, anchor='e')\
                    .pack(padx=12, pady=10)
frame_show.pack()

# 逻辑编写
"""
考虑以下几种情况
1.按下数字
2.按下操作符号
3.只考虑两个操作数操作
"""
num1 = ''
num2 = ''
operator = None


def delete():
    print("我被删除了")


def fan():
    print("烦了")


def clear():
    print("克利尔")


def change(num):
    """
    按下一个数字需要考虑两种情况:
    1.数字属于第一种操作数
    2.数字属于第二种操作数
    3.判断是否属于第一个操作数，可以通过operator判断
    :param num:
    :return:
    """
    global num1
    global num2
    global operator
    # 加入操作数是None，表明肯定是第一个操作数
    if not operator:
        num1 = num1 + num
        sv.set(num1)
        # 如何是第一个操作数，则只显示第一个操作数
    else:
        num2 = num2 + num
        # 如果是第二个操作数，则应该显示完整的计算式子
        sv.set(num1+operator+num2)


def operation(op):
    global operator
    global num1
    global num2
    if op in ['+', '-', 'x', '÷'] and num1 != '':
        operator = op
        sv.set(num1 + operator)
    else:  # 认为是按下的是等于号
        if num2 == '':
            rst = int(num1)
        elif operator == "+":
            rst = int(num1) + int(num2)
        elif operator == "-":
            rst = int(num1) - int(num2)
        elif operator == "x":
            rst = int(num1) * int(num2)
        elif operator == "÷":
            rst = int(num1) / int(num2)
        # str(rst)[:10]为取前面的10位数
        sv.set(str(rst)[:10])
        operator = None
        num1 = ''
        num2 = ''


# 计算器下半部（按钮）
frame_bord = Frame(width=400, height=350, bg='#cccccc')
button_clear = Button(frame_bord, text="C", width=5, height=1,
                      command=clear).grid(row=0, column=0)
button_fan = Button(frame_bord, text="±", width=5, height=1,
                    command=fan).grid(row=0, column=1)
button_ce = Button(frame_bord, text="CE", width=5, height=1,
                   command=clear).grid(row=0, column=2)
button_plus_ = Button(frame_bord, text="+", width=5, height=1,
                      command=lambda: operation("+")).grid(row=0, column=3)
# 此处用到lambda函数，lambda函数用法-lambda a: b()表示用a代表b()函数
b_1 = Button(frame_bord, text="1", width=5, height=1,
             command=lambda: change("1")).grid(row=1, column=0)
b_2 = Button(frame_bord, text="2", width=5, height=1,
             command=lambda: change("2")).grid(row=1, column=1)
b_3 = Button(frame_bord, text="3", width=5, height=1,
             command=lambda: change("3")).grid(row=1, column=2)
button_minus = Button(frame_bord, text="-", width=5, height=1,
                      command=lambda: operation("-")).grid(row=1, column=3)
b_4 = Button(frame_bord, text="4", width=5, height=1,
             command=lambda: change("4")).grid(row=2, column=0)
b_5 = Button(frame_bord, text="5", width=5, height=1,
             command=lambda: change("5")).grid(row=2, column=1)
b_6 = Button(frame_bord, text="6", width=5, height=1,
             command=lambda: change("6")).grid(row=2, column=2)
button_time = Button(frame_bord, text="x", width=5, height=1,
                     command=lambda: operation("x")).grid(row=2, column=3)
b_7 = Button(frame_bord, text="7", width=5, height=1,
             command=lambda: change("7")).grid(row=3, column=0)
b_8 = Button(frame_bord, text="8", width=5, height=1,
             command=lambda: change("8")).grid(row=3, column=1)
b_9 = Button(frame_bord, text="9", width=5, height=1,
             command=lambda: change("9")).grid(row=3, column=2)
button_divide = Button(frame_bord, text="÷", width=5, height=1,
                       command=lambda: operation("÷")).grid(row=3, column=3)
button_point = Button(frame_bord, text=".", width=5, height=1,
                      command=lambda: change(".")).grid(row=4, column=0)
b_0 = Button(frame_bord, text="0", width=5, height=1,
             command=lambda: change("0")).grid(row=4, column=1)
b_del = Button(frame_bord, text="←", width=5, height=1,
               command=delete).grid(row=4, column=2)
button_equal = Button(frame_bord, text="=", width=5, height=1,
                      command=lambda: operation("=")).grid(row=4, column=3)
frame_bord.pack(padx=10, pady=0)
root.mainloop()
