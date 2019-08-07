#coding:utf-8
import math
print "Cálculo da Superfície de um Cilindro"
print "---"
d = float(raw_input("Medida do diâmetro? "))
h = float(raw_input("Medida da altura? "))
print "---"
base = 2*math.pi*((d/2)**2)
lateral = 2*math.pi*(d/2)*h
print "Área calculada: {:.2f}".format(base+lateral)
