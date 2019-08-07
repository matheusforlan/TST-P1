#coding:utf-8

def busca_todos_por_coluna_em_matriz(m,e):
	linhacoluna = []
	
	for j in range(len(m[0])):
		for i in range(len(m)):
			if m[i][j] == e:
				linhacoluna.append((i,j))
	
	return linhacoluna


matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [3, 2, 3, 2, 1],
]
assert busca_todos_por_coluna_em_matriz(matriz, 4) == []
assert busca_todos_por_coluna_em_matriz(matriz, 3) == [(1,0), (2,0), (0,1), (2,2), (0,3)]
assert busca_todos_por_coluna_em_matriz(matriz, 1) == [(1,2), (0,4), (2,4)]
