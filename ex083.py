#coding:utf-8

aberto = 0
fechado = 0
expressao = raw_input("Digite a expressão: ")
sequencia = True
for c in expressao:
	if c == "(":
		aberto += 1
		
	elif c == ")":
		fechado += 1
		if fechado > aberto:
			sequencia = False
			break

if aberto == fechado and sequencia == True:
	print "sua expressão está certa"
else:
	print "sua expressão está errada"
