#coding: utf-8
import math
l = float(raw_input())
r = math.sqrt((l/2)**2 + (l/2)**2)
perimetro = 2*math.pi*r
area = math.pi*r**2
print "Perímetro: {:.5f}".format(perimetro)
print "Área: {:.5f}".format(area)

