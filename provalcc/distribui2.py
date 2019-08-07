#coding:utf-8
def tamanho(lista1, lista2):
	if len(lista1)> len(lista2):
 		return lista1, lista2
 	elif len(lista2) > len(lista1):
		return lista2, lista1


def distribui_alunos(turma1, turma2, capacidade):
	lcc = []
	labs = [ [],[]]
	if len(turma1) != len(turma2):
		maior, menor = tamanho(turma1,turma2)
		for c in range(len(maior)):
			if c <= len(menor)-1:
				lcc.append(turma1[c])
				lcc.append(turma2[c])
			else: #c > len(menor)-1:
				lcc.append(maior[c])
			
		
	else:  #len(turma1) == len(turma2):
		for j in range(len(turma1)):
			lcc.append(turma1[j])
			lcc.append(turma2[j])
	for p in range(len(lcc)):
		if p <= capacidade-1:
			labs[0].append(lcc[p])
		else: #p >= capacidade-1
			labs[1].append(lcc[p])

	print lcc
	print labs
	return labs

t1 = [43, 21, 96, 33, 85, 17, 94]
t2 = [ 10, 38, 87, 22, 25]
assert distribui_alunos(t1, t2, 6) == [[ 43,10, 21,38,96, 87], [33, 22, 85,25, 17, 94]]

t1 = [10, 38, 87, 22, 25]
t2 = [43, 21, 96, 33, 85, 17, 94]
assert distribui_alunos(t1, t2, 6) == [[10, 43, 38, 21, 87, 96], [22, 33, 25, 85, 17, 94]]

t1 = [10,38,87,22,25]
t2 = [43,21,96,33,85]
assert distribui_alunos(t1,t2,6) == [[10,43,38,21,87,96],[22,33,25,85]]

t1 = [10,38,87,22,25]
t2 = [43,21,96,33,85]
assert distribui_alunos(t1,t2,5) == [[10,43,38,21,87],[96,22,33,25,85]]

t1 = [10, 38, 87, 22 ]
t2 = [43, 21, 96, 33, 85, 69]
assert distribui_alunos(t1, t2, 5) == [[10, 43, 38, 21, 87], [96,22, 33,85,69]]

t1 = [5,8]
t2 = [15,17,18,19]
assert distribui_alunos(t1, t2, 5) == [[5,15,8,17,18], [19]]

t1 = [5,8]
t2 = [15,17,18,19]
assert distribui_alunos(t1, t2, 8) == [[5,15,8,17,18,19], []]
