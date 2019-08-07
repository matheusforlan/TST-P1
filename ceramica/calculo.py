#coding:utf-8
capacidade = float(raw_input("Capacidade de revestimento?"))
print " "
print "== Dados do vão a revestir =="
c = float(raw_input("Comprimento? "))
l = float(raw_input("Largura? "))
a = float(raw_input("Altura?"))
print " "
print "== Resultados =="
area = c*l+2*a*c+2*a*l
print "Área total a revestir: {:.1f} m2".format(area)
caixas = int(area/capacidade)
print "Número de caixas: {}".format(caixas)
