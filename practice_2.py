# -*- coding: utf-8 -*-
import turtle as te
import time
from __package__.te_draw import TE_Draw, RandDraw, RandAnime
 
te.tracer(10)#用這行可瞬間作畫
te.setup(TE_Draw.Width, TE_Draw.Height, 0, 0)
te.pensize(1)
te.speed('fast')
te.penup()
 

def face(x,y):
    """
    給定下巴位置，繪製一張正臉
    (參考https://www.youtube.com/watch?v=Uoe4gmihCaA 畫臉部比例)
    """
    te.color("black", "#F3EEEB")
    te.begin_fill()
    TE_Draw.moveTo(x,y)
    TE_Draw.lineRel([(-70, -45),(-30, -120)])
    te.setheading(90)
    te.circle(-100, extent=180)
    TE_Draw.lineRel([(-30, 120), (-70, 45)])
    te.end_fill()
    
def eye(x,y):
    """
    給定眼睛左上角位置，畫出一隻眼睛
    """
    te.color("black")
    te.pensize(2)
    TE_Draw.moveTo(x,y)
    te.begin_fill()
    TE_Draw.lineRel([(15, -7)])
    TE_Draw.curveRel([(4, -1), (26, -2), (30, 0)])
    TE_Draw.curveRel([(10, 3), (12, 7)])
    
    te.color("#D1D1D1")
    te.pensize(1)
    TE_Draw.curveRel([(2, 27), (-1, 30)])
    TE_Draw.curveRel([(-39, 5), (-44, 1)])
    TE_Draw.lineTo([(x,y)])
    te.end_fill()
    
    te.color("#0C1631")    
    TE_Draw.moveTo(x+10,y-2)
    te.begin_fill()
    TE_Draw.lineRel([(45, 0), (-2, 33), (-36,0)])
    TE_Draw.lineTo([(x+10,y-2)])
    te.end_fill()
    
    te.color("white")
    TE_Draw.moveTo(x+45,y)
    te.setheading(270)
    te.begin_fill()
    te.circle(5)
    te.end_fill()
    
    te.color("black")
    TE_Draw.moveTo(x+35,y)
    te.setheading(0)
    te.begin_fill()
    te.circle(-15)
    te.end_fill()
    
def hair():
    pt = (280,50)
    RandAnime.hair2(pt)

    


    
te.colormode(255)
face(285, 312)
eye(206, 162)
eye(302, 164)

hair()

# 鼻子、嘴
#te.pencolor("black")
#TE_Draw.moveTo(280, 224)
#TE_Draw.curveRel([(4, 7), (1, 9)])
#TE_Draw.moveTo(281, 260)
#TE_Draw.curveRel([(10, -1), (10, 2)])


te.hideturtle()
te.update()
te.done()