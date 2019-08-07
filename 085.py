#coding:utf-8


parimpar = [ [], []]

for c in range(7):
	numero = int(raw_input("Digite o {}º número: ".format(c)))
	if (numero % 2) == 0:
		parimpar[0].append(numero)
	else:
		parimpar[1].append(numero)

for j in parimpar:
	j.sort()
	
print "Valores pares: {}".format(parimpar[0])
print "Valores ímpares: {}".format(parimpar[1])
