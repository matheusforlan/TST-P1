#coding:utf-8

lista = []
while True:
	nome = raw_input("Nome: ")
	nota1 = float(raw_input("Nota 1: "))
	nota2 = float(raw_input("Nota 2: "))
	media = (nota1 + nota2)/2
	dados = []
	lista.append([nome,[nota1,nota2],media])

	print lista
	
	continuar = raw_input("Quer continuar? [S/N]")
	if continuar in "nN": break

print "="*50
print "Nº / Nome     / Média"
for c in range (len(lista)):
	print "{}   {}     {}".format(c, lista[c][0], lista[c][2])
print "+="*50

while True:
	aluno = int(raw_input("Mostar notas de qual aluno? (999) interrompe:  "))
	if aluno == 999: break
	print "As notas de {} são {}".format(lista[aluno][0],lista[aluno][1])
