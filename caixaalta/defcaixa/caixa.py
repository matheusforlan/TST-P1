#coding:utf-8
def caixa_registradora(vendas,meta):
	soma_dia = 0
	comissoes = 0
	
	for venda in vendas:
		if float(venda)< 1000.0:
			comissoes += (float(venda)*0.05)
			soma_dia += float(venda)
		elif float(venda)>= 1000.0 and float(venda) < 5000.0:
			comissoes += (float(venda)*0.10)
			soma_dia += float(venda)
		elif float(venda) >= 5000.0:
			comissoes += (float(venda)*0.15)
			soma_dia += float(venda)
	if soma_dia < meta:
		situacao = "Prejuizo"
	else:
		if soma_dia - comissoes >= meta:
			situacao = "Lucro"
		else:
			situacao = "Prejuizo"
	
	return [soma_dia, comissoes, situacao]



	
assert caixa_registradora([1000.0, 2000.0, 5000.0, 2500.0, 950.0], 2000.0) == [11450.0, 1347.5, 'Lucro']
