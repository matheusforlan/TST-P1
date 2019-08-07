#coding:utf-8
def anula(lista):
	houve_for = True
	while houve_for:
		houve_for = False
		for c in range(len(lista)-1,0,-1):
			if  len(lista) == 1:
				break
		
			if lista[c] + lista[c-1] == 0:
				lista.pop(c)
				lista.pop(c-1)
				houve_for = True
				break


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

lista6  = [4,-8,7,-7,8]
assert anula(lista6) == None
assert lista6 == [4]


