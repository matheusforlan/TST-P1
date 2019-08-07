#coding:utf-8
def adicionador(lista):
	pos = len(lista)-1
	
	for c in range((len(lista)-1),0,-1):
		if lista[c] < lista[c-1]:
			lista[c],lista[c-1] = lista[c-1], lista[c]
			pos -= 1
	
	if pos == len(lista)-1:
		return lista, "Adicionado ao final da lista"
	else:
		return lista, pos


lista = []
valor = int(raw_input("Digite um valor: "))
lista.append(valor)
print "Adicionado ao final da lista"
for c in range(4):
	valor = int(raw_input("Digite um valor: "))
	lista.append(valor)
	lista,posicao = adicionador(lista)
	print "Adicionado na posição {} da lista".format(posicao)

print "Lista ordenada é: {}".format(lista)
	
