#coding:utf-8

def conta_palavras(tamanho,sequencia):
	seq_split = sequencia.split(":")
	comprimento = 0
	contador = 0
	for c in range(len(seq_split)):
		if len(seq_split[c]) >= tamanho:
			contador += 1
	
	return contador



assert conta_palavras(5, "zero:um:dois:tres:quatro:cinco") == 2
