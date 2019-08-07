#coding:utf-8
soma = 0
lista = []

while True:
	num = raw_input()
	if num == "fim": break
	soma += int(num)
	lista.append(num)
	
media = float(soma)/len(lista)
print "%.2f"%(media)
pos =0
indice = 1
for c in lista:
	if float(c) < media:
		print "%s %s"%(indice, lista[pos])
	pos+= 1
	indice += 1
