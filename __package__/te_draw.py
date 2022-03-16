# -*- coding: utf-8 -*-
import turtle as te
import numpy as np
te.TurtleScreen._RUNNING = True

class TE_Draw():
    """
    名詞解說:
    SVG座標指的是以左上角為(0, 0)的座標系統，
    x軸正方向是向右，y軸正方向是向下。
    """
    WriteStep = 15  # 贝塞尔函数的取样次数
    Width = 600  # 界面宽度
    Height = 500  # 界面高度
    
    @staticmethod
    def _one_bezier(p1, p2, t):
        # 一階貝茲曲線，由兩點連成的直線，t屬於實數[0,1]區間，其中point為np.array
        return p1 * (1 - t) + p2 * t
    
    @staticmethod
    def _bezier(points, t):
        """
        n階貝茲曲線，t屬於實數[0,1]區間，實作方法參考
        wiki的遞迴公式: https://zh.wikipedia.org/wiki/%E8%B2%9D%E8%8C%B2%E6%9B%B2%E7%B7%9A，
        回傳一個座標點
        """
        assert 2<=len(points)<=6, "only support 2~6 points bezier curve"
        if len(points)==2:
            return TE_Draw._one_bezier(points[0], points[1], t)
        return (1 - t) * TE_Draw._bezier(points[:-1], t) +  t * TE_Draw._bezier(points[1:], t)
    
    @staticmethod
    def draw_bezier(points):
        """
        給定k個points, 以svg座標表示，畫出k-1階的beziercurve
        """
        TE_Draw.moveTo(*points[0])
        for t in range(0, TE_Draw.WriteStep + 1):
            x, y = TE_Draw._bezier(np.array(points), t / TE_Draw.WriteStep)
            TE_Draw.lineTo(x, y)
        
    @staticmethod
    def curveTo(points):
        """
        從當前點出發，依points方向畫bezier curve
        """
        TE_Draw.draw_bezier([TE_Draw.cur_svg()] + points)
        
    @staticmethod
    def curveRel(points):
        """
        從當前點為基準，依相對坐標畫bezier curve
        """
        cur_x, cur_y = TE_Draw.cur_svg()
        TE_Draw.draw_bezier([(cur_x, cur_y)] + [(cur_x+x, cur_y+y) for x,y in points])

    
    @staticmethod
    def cur_svg():
        # 取得畫筆當前點的svg座標
        return te.xcor() + TE_Draw.Width/2,  TE_Draw.Height / 2 - te.ycor()
    
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

    @staticmethod
    def lineRel(dx, dy): 
        # 連接當前點和相對坐標（dx，dy）的點
        cur_x, cur_y = TE_Draw.cur_svg()
        TE_Draw.line(cur_x, cur_y, cur_x+dx, cur_y+dy)


    @staticmethod
    def lineTo(x, y):
        # 連接當前點svg坐標（x，y）
        te.pendown()
        te.goto(*TE_Draw.svg_to_Cart(x,y))
        te.penup()
    
    @staticmethod
    def horizontalTo(x): 
        # 畫水平線到x座標
        te.pendown()
        te.setx(x - TE_Draw.Width / 2)
        te.penup()
    
    @staticmethod
    def horizontalRel(dx):  
        # 畫水平線到相對位置dx
        TE_Draw.lineRel(dx, 0)
    
    @staticmethod
    def verticalTo(y):
        # 畫垂直線到y座標
        te.pendown()
        te.sety(y + TE_Draw.Height / 2)
        te.penup()
    
    @staticmethod
    def verticalRel(dy):
        # 畫垂直線到相對位置dy
        TE_Draw.lineRel(0, dy)
    
    @staticmethod
    def polyline(points):
        # 畫svg坐標下的折線
        assert points
        TE_Draw.moveTo(*points[0])
        for i in range(1, len(points)):
            TE_Draw.lineTo(*points[i])


if __name__=='__main__':
    te.speed('slow')
    te.setup(TE_Draw.Width, TE_Draw.Height, 0, 0)
    TE_Draw.moveTo(300,300)
    TE_Draw.line(100,200,100,100)
    TE_Draw.horizontalTo(300)
    TE_Draw.verticalRel(-30)
    TE_Draw.moveTo(300,400)
    TE_Draw.horizontalRel(-100)
    TE_Draw.polyline([(195, 49), (175.5, 106.5), (202.522, 49)])
    TE_Draw.verticalTo(0)
    TE_Draw.draw_bezier([(90, 200), (150, 250), (250,350),(100,400)])
    TE_Draw.curveRel([(100, -50), (200, 0)])
    te.done()
