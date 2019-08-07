#coding:utf-8
s0 = float(raw_input("Posição inicial? "))
v0 = float(raw_input("Velocidade inicial? "))
t = float(raw_input("Tempo? "))
a = float(raw_input("Aceleração? "))
print""
print "Dados da questão"
print "================"
print "   Posição inicial: {:.2f} m".format(s0)
print "Velocidade inicial: {:.2f} m/s".format(v0)
print "        Aceleração: {:.2f} m/s2".format(a)
print "             Tempo: {:.2f} s".format(t)
print "  Velocidade final: {:.2f} m/s".format(v0+a*t)
print "  Velocidade média: {:.2f} m/s".format(v0+(a*t/2))
print "     Posição final: {:.2f} m".format(s0+v0*t+(a*t**2/2))
