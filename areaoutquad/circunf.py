#coding: utf-8
import math
r = float(raw_input())
area_quad = ((2*r)**2)/2
area_circ = math.pi*r**2
nao_comum = area_circ-area_quad
print "Área não comum: {:.5f}".format(nao_comum)
