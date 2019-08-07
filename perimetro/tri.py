#coding:utf-8
import math
x1 = int(raw_input())
y1 = int(raw_input())
x2 = int(raw_input())
y2 = int(raw_input())
x3 = int(raw_input())
y3 = int(raw_input())
dis12 = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
dis13 = math.sqrt(((x1-x3)**2)+((y1-y3)**2))
dis23 = math.sqrt(((x2-x3)**2)+((y2-y3)**2))
perimetro = dis12+dis13+dis23
print "O perímetro é de {:.2f}".format(perimetro)
