#coding:utf-8
def insere_ordenado(nome,numero):
	lista_nomes.append(nome)
	lista_numeros.append(numero)
	if len(lista_nomes) != 1:
		for c in range(len(lista_nomes)-1,0,-1):
			if lista_nomes[c] < lista_nomes[c-1]:
				lista_nomes[c-1], lista_nomes[c] = lista_nomes[c], lista_nomes[c-1]
				lista_numeros[c-1], lista_numeros[c] = lista_numeros[c], lista_numeros[c-1]
def forlan_in(elemento,lista):
	for e in lista:
		if e == elemento:
			return True
	return False 

def buscador(nome):
	for i in range(len(lista_nomes)):
		if lista_nomes[i] == nome:
			print "Nome: %s"%lista_nomes[i]
			print "Fone: %s"%lista_numeros[i]
			print "----------"
		
lista_nomes = []
lista_numeros = []

while True:
	instrucao = raw_input()
	if instrucao == "finalizar": break
	elif instrucao == "inserir":
		quantidade =  int(raw_input())
		control = 1
		while control <= quantidade:  #ordenar pela quantidade de números que você digitar
			nome = raw_input()
			numero = raw_input()
			insere_ordenado(nome,numero)
			control +=1
	elif instrucao == "buscar":
		nome = raw_input()
		if forlan_in(nome, lista_nomes):
			buscador(nome)

		else:
			print "Nome inexistente"
			print "----------"
	elif instrucao == "imprimir":
		for j in range(len(lista_nomes)):
			print "Nome: %s"%lista_nomes[j]
			print "Fone: %s"%lista_numeros[j]
			print "----------"
	
			
		
