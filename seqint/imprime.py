#coding:utf-8
num = 1
maiores = 0
alvo = int(raw_input())
lista_pos = []
lista_maiores= []
while True:
	sequencia = raw_input()
	if sequencia == "fim":break
	splitado = sequencia.split()
	maiores = 0
	for c in splitado:
		if int(c)>alvo:
			maiores += 1
	if maiores > (len(splitado)/2.0):     #guarda à posição e a sequencia que satisfaz
		lista_pos.append(num)
		lista_maiores.append(sequencia)
	num += 1
indice = 0
for m in range(len(lista_pos)):
	print "sequencia {}: {}".format(lista_pos[indice],lista_maiores[indice])
	indice += 1

		
	
