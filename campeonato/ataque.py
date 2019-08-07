#coding:utf-8
n = int(raw_input())
soma = 0
lista_nomes = []
lista_gols = []
pos = 1
maiorgols = 0
maiornomes = []
for c in range(n):
	nome = raw_input()
	gols = int(raw_input())
	soma += gols
	lista_nomes.append(nome)
	lista_gols.append(gols)

for i in range(n):
	if lista_gols[i] >= maiorgols:
		maiorgols = lista_gols[i]

for m in range(n):
	if lista_gols[m] == maiorgols:
		maiornomes.append(lista_nomes[m])
print "Time(s) com melhor ataque ({} gol(s)):".format(maiorgols)
for i in maiornomes:
	print i
print""
print "Média de gols marcados: {:.1f}".format(soma*1.0/n)
	
		
