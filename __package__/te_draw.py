# -*- coding: utf-8 -*-
import turtle as te
te.TurtleScreen._RUNNING = True

class TE_Draw():
    """
    名詞解說:
    SVG座標指的是以左上角為(0, 0)的座標系統，
    x軸正方向是向右，y軸正方向是向下。
    """
    WriteStep = 15  # 贝塞尔函数的取样次数
    Speed = 5
    Width = 600  # 界面宽度
    Height = 500  # 界面高度
    Xh = 0  # 记录前一个贝塞尔函数的手柄
    Yh = 0
     
#    def Bezier(p1, p2, t):  # 一阶贝塞尔函数
#        return p1 * (1 - t) + p2 * t
#     
#    def Bezier_2(x1, y1, x2, y2, x3, y3):  # 二阶贝塞尔函数
#        te.goto(x1, y1)
#        te.pendown()
#        for t in range(0, WriteStep + 1):
#            x = Bezier(Bezier(x1, x2, t / WriteStep),
#                       Bezier(x2, x3, t / WriteStep), t / WriteStep)
#            y = Bezier(Bezier(y1, y2, t / WriteStep),
#                       Bezier(y2, y3, t / WriteStep), t / WriteStep)
#            te.goto(x, y)
#        te.penup()
#     
#    def Bezier_3(x1, y1, x2, y2, x3, y3, x4, y4):  # 三阶贝塞尔函数
#        x1 = -Width / 2 + x1
#        y1 = Height / 2 - y1
#        x2 = -Width / 2 + x2
#        y2 = Height / 2 - y2
#        x3 = -Width / 2 + x3
#        y3 = Height / 2 - y3
#        x4 = -Width / 2 + x4
#        y4 = Height / 2 - y4  # 坐标变换
#        te.goto(x1, y1)
#        te.pendown()
#        for t in range(0, WriteStep + 1):
#            x = Bezier(Bezier(Bezier(x1, x2, t / WriteStep), Bezier(x2, x3, t / WriteStep), t / WriteStep),
#                       Bezier(Bezier(x2, x3, t / WriteStep), Bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
#            y = Bezier(Bezier(Bezier(y1, y2, t / WriteStep), Bezier(y2, y3, t / WriteStep), t / WriteStep),
#                       Bezier(Bezier(y2, y3, t / WriteStep), Bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)
#            te.goto(x, y)
#        te.penup()
    
    @staticmethod
    def svg_to_Cart(x,y):
        """
        將svg座標轉換成較常見的笛卡兒座標。
        因為電腦慣用座標為svg座標，turtle用的為笛卡兒座標，
        做此轉換以符合電腦慣用座標。
        """
        return -TE_Draw.Width / 2 + x, TE_Draw.Height / 2 - y
        
    @staticmethod
    def moveTo(x, y):
        # 移動到svg座標(x,y)
        te.penup()
        te.goto(*TE_Draw.svg_to_Cart(x,y))
    
    @staticmethod
    def line(x1, y1, x2, y2): 
        # 連接svg坐標下兩點
        TE_Draw.moveTo(x1, y1)
        TE_Draw.lineTo(x2, y2)

     
    def lineRel(dx, dy): 
        # 連接當前點和相對坐標（dx，dy）的點
        te.pendown()
        te.goto(te.xcor() + dx, te.ycor() - dy)
        te.penup()
     
    def lineTo(x, y):
        # 連接當前點svg坐標（x，y）
        te.pendown()
        te.goto(*TE_Draw.svg_to_Cart(x,y))
        te.penup()
     
    def horizontalTo(x): 
        # 畫水平線到x座標
        te.pendown()
        te.setx(x - TE_Draw.Width / 2)
        te.penup()
     
    def horizontalRel(dx):  
        # 畫水平線到相對位置dx
        TE_Draw.lineRel(dx, 0)
        
#     
#    def vertical(dy):  # 做到相对纵坐标为dy的垂直线
#        te.seth(-90)
#        te.pendown()
#        te.fd(dy)
#        te.penup()
#        te.seth(0)
#     
#    def polyline(x1, y1, x2, y2, x3, y3):  # 做svg坐标下的折线
#        te.penup()
#        te.goto(-Width / 2 + x1, Height / 2 - y1)
#        te.pendown()
#        te.goto(-Width / 2 + x2, Height / 2 - y2)
#        te.goto(-Width / 2 + x3, Height / 2 - y3)
#        te.penup()
#     
#    def Curveto(x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到（x，y）
#        te.penup()
#        X_now = te.xcor() + Width / 2
#        Y_now = Height / 2 - te.ycor()
#        Bezier_3(X_now, Y_now, x1, y1, x2, y2, x, y)
#        global Xh
#        global Yh
#        Xh = x - x2
#        Yh = y - y2
#     
#    def curveto_r(x1, y1, x2, y2, x, y):  # 三阶贝塞尔曲线到相对坐标（x，y）
#        te.penup()
#        X_now = te.xcor() + Width / 2
#        Y_now = Height / 2 - te.ycor()
#        Bezier_3(X_now, Y_now, X_now + x1, Y_now + y1,
#                 X_now + x2, Y_now + y2, X_now + x, Y_now + y)
#        global Xh
#        global Yh
#        Xh = x - x2
#        Yh = y - y2
#     
#    def Smooth(x2, y2, x, y):  # 平滑三阶贝塞尔曲线到（x，y）
#        global Xh
#        global Yh
#        te.penup()
#        X_now = te.xcor() + Width / 2
#        Y_now = Height / 2 - te.ycor()
#        Bezier_3(X_now, Y_now, X_now + Xh, Y_now + Yh, x2, y2, x, y)
#        Xh = x - x2
#        Yh = y - y2
#     
#    def smooth_r(x2, y2, x, y):  # 平滑三阶贝塞尔曲线到相对坐标（x，y）
#        global Xh
#        global Yh
#        te.penup()
#        X_now = te.xcor() + Width / 2
#        Y_now = Height / 2 - te.ycor()
#        Bezier_3(X_now, Y_now, X_now + Xh, Y_now + Yh,
#                 X_now + x2, Y_now + y2, X_now + x, Y_now + y)
#        Xh = x - x2
#        Yh = y - y2

if __name__=='__main__':
    te.speed('slowest')
    te.setup(TE_Draw.Width, TE_Draw.Height, 0, 0)
    TE_Draw.moveTo(300,300)
    TE_Draw.line(100,200,100,100)
    TE_Draw.horizontalTo(300)
    TE_Draw.moveTo(300,400)
    TE_Draw.horizontalRel(-100)
    te.done()
