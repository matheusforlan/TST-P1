#coding:utf-8
def tamanho(lista1, lista2):
	if len(lista1)> len(lista2):
 		return lista1, lista2
 	elif len(lista2) > len(lista1):
		return lista2, lista1
			
def distribui_alunos(turma1, turma2, capacidade):
	lab = [[],[]] 
	if len(turma1) != len(turma2):
		maior, menor = tamanho(t1,t2)
		quantidade = 0
		for c in range(len(maior)):
			if c<= len(menor)-1:
				if quantidade == capacidade:
					if c<= len(menor)-1:
						lab[1].append(turma1[c])
				
				elif quantidade < capacidade:
					lab[0].append(turma1[c])
					quantidade += 1
			
				if quantidade == capacidade:
					lab[1].append(turma2[c])
				elif quantidade < capacidade:
					lab[0].append(turma2[c])
					quantidade += 1
			else:
				if quantidade < capacidade:
					lab[0].append(maior[c])
					quantidade += 1
				elif quantidade == capacidade:
					lab[1].append(maior[c])
	
	elif len(turma1) == len(turma2):
		quantidade = 0
		for m in range(len(turma1)):
			if quantidade == capacidade:
				lab[1].append(turma1[m])
			elif quantidade < capacidade:
				lab[0].append(turma1[m])
				quantidade += 1
			if quantidade == capacidade:
				lab[1].append(turma2[m])
			elif quantidade < capacidade:
				lab[0].append(turma2[m])
				quantidade += 1
	print lab
	return lab
				
		
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

