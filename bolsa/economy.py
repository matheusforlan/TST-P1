saldo_acum = []
mes = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]
maior_saldo= 0
maior_mes = []
for c in range(12):
	gastos = int(raw_input())
	if c == 0:
		saldo = 500-gastos
		saldo_acum.append(saldo)
	else:
		saldo = (saldo_acum[c-1])-gastos+500
		saldo_acum.append(saldo)
maior_saldo = saldo_acum[0]
for m in range(len(saldo_acum)):
	if saldo_acum[m] > maior_saldo:
		maior_saldo = saldo_acum[m]
for d in range(len(saldo_acum)):
	if saldo_acum[d] == maior_saldo:
		maior_mes.append(mes[d])
print maior_mes[len(maior_mes)-1]
	
