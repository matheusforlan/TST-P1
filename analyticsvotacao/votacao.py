#coding:utf-8

def conta_votos(votacoes, _id):
	sim = 0
	nao = 0
	for voto in votacoes:
		splitado = voto.split(",")
		if int(splitado[1]) == int(_id):
			if splitado[-1] == "sim":
				sim += 1
			elif splitado[-1] == "nao":
				nao+=1

	return [sim, nao]
			 
	
	
	
	
votacao = ['lei sobre bancos,543,joao,PPPP,sim', 'lei sobre bancos,543,marina,PPPP,nao', 'lei maria da penha,5,joao,PPPP,sim',  'lei sobre bancos,543,julio,P,nao', 'lei sobre bancos,543,carlos,PBBBB,sim',  'lei sobre bancos,543,juliana,PP,sim', 'lei das brs,99,joao,PPPP,sim']
assert conta_votos(votacao, 543) == [3, 2]
 
