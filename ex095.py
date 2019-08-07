lista = []
dados = {}
while True:
	dados = {}
	dados["nome"] = input("Nome do jogador: ")
	partidas = int(input("Quantas partidas ele jogou?: "))
	total = 0
	gols = []
	for c in range(partidas):
		partida = int(input("Quantos gols na partida %s: "%c))
		gols.append(partida)
		total += partida

	dados["gols"] = gols
	dados["total"] = total
	lista.append(dados)
	acao = input("Quer continuar? [S/N]: ")
	if acao in "Nn": break

print 
print ("=-"*30)
print ("cod --- nome -------------- gols ------ total")
for c in range(len(lista)):
	print ("%s - %-15s - %-6s - %-6s"%(c, lista[c]["nome"], lista[c]["gols"], lista[c]["total"]))


while True:
	codigo = int(input("Mostrar dados de qual jogador? (999 para parar): "))
	if codigo == 999: break
	if codigo <= len(lista)-1:
		print ("-- Levantamento do jogador -- %s: "%(lista[codigo]["nome"]))
		for c in range(len(lista[codigo]["gols"])):
			print ("No jogo %s fez %s gol(s)"%(c+1, lista[codigo]["gols"][c]))
	
	else: #Jogador inexistente
		print ("ERRO, não existe jogador com código %s"%codigo)
