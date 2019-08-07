#coding:utf-8

def lista_ordenada(lista, nome):
	lista.append(nome) 
	if len(lista) != 1: #tem que ser diferente de 1 para ordenar...
		for c in range(len(lista)-1, 0, -1): #adiciona no final e vai comparando de trás
			if lista[c] < lista[c-1]:                                  # para frente
				lista[c], lista[c-1] = lista[c-1], lista[c]
				

lista_nomes =[]
while True:
	nome= raw_input()
	if nome == "####": break
	lista_ordenada(lista_nomes,nome)  #Adiciona o nome e ordena
	for m in lista_nomes:   #printa dps que tá ordenado
		if m == nome: #Se for o nome que você acabou de colocar, coloca o * no print
			print "* %s"%m
		else:
			print m
	print "----"
	
	
	
