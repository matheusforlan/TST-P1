#coding:utf-8
palavra  = raw_input()
lista = []
vogais = ["a","e","i","o","u","A","E","I","O","U"]
for c in palavra:
	lista.append(c)
for m in lista:
	if m in vogais:
		print "<{}> sim".format(m)
	else:
		print "<{}> nao".format(m)
