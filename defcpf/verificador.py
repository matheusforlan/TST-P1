#coding:utf-8

def calcula_digitos_verificacao(cpf):
	primeiro = 0
	segundo = 0
	multi_prim = 2
	multi_seg = 3
	
	for c in range(8,-1, -1):
		primeiro += int(cpf[c])*multi_prim
		multi_prim += 1
		
	primeiro = (10*primeiro)%11
	if primeiro == 10:
		primeiro = 0
	segundo += primeiro*2
	for m in range(8, -1, -1):
		segundo += int(cpf[m])*multi_seg
		multi_seg += 1
	
	segundo =  10*(segundo) %11
	
	if segundo == 10:
		segundo = 0
		
	return str(primeiro)+str(segundo)
	
	
assert calcula_digitos_verificacao('153245875') == '40'

