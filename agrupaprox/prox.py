#coding:utf-8

def agrupa_proximos(lista, valor, criterio):
	lista_proximos = []
	for c in range(len(lista)):
		if (valor-lista[c]) < 0: #negativo
			if (valor-lista[c])*-1.0 < criterio:
				lista_proximos.append(lista[c])
		else:  # valor-lista[c]) > 0: #postivo
			if valor-lista[c] < criterio:
				lista_proximos.append(lista[c])
	print lista_proximos 
	return lista_proximos



l = [1,2,3,4,8,22,3,5]
assert agrupa_proximos(l,4,2) == [3,4,3,5]
assert l == [1,2,3,4,8,22,3,5]
