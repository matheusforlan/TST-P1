#coding:utf-8
kg = int(raw_input())
horas = int(raw_input())
calcons = int(raw_input())
calgas = horas*900+2000-calcons*1.0
dias = (kg*7700)/calgas*1.0
print "Você precisará de {:.2f} dias de dieta".format(dias)
