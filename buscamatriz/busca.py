#coding:utf-8

def busca_matriz(m,e):
	
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j] == e:
				print (i,j)
				return (i,j)
	
	return None


matriz = [[2, 3, 5, 3, 1],[3, 2, 1, 5, 6], [1, 2, 3, 2, 1],]
assert busca_matriz(matriz, 4) == None
assert busca_matriz(matriz, 3) == (0,1)
assert busca_matriz(matriz, 1) == (0,4)
