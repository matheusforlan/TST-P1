#coding:utf-8
n = int(raw_input())
soma_rep = 0
soma_apr = 0
reprovados = 0
aprovados = 0
quant_rep = 0
quant_apr = 0
for c in range (n):
	nota = float(raw_input())
	if nota < 7:
		soma_rep += nota
		reprovados += 1
		quant_rep += 1
	else:
		soma_apr += nota
		aprovados += 1
		quant_apr += 1
if reprovados == 0:
	print "Reprovados: {}".format(reprovados)
	print ""
	print "Aprovados: {}".format(aprovados)
	print "Média: {:.1f}".format(soma_apr/quant_apr)
elif aprovados == 0:
	print "Reprovados: {}".format(reprovados)
	print "Média: {:.1f}".format(soma_rep/quant_rep)
	print ""
	print "Aprovados: {}".format(aprovados)
else:
	print "Reprovados: {}".format(reprovados)
	print "Média: {:.1f}".format(soma_rep/quant_rep)
	print ""
	print "Aprovados: {}".format(aprovados)
	print "Média: {:.1f}".format(soma_apr/quant_apr)
