def organiza_por_media(lista):
	lista_maiores= []
	lista_final = []
	soma = 0
	for num in lista:
		soma += num
	if len(lista) > 0:
		media = float(soma)/len(lista)
	else:
		media = 0
	for c in range(len(lista)-1,-1,-1):
		if lista[c] >= media:
			lista_maiores.append(lista[c])
			lista.pop(c)
	
	
	for m in range(len(lista_maiores)-1,-1,-1):
		lista.append(lista_maiores[m])

			
	return lista
	
p1 = [1, 2, 4, 1, 3, 4, 56, 7, 7, 4, 3, 67]
assert organiza_por_media(p1) == [1, 2, 4, 1, 3, 4, 7, 7, 4, 3, 56, 67]
assert p1 == [1, 2, 4, 1, 3, 4, 7, 7, 4, 3, 56, 67]
	
	
	
		
	
