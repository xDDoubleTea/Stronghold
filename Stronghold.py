import math


PI = math.pi

print('請依照格式輸入:')
print('x[1] ,z[1] ,Angle1')
x1 , z1, Angle1 = input().split(' ,')
print('x[2] ,z[2] ,Angle2')
x2 , z2, Angle2 = input().split(' ,')

x1 ,x2 = -eval(x1) ,-eval(x2)
#x座標互換
Angle1 , Angle2 = -eval(Angle1) + 90 , -eval(Angle2) + 90
#角度轉換
tanAngle1 , tanAngle2 = math.tan(Angle1/180*PI) , math.tan(Angle2/180*PI)
#轉換斜率

a1 ,a2 = tanAngle1 , tanAngle2
b1 = b2 = -1
c1 , c2 = (a1*x1) - eval(z1) , (a2*x2) - eval(z2)
xFin = -((c2*b1)-(c1*b2))/((a2*b1)-(a1*b2))
zFin = ((a1*c2)-(a2*c1))/((b2*a1)-(a2*b1))
print(xFin, zFin)

