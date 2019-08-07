#coding:utf-8
def conta_votos(votacoes,id_votacao):
	sim = 0
	nao = 0
	final = []
	for c in votacoes:
		splitado = c.split(",")
		if int(splitado[2]) == id_votacao:
			if splitado[1] == "sim":
				sim += 1
			elif splitado[1] == "nao":
				nao += 1
	final=[sim, nao]
	return final 
	

votacao = []
votacao.append('greve geral,sim,543,joao,servidor')
votacao.append('greve geral,nao,543,marina,servidor')
votacao.append('indicativo de greve,sim,5,joao,professor')
votacao.append('paralisação,nao,543,julio,professor')
votacao.append('paralisação,sim,543,carlos,professor')
votacao.append('paralisação,sim,543,juliana,professor')
votacao.append('lei 1329,sim,99,joao,servidor')
resultado = (conta_votos(votacao,543))

assert conta_votos(votacao, 543) == [3,2]

