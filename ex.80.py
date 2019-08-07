#coding:utf-8
def adicionador(lista):
	for c in range(len(lista)-1,0,-1)):
		if lista[c] < lista[c-1]:
			lista[c],lista[c-1] = lista[c-1], lista[c]
	
	return lista


lista = []
valor = int(raw_input("Digite um valor: "))
lista.append(valor)
print "Adicionado ao final da lista"
for c in range(4):
	valor = int(raw_input("Digite um valor: "))
	lista.append(valor)
	parcial = adicionador(lista)
	print parcial
	
	
	
