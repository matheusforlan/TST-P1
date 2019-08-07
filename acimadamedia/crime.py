ssp = float(raw_input())

lista = []

while True:
	ocorrencia = raw_input()
	if ocorrencia == "fim":break
	seq = ocorrencia.split()
	soma = 0
	for c in seq:
		soma += int(c)
	media = float(soma)/len(seq)
	if media < ssp/2: break
	if media > ssp:
		lista.append(ocorrencia)
for m in lista:
	print m
		
	
