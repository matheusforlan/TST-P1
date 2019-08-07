#coding:utf-8
def encontra_menores(num,lista):
	
	for c in lista:
		if c < num:
			return c
	return int("-1")
	
	

lista1 = [100,200,300,400]
lista2 = [15, 12, 4, 9, 10]
assert encontra_menores(100, lista1) == -1
assert encontra_menores(10, lista2) == 4
