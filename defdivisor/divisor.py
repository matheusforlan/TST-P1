#coding:utf-8

def divisor(num,lista):
	indice = -1
	
	for c in range(len(lista)):
		if lista[c]%num == 0:
			indice = c
			break
	
	return indice
	


lista1 = [100,10,40,50]
lista2 = [3,15,50,23,5]
assert divisor(10, lista1) == 0
assert divisor(5, lista2) == 1
