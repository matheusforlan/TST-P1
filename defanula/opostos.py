#coding:utf-8
def anula(lista):
	for c in range(len(lista)-1,0,-1):
		if  len(lista) == 1:
			return lista
		
		if lista[c] + lista[c-1] == 0:
			lista.pop(c)
			lista.pop(c-1)


lista1 = [1, 2, -2, 3, 4]
assert anula(lista1) == None
assert lista1 == [1, 3, 4]

lista2 = [1, 2, -2, -1, 4]
assert anula(lista2) == None
assert lista2 == [4]

lista3 = [4]
assert anula(lista3) == None
assert lista3 == [4]

lista4 = [-4,4]
assert anula(lista4) == None
assert lista4 == []

lista5 = [-6,4,-1,0,1,-4,6]
assert anula(lista5) == None
assert lista5 == [-6,4,-1,0,1,-4,6]

