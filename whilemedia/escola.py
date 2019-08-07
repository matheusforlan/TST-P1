#coding:utf-8
soma= 0
contador = 0
lista = []
while True:
	num = raw_input()
	soma += float(num)
	contador += 1
	lista.append(num)
	if soma > 100: break

media = soma/contador
print "Quantidade de números lidos: {}".format(contador)
print "Soma dos números lidos: {:.2f}".format(soma)
print "Média = {:.2f}".format(media)
print ""
print "Abaixo da média"
pos = 1
for c in lista:
	if float(c) < media:
		print "{:.2f} ({}o)".format(float(c),pos)
	pos += 1
print""
print "Acima da média"
pos = 1
for m in lista:
	if float(m) > media:
		print "{:.2f} ({}o)".format(float(m),pos)
	pos += 1

		
