#coding:utf-8
def conta_alertas_acude(historico):
	alertas = 0
	
	for medicao in range(len(historico)):
		if medicao == 0 and int(historico[medicao]) <17:
			alertas += 1
		else:
			if int(historico[medicao]) < 17 and ((int(historico[medicao]) - int(historico[medicao-1]))*-1) < 10:
				alertas += 1
	
	
	return alertas


medicoes = [50, 50, 50, 23, 21, 17, 15, 60, 65, 15, 15]
assert conta_alertas_acude(medicoes) == 2
