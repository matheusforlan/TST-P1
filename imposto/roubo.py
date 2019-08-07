#coding:utf-8
bruto = float(raw_input())
horas = float(raw_input())
print "Salário Bruto = {:.1f}".format(bruto)
print "Hora Bruta = {}".format(bruto/horas)
ir = bruto*0.11
inss = bruto*0.08
sindicato = bruto*0.05
print "Desconto IR = {:.1f}".format(ir)
print "Desconto INSS = {:.1f}".format(inss)
print "Desconto Sindicato = {:.1f}".format(sindicato)
liquido = bruto - ir - inss - sindicato
print "Salário Líquido = {:.1f}".format(liquido)
print "Hora Líquida = {}".format(liquido/horas)
