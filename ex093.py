#coding:utf-8

dados = {}
dados["nome"] = raw_input("Nome do jogador: ")
partidas = int(raw_input("Quantas partidas ele jogou?: "))
total = 0
gols = []
for c in range(partidas):
	partida = int(raw_input("Quantos gols na partida %s: "%c))
	gols.append(partida)
	total += partida

dados["gols"] = gols
dados["total"] = total

print dados
print "="*50
for k,v in dados.items():
	print "A chave  %s tem o valor %s"%(k,v)
print "="*50
print "O jogador %s jogou %s partidas"%(dados["nome"],partidas)
for c in range(partidas):
	print "Na partida %s fez %s gols"%(c, dados["gols"][c])
print "foi um total de %s gols."%total

