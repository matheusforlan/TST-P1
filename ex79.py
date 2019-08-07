#coding:utf-8

lista = []
valor = int(raw_input("Digite um valor: "))
lista.append(valor)
print "Valor adicionado"

while True:
	
	acao = raw_input("Você quer continuar: [S/N] ")
	if acao == "n" or acao == "N": break
	valor = int(raw_input("Digite um valor: "))
	if valor not in lista:
		lista.append(valor)
		print "Valor adicionado"
	else:
		print "Valor duplicado não adicionado"

lista.sort()
print lista
	
	
