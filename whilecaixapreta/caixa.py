#coding:utf-8
dados_pos = True
lista = []
peso = 0
combustivel = 0
altitude = 0
parada = ""
while True:
	dados = raw_input().split()
	lista.append(dados)
	if int(dados[0]) < 0: 
		parada = "peso negativo"
		break 
	if int(dados[0]) >= 0:
		peso +=1
	if int(dados[1]) <0: 
		parada = "combustível negativo"
		break
	if int(dados[1])>= 0:
		combustivel += 1
	if int(dados[2])<0: 
		parada = "altitude negativa"
		break
	if int(dados[2])>= 0:
		altitude += 1
print "dado inconsistente. %s."%parada
print "peso: %d"%peso
print "combustível: %d"%combustivel
print "altitude: %d"%altitude

			
