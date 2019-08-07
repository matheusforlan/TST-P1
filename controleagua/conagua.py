#coding: utf-8
import math
velvaz = float(raw_input())
diam = float(raw_input())
tempo = int(raw_input())
seccao = float(math.pi*diam**2)/4
vazao = velvaz*seccao*1000

quantidade_de_agua = tempo*vazao
print "Quantidade de água = %s litros."%quantidade_de_agua
