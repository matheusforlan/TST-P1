#coding:utf-8

def coluna(matriz, i):
	colunas= []
	for linha in range(len(matriz)):
		colunas.append(matriz[linha][i])
	
	return colunas
				
	
	
	

M = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
assert coluna(M,0) == [1,2,3]
assert coluna(M,1) == [1,2,3]
assert coluna(M,2) == [1,2,3]
assert coluna(M,3) == [1,2,3]
