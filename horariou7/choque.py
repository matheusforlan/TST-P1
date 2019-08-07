#coding:utf-8
def meu_in(elemento,sequencia):
	for e in sequencia:
		if e == elemento:
			return True
	
	return False
def choques(elemento,sequencia):
	contador = 0
	for e in sequencia:
		if e == elemento:
			contador += 1
	if contador >1:
		return True
	
	return False
def get_choque_horario(disciplinas):
	lista_choques = []
	hora_splitada = []
	
	for m in range(len(disciplinas)):      #Pra separar os horários
		splitada = disciplinas[m].split("-")
		hora_splitada.append(splitada[1])
	
	for da_vez in range(len(disciplinas)):
		da_vez_splitada = disciplinas[da_vez].split("-")
		for comparada in range(len(disciplinas)):
			comp_splitada = disciplinas[comparada].split("-")
			if choques(da_vez_splitada[-1],hora_splitada): #Testa se houve choque 
				if da_vez_splitada[-1] == comp_splitada[-1] and meu_in(disciplinas[comparada],lista_choques)== False:
					lista_choques.append(disciplinas[comparada]) #Adiciona 
	#print lista_choques
	return lista_choques
		


l1 = ["oac-4", "so-5", "atal-5", "prog1-1", "es-4"]
assert get_choque_horario(l1) == ["oac-4", "es-4", "so-5", "atal-5"]

l1 = ["oac-4", "loac-4", "so-5", "atal-5", "prog1-1", "es-4"]
assert get_choque_horario(l1) == ["oac-4", "loac-4", "es-4", "so-5", "atal-5"]
