#coding:utf-8
n = int(raw_input())
confiavel = 0
positivo = True 
for c in range(n):
	dados = raw_input().split()
	if positivo == True:
		if int(dados[0]) < 0 or int(dados[1]) <0 or int(dados[2])<0:
			if int(dados[0]) < 0:
				print "dado inconsistente. peso negativo."
			elif int(dados[1]) < 0:
				print "dado inconsistente. combustível negativo."
				confiavel += 1
			elif int(dados[2])<0:
				print "dado inconsistente. altitude negativa."
				confiavel += 2
			positivo = False 
		else:
			confiavel += 3
print "{} dados válidos.".format(confiavel)
