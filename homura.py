# -*- coding: utf-8 -*-
import turtle as te
import time
from __package__.te_draw import TE_Draw
 
te.tracer(10)#用這行可瞬間作畫
te.setup(TE_Draw.Width, TE_Draw.Height, 0, 0)
te.pensize(1)
te.speed('slow')
te.penup()
 
# 图层_2
te.color("black", "#F2F2F2")  # 外套
TE_Draw.moveTo(61, 462)
te.begin_fill()
TE_Draw.curveRel([(12, -41), (27, -58)])
TE_Draw.curveRel([(-6, -36), (6, -118),(9, -132)])
TE_Draw.curveRel([(-15, -27), (-23, -51),(-26, -74)])
TE_Draw.curveRel([(4, -66), (38, -105), (65, -149)])
TE_Draw.horizontalTo(486)
TE_Draw.curveRel([(12, 24), (40, 99), (33, 114)])
TE_Draw.curveRel([(39, 82), (55, 129), (39, 144)])
TE_Draw.curveRel([(-31, 23), (-39, 28), (-51,65)])
TE_Draw.lineRel(50, 92)
TE_Draw.horizontalTo(445)
TE_Draw.curveRel([(-29, -38), (-31, -46), (47, -153),(41,-165)])
TE_Draw.curveTo([(355, 178), (340, 176), (272, 63), (264, 64)])
TE_Draw.curveRel([(-29, 67), (-27, 73)])
TE_Draw.curveTo([(99, 292), (174, 428), (173, 439),(165,462)])
TE_Draw.lineTo(61, 462)
te.end_fill()
 
TE_Draw.moveTo(60.5, 461.5)  # 阴影
te.color("black", "#D3DFF0")
te.begin_fill()
TE_Draw.curveRel([(17, -42), (27, -59)])
TE_Draw.curveRel([(-6, -33), (6, -128), (10, -133)])
TE_Draw.curveRel([(-15, -10), (-27, -75)])
te.pencolor("#D3DFF0")
TE_Draw.curveRel([(12, 11), (83, 156)])
te.pencolor("black")
TE_Draw.curveRel([(12, 75), (19, 86), (18, 97),(11,111)])
TE_Draw.horizontalTo(60.5)
te.end_fill()
 
TE_Draw.moveTo(444.5, 464)
te.begin_fill()
TE_Draw.curveRel([(-29, -36), (-31, -46),(24,-128)])
te.pencolor("#D3DFF0")
TE_Draw.curveRel([(86, -48), (96, -55)])
TE_Draw.curveTo([(563.5, 297.5), (570.5, 299.5), (518.5, 334)])
te.pencolor("black")
TE_Draw.curveRel([(-2, 16), (-12, 33), (-12, 37),(38,129)])
TE_Draw.horizontalTo(444.5)
te.end_fill()
 
TE_Draw.moveTo(195, 49)
te.begin_fill()
te.pencolor("#D3DFF0")
TE_Draw.polyline([(195, 49), (175.5, 106.5), (202.522, 49)])
te.pencolor("black")
TE_Draw.horizontalTo(195)
te.pencolor("#D3DFF0")
te.end_fill()

 
TE_Draw.moveTo(328, 49)
te.begin_fill()
te.pencolor("#D3DFF0")
TE_Draw.curveRel([(11, 121), (13, 128), (24, 130), (67,165)])
TE_Draw.lineRel(-40, -165.087)
te.pencolor("black")
TE_Draw.lineTo(328, 49)
te.pencolor("#D3DFF0")
te.end_fill()

 
te.pencolor("black")
TE_Draw.line(94.5, 397.5, 107.5, 373.5)  # 皱纹
TE_Draw.line(122.5, 317.5, 95.875, 275)
TE_Draw.line(122.5, 341.5, 141.5, 402.5)
TE_Draw.line(141.5, 409.5, 153.5, 431.5)
TE_Draw.line(340, 49, 360.5, 144)
TE_Draw.line(478.5, 95.5, 518.5, 161.5)
TE_Draw.line(518.5, 332.5, 460.5, 359.5)
TE_Draw.polyline([(506.5, 369.5), (493.5, 402.5), (502.5, 443.5)])
TE_Draw.moveTo(530, 429)
TE_Draw.curveRel([(4, 16), (-5, 33)])
 
# 图层_3
te.color("black", "#2b1d2a")  # 外套内侧
TE_Draw.moveTo(225, 462)
te.begin_fill()
TE_Draw.horizontalTo(165)
TE_Draw.curveRel([(9, -15), (8, -25)])
TE_Draw.curveRel([(-47, -126), (6, -212), (12, -225)])
TE_Draw.curveTo([(185, 305), (202, 428), (225, 462)])
te.end_fill()


 
TE_Draw.moveTo(390, 462)
te.begin_fill()
TE_Draw.curveRel([(10, -23), (34, -180), (35, -222)])
TE_Draw.curveRel([(7, 4), (54, 45), (61, 61),(-11,179)])
TE_Draw.curveRel([(5, 15),(31, 45)])
TE_Draw.lineTo(390, 462)
te.end_fill()


# 图层_4
te.color("#2b1d29")  # 外套内侧
TE_Draw.moveTo(225, 462)
te.begin_fill()
TE_Draw.curveRel([(-28, -50), (-40, -166), (-40, -250)])
TE_Draw.curveRel([(6, 51), (-6, 87), (45, 106)])
TE_Draw.curveRel([(64, 27), (89, 24)])
TE_Draw.curveRel([(49, -18), (56, -20)])
TE_Draw.curveRel([(50, -10), (51, -85)])
TE_Draw.curveRel([(0, 29), (-25, 201), (-36, 225)])
TE_Draw.lineTo(225, 462)
te.end_fill()


# 图层_5
te.color("black", "#3D3D3D")  # 衣服
TE_Draw.moveTo(225, 462)
te.begin_fill()
TE_Draw.curveRel([(-5, -5), (-22, -53), (-23, -70)])
TE_Draw.lineRel(32, -13)
TE_Draw.curveRel([(3, -25), (6, -28), (12, -36),(28,-48)])
TE_Draw.verticalRel(-2)
TE_Draw.curveRel([(45, 20), (64, 14), (94, 1)])
TE_Draw.verticalRel(2)
TE_Draw.curveRel([(8, -2), (17, 4), (17,10), (15,13)])
TE_Draw.curveRel([(10, 10), (10, 29), (11, 33)])
TE_Draw.curveRel([(25, 4), (8,82)])
TE_Draw.lineTo(225, 462)
te.end_fill()


# 图层_6
te.color("black", "#968281")  # 脖子
TE_Draw.moveTo(262, 329)
te.begin_fill()
TE_Draw.verticalRel(17)
TE_Draw.curveRel([(1, 2), (45, 15), (48, 27)])
TE_Draw.horizontalRel(3)
TE_Draw.verticalRel(-5)
TE_Draw.curveRel([(1, -3), (4, -6), (5, -7)])
TE_Draw.lineRel(36, -14)
TE_Draw.curveRel([(1, -1), (3, -16), (2, -17)])
TE_Draw.curveTo([(318, 348), (296, 344), (262, 329)])
te.end_fill()


# 图层_7
te.color("#E7F1FF")  # 白色褶皱
TE_Draw.moveTo(225, 462)
te.begin_fill()
TE_Draw.lineRel(-3, -5)
TE_Draw.curveRel([(4, -4), (5, -6), (21, -3), (24,-14)])
TE_Draw.curveRel([(0, -7), (0, -11),(5,-19),(9,-16)])
TE_Draw.curveRel([(19, -8), (19, -11), (25, -18), (33, -21)])
TE_Draw.lineRel(41, -2)
TE_Draw.lineRel(12, 9)
TE_Draw.curveRel([(3, 15), (7, 18),(23, 22),(18,18)])
TE_Draw.curveRel([(6, 4), (5, 9),(5,18)])
TE_Draw.curveRel([(1, 7), (7, 6),(15,6)])
TE_Draw.lineRel(-2, 8)
TE_Draw.lineTo(225, 462)
te.end_fill()

te.pensize(2)
TE_Draw.moveTo(240, 450)
TE_Draw.curveRel([(0, 9), (3, 12)])
TE_Draw.moveTo(372, 462)
TE_Draw.curveRel([(-2, -4), (-5, -29), (-7, -28)])
te.pensize(1)

# 图层_8
te.color("black", "#A2B8D6")  # 衣领
TE_Draw.moveTo(262, 331)
te.begin_fill()
TE_Draw.curveRel([(0, 8), (-1, 13), (0, 15),(45, 30)])
TE_Draw.lineRel(3, 12)
TE_Draw.horizontalRel(3)
TE_Draw.curveRel([(-1, -3),(0, -5)])
TE_Draw.lineRel(5, -7)
TE_Draw.lineRel(36, -14)
TE_Draw.curveRel([(1, -1), (2, -13),(27,-17),(17,2)])
TE_Draw.curveRel([(-2, 4), (-7, 30), (-42,49),(-48,52)])
TE_Draw.curveRel([(-10, 14), (-17,2),(-24,-1)])
TE_Draw.curveRel([(-19, -2), (-41, -25), (-51, -53)])
TE_Draw.curveTo([(255, 332), (262, 331)])
te.end_fill()

TE_Draw.moveTo(262, 346)
TE_Draw.lineRel(-12, -6)
TE_Draw.moveTo(369, 333)
TE_Draw.curveRel([(2, 4), (-6, 10), (-15, 14)])

# 图层_9
te.color("black", "#151515")  # 领结
TE_Draw.moveTo(247, 358)
te.begin_fill()
TE_Draw.curveRel([(-5, 3), (-8, 20), (-6, 23)])
TE_Draw.curveRel([(25, 21), (50, 17)])
TE_Draw.lineRel(-23, 64)
TE_Draw.horizontalRel(22)
TE_Draw.curveRel([(1, -13), (2, -16)])
TE_Draw.lineRel(13, -50)
TE_Draw.curveRel([(2, 2), (7, 3), (10, 1), (28,66)])
TE_Draw.horizontalRel(19)
TE_Draw.lineRel(-24, -65)
TE_Draw.curveRel([(21, 5), (39, -10), (44, -13)])
TE_Draw.curveRel([(5, -20), (1, -21), (0, -24)])
TE_Draw.curveRel([(-18, -2), (-49, 15), (-52, 17), (-67,16)])
TE_Draw.curveTo([(252, 356), (247, 358)])
te.end_fill()

# 图层_10
te.color("black", "#A2B8D6")  # 衣领（透过领结）
TE_Draw.moveTo(297, 387)
te.begin_fill()
TE_Draw.lineRel(-11, 6)
TE_Draw.curveRel([(-20, -7), (-30, -19)])
TE_Draw.curveTo([(259, 373), (297, 385), (297, 387)])
te.end_fill()
 
TE_Draw.moveTo(323, 384)
te.begin_fill()
TE_Draw.lineRel(8, 7)
TE_Draw.lineRel(30, -14)
TE_Draw.curveRel([(1, -1), (5, -6), (4, -7)])
TE_Draw.curveTo([(329, 379), (323, 384)])
te.end_fill()

# 图层_11
te.color("black", "#F3EEEB")  # 脸
TE_Draw.moveTo(185, 212)
te.begin_fill()
TE_Draw.curveRel([(4, -9), (46, -77), (52, -75)])
TE_Draw.curveRel([(-2, -17), (19, -68), (27, -73)])
TE_Draw.curveRel([(16, 15), (71, 108), (76, 112)])
TE_Draw.curveRel([(76, 53), (86, 60)])
TE_Draw.curveRel([(0, 65), (-27, 75), (-31, 76)])
TE_Draw.curveRel([(-50, 28), (-70, 30), (-85, 30)])
TE_Draw.curveRel([(-77, -22), (-86, -26)])
TE_Draw.curveTo([(180, 302), (186, 228), (185, 212)])
te.end_fill()

# 图层_12
te.color("black", "#2B1D29")  # 頭髮
TE_Draw.moveTo(189, 202)
te.begin_fill()
TE_Draw.curveRel([(-1, 22), (19, 51), (9, 9), (26,-41)])
TE_Draw.curveTo([(212, 168), (196, 189), (189, 202)])
te.end_fill()

 
TE_Draw.moveTo(221, 155)
te.begin_fill()
TE_Draw.curveRel([(-2, 6), (5, 48),(23,20),(25,0)])
TE_Draw.curveRel([(-5, 24), (4, 43), (7, 50)])
TE_Draw.curveRel([(-10, -49), (3, -72), (13, -106)])
TE_Draw.curveRel([(-2, -7), (-3, -32), (-3, -35)])
TE_Draw.curveRel([(-17, 18), (-27, 71)])
TE_Draw.lineTo(221, 155)
te.end_fill()
 
TE_Draw.moveTo(264, 64)
te.begin_fill()
TE_Draw.curveRel([(-4, 5), (14, 100)])
TE_Draw.curveRel([(-6, -79), (-5, -85)])
TE_Draw.curveRel([(0, 98), (49, 139)])
TE_Draw.curveRel([(8, -50), (3, -65)])
TE_Draw.curveTo([(272, 64), (264, 64)])
te.end_fill()

 
TE_Draw.moveTo(342, 176)
te.begin_fill()
TE_Draw.curveRel([(-1, 27), (-10, 57)])
TE_Draw.curveRel([(20, -33), (17, -54)])
TE_Draw.lineTo(342, 176)
te.end_fill()

 
te.penup()
te.begin_fill()
TE_Draw.polyline([(349, 180), (353, 203), (361, 203), (362, 188), (349, 180)])
te.end_fill()

# 图层_13
te.pensize(2)
TE_Draw.moveTo(210, 180)  # 眉毛
TE_Draw.curveRel([(5, -4), (63, 9), (63, 14)])
TE_Draw.moveTo(338, 193)
TE_Draw.curveRel([(0, -3), (18, -6)])
te.pensize(1)

# 图层_14
te.color("black", "#D1D1D1")  # 眼睛1
te.pensize(2)
TE_Draw.moveTo(206, 212)
te.begin_fill()
TE_Draw.lineRel(15, -7)
TE_Draw.curveRel([(4, -1), (26, -2), (30, 0)])
TE_Draw.curveRel([(10, 3), (12, 7)])
te.pencolor("#D1D1D1")
te.pensize(1)
TE_Draw.curveRel([(2, 27), (-1, 30)])
TE_Draw.curveRel([(-39, 5), (-44, 1)])
TE_Draw.curveTo([(206, 212)])
te.end_fill()

 
TE_Draw.moveTo(384, 204)
te.begin_fill()
te.pencolor("black")
te.pensize(2)
TE_Draw.curveRel([(-3, -1), (-18, -1),(-28, 1)])
TE_Draw.curveRel([(-9, 6), (-10, 9)])
te.pencolor("#D1D1D1")
te.pensize(1)
TE_Draw.curveRel([(3, 18), (6, 23)])
TE_Draw.curveRel([(38, 6), (40, 4)])
TE_Draw.curveRel([(10, -9), (13, -22)])
te.pencolor("black")
te.pensize(2)
TE_Draw.lineTo(384, 204)
te.end_fill()

# 图层_15
te.color("#0C1631", "#0C1631")  # 眼睛2
te.pensize(1)
TE_Draw.moveTo(216, 206)
te.begin_fill()
TE_Draw.curveRel([(-1, 5), (0, 26), (7, 35)])
TE_Draw.curveRel([(30, 2), (33, 0)])
TE_Draw.curveRel([(5, -31), (2, -34)])
TE_Draw.curveTo([(219, 203), (216, 206)])
te.end_fill()

 
TE_Draw.moveTo(354, 207)
te.begin_fill()
TE_Draw.curveRel([(-2, 1), (2, 29), (4, 31)])
TE_Draw.curveRel([(30, 3), (33, 1)])
TE_Draw.curveRel([(6, -24), (4, -27)])
TE_Draw.lineRel(-11, -8)
TE_Draw.curveTo([(382, 204), (357, 206), (354, 207)])
te.end_fill()

 
# 图层_17
te.color("#F5F5F5")  # 眼睛3
TE_Draw.moveTo(253, 211)
te.begin_fill()
TE_Draw.curveRel([(-3, 0), (-8, 8), (1, 10)])
TE_Draw.curveTo([(258, 210), (253, 211)])
te.end_fill()

 
TE_Draw.moveTo(392, 209)
te.begin_fill()
TE_Draw.lineRel(4, 3)
TE_Draw.verticalRel(4)
TE_Draw.lineRel(-4, 2)
TE_Draw.curveTo([(386, 214), (392, 209)])
te.end_fill()

# 图层_18
te.color("#352F53")  # 眼睛4
TE_Draw.moveTo(219, 229)
te.begin_fill()
TE_Draw.curveRel([(2, -5), (6, -4)])
TE_Draw.curveRel([(18, 13), (27, 1)])
TE_Draw.curveRel([(3, 0), (5, 3)])
TE_Draw.verticalRel(13)
TE_Draw.horizontalTo(224)
TE_Draw.lineTo(219, 229)
te.end_fill()

 
TE_Draw.moveTo(357, 227)
te.begin_fill()
TE_Draw.curveRel([(4, -6), (10, -2)])
TE_Draw.curveRel([(10, 13), (19, 1)])
TE_Draw.curveRel([(6, 0), (8, 6)])
TE_Draw.lineRel(-2, 9)
TE_Draw.curveRel([(-12, 3), (-29, 0), (-32, -2)])
TE_Draw.lineTo(357, 227)
te.end_fill()

# 图层_19
te.color("#9A90CB")  # 眼睛5
TE_Draw.moveTo(227, 231)
te.begin_fill()
TE_Draw.curveRel([(-6, 0), (-5, 5), (-3, 8)])
TE_Draw.curveRel([(24, 2), (27, 0)])
TE_Draw.curveRel([(0, -8), (-1, -8)])
TE_Draw.curveTo([(234, 231), (227, 231)])
te.end_fill()

 
TE_Draw.moveTo(361, 227)
te.begin_fill()
TE_Draw.curveRel([(2, 18), (26, 14), (30, 6)])
TE_Draw.curveRel([(-1, -3), (-2, -4)])
TE_Draw.curveRel([(-15, 9), (-24, -4)])
TE_Draw.curveTo([(363, 224), (361, 225), (361, 227)])
te.end_fill()

 
# 图层_16
te.pencolor("black")  # 眼睛(线条)
te.pensize(3)
TE_Draw.moveTo(225, 215)
TE_Draw.curveRel([(10, 28), (22, 16), (24, 6)])
TE_Draw.moveTo(365, 219)
TE_Draw.curveRel([(4, 14), (18, 24), (22, -3)])
te.pensize(2)
TE_Draw.line(240.5, 207.5, 227.5, 211.5)
TE_Draw.line(245.5, 209.5, 227.5, 214.5)
TE_Draw.line(247.5, 211.5, 227.5, 217.5)
TE_Draw.line(247.5, 214.5, 229.5, 220.5)
TE_Draw.line(247.5, 218.5, 230.5, 223.5)
TE_Draw.line(246.5, 222.5, 232.5, 226.5)
TE_Draw.line(244.5, 225.5, 234.5, 228.5)
 
TE_Draw.line(377.5, 207.5, 367.5, 210.5)
TE_Draw.line(384.5, 207.5, 366.5, 212.5)
TE_Draw.line(385.5, 210.5, 366.5, 215.5)
TE_Draw.line(384.5, 213.5, 366.5, 218.5)
TE_Draw.line(384.5, 215.5, 367.5, 220.5)
TE_Draw.line(384.5, 218.5, 368.5, 223.5)
TE_Draw.line(382.5, 223.5, 370.5, 227.5)

# 图层_20
te.pencolor("black")
TE_Draw.moveTo(309, 270)  # 鼻子、嘴
TE_Draw.curveRel([(4, 7), (1, 9)])
TE_Draw.line(296.5, 307.5, 303.5, 307.5)
TE_Draw.moveTo(315, 307)
TE_Draw.curveRel([(10, -1), (10, 2)])
 
te.penup()
te.hideturtle()
te.update()
te.done()