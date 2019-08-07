#coding:utf-8

lista = []
contador = 0
while True:
	if contador == 0:
		numero = int(raw_input("Digite um número: "))
		lista.append(numero)
		contador += 1
	acao = raw_input("Deseja continuar?: ")
	if acao in "Nn": break
	numero = int(raw_input("Digite um número: "))
	lista.append(numero)
	contador += 1

print "-"*50
print "você digitou {} números".format(contador)
lista.sort(reverse = True)
print "Os valores em ordem decrescente são {}".format(lista)
if int("5") in lista:
	print "Valor 5 foi encontrado"
else:
	print "Valor 5 não foi encontrado"
	
