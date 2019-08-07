#coding:utf-8


def calcula_seguro(valor, lista_infos):
	pontuacao  = 0
	for infos in range(len(lista_infos)):
		if infos == 0:
			if int(lista_infos[0]) <= 21:
				pontuacao += 20
			elif int(lista_infos[0]) >= 22 and  int(lista_infos[0]) <= 30:
				pontuacao += 15
			elif int(lista_infos[0]) >= 31 and int(lista_infos[0]) <= 40:
				pontuacao += 12
			elif int(lista_infos[0]) >= 41 and int(lista_infos[0]) <= 60:
				pontuacao += 10
			else:  #acima de 60
				pontuacao += 20
		if infos == 1:
			if int(lista_infos[1]) == True: #casado
				pontuacao += 10
			else: #solteiro
				pontuacao += 20
		if infos == 2:
			if int(lista_infos[2]) == True: #area de risco
				pontuacao += 20
			else:
				pontuacao += 10
		if infos == 3:
			if int(lista_infos[3]) == True: #portao eletronico
				pontuacao += 20
			else:
				pontuacao += 10 
		if infos == 4:
			if int(lista_infos[4]) == True: #mora em casa
				pontuacao += 20
			else: #apartamento
				pontuacao += 10
		if infos == 5:
			if int(lista_infos[5]) == True: #casa própria
				pontuacao += 10
			else:      #alugada
				pontuacao += 20
		if infos == 6:
				if (lista_infos[6]) == "Lazer":
					pontuacao += 20
				elif (lista_infos[6]) == "Trabalho":
					pontuacao += 10
				else:       #misto
					pontuacao += 20
	if pontuacao <= 80:
		risco = "Risco Baixo"
		valor_pago = valor*0.10
	elif pontuacao > 80 and pontuacao <= 100:
		risco = "Risco Medio"
		valor_pago = valor*0.20
	elif pontuacao >100:  # Maior que 100
		risco = "Risco Alto"
		valor_pago = valor*0.30
	
	#print [pontuacao, risco, valor_pago]
	return [pontuacao, risco, valor_pago]



			
				
assert calcula_seguro(2000.0, [60, True, False, True, False, True, 'Trabalho']) == [80, 'Risco Baixo', 200.0]
assert calcula_seguro(2000.0, [21, True, True, True, False, True, 'Trabalho']) == [100, 'Risco Medio', 400.0]

assert calcula_seguro(2000.0, [21, True, True, True, True, True, 'Misto']) == [120, 'Risco Alto', 600.0]
