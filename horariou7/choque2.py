#coding:utf-8
def get_choque_horario(disciplinas):
	lista_choques = list()
	for disciplina in range(len(disciplinas)):
		primeiro_choque = True
		indices_a_remover = list()
		for disciplina_comparada in range(len(disciplinas)):
			if disciplinas[disciplina] == disciplinas[disciplina_comparada]:
				# se for a mesma disciplina, ignore
				continue
			if disciplinas[disciplina].split('-')[1] == disciplinas[disciplina_comparada].split('-')[1]:
				# houve choque
				if (primeiro_choque):
					# na primeira vez, adicione a atual também
					primeiro_choque = False
					lista_choques.append(disciplinas[disciplina])
					indices_a_remover.append(disciplina)
				# adicione a comparada
				lista_choques.append(disciplinas[disciplina_comparada])
			for indice_a_remover in range(len(indices_a_remover) - 1, -1, -1):
				# removendo do fim pro início para não dar problema com os índices
				disciplinas.pop(indices_a_remover[indice_a_remover])
	
	return lista_choques
				
				
l1 = ["oac-4", "so-5", "atal-5", "prog1-1", "es-4"]
assert get_choque_horario(l1) == ["oac-4", "es-4", "so-5", "atal-5"]

l1 = ["oac-4", "loac-4", "so-5", "atal-5", "prog1-1", "es-4"]
assert get_choque_horario(l1) == ["oac-4", "loac-4", "es-4", "so-5", "atal-5"]
