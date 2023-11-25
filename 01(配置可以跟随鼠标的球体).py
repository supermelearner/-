import turtle as t

class BetterPen(t.Turtle):
    def __init__(self):
        super().__init__()
        t.tracer(False)
        self.speed(0)
        self.begin_poly()
        self.begin_fill()
        self.circle(30)
        self.end_fill()
        self.end_poly()
        t.register_shape("ball", self.get_poly())
        self.shape('ball')
        self.clear()
        t.tracer(True)
        self.penup()

pen_one = BetterPen()

def detectAndMove(event):
    x, y = event.x - 415, 320 - event.y
    pen_one.goto(x, y)




screen = t.Screen()
canvas = screen.getcanvas()
canvas.bind('<Motion>', detectAndMove)	# <Motion> 是 Tkinter 中用于表示鼠标移动的事件类型的标准字符串,将鼠标移动事件（<Motion>）与一个名为 motion 的函数绑定在一起

screen.mainloop()
t.done()