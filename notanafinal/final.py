#coding:utf-8
print "== Estágio 1 =="
peso1 = float(raw_input("Peso? "))
nota1 = float(raw_input("Nota? "))
print "== Estágio 2 =="
peso2 = float(raw_input("Peso? "))
nota2 = float(raw_input("Nota? "))
print "== Estágio 3 =="
peso3 = float(raw_input("Peso? "))
nota3 = float(raw_input("Nota? "))
print "== Resultados =="
parcial = peso1*nota1+peso2*nota2+peso3*nota3/(peso1+peso2+peso3)
print "Média parcial: {}".format(parcial)
print "Nota na final, pra média 5.0 = {:.1f}".format((parcial*0.6-5)/0.4*-1)
print "Nota na final, pra média 7.0 = {:.1f}".format((parcial*0.6-7)/0.4*-1)
