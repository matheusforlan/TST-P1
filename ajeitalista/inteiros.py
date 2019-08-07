#coding:utf-8


def ajeita_lista(lista):
	
	for pos in range(len(lista)-1):
		
		for j in range(len(lista)-1):
			if lista[j]%2 != 0 and lista[j+1]%2==0:
				lista[j], lista[j+1] = lista[j+1], lista[j]
		
	for parimpar in range(len(lista)-1):
		for m in range(len(lista)-1):
			if lista[m]%2 == 0 and lista[m+1]%2 ==0:
				if lista[m] < lista[m+1]:
					lista[m], lista[m+1] = lista[m+1], lista[m]
		
			elif lista[m]%2 !=0 and lista[m+1]%2 != 0:
				if lista[m] > lista[m+1]:
					lista[m], lista[m+1] = lista[m+1], lista[m]
					
			
	return None

lista1 = [3, 2, 1, 4, 5, 6, 7, 8, 9]
assert ajeita_lista(lista1) == None
assert lista1 == [8, 6, 4, 2, 1, 3, 5, 7, 9]
