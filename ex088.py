#coding:utf-8

from random import randint
print "-----------   JOGO DA MEGA SENA ------------ "
quantidade = int(raw_input("Quantos jogos serão feitos? "))
controlador = 1
jogos = []
lista = []

while controlador <= quantidade:
	cont = 1
	lista = []
	while True:
		numero = randint(1,61)
		if numero not in lista:
			lista.append(numero)
			cont += 1
		if cont > 6:
			break
			
	lista.sort()
	jogos.append(lista[:])
	controlador += 1

for c in range(len(jogos)):
	print "jogo {}: {}".format(c+1, jogos[c])

