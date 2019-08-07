#coding:utf-8
def media_geometrica(numeros):
	soma = 1
	for j in numeros:
		soma  *= float(j)
	media_g = float(soma)**(1/float(len(numeros)))
	return "%.4f"%media_g

def media_aritmetica(numeros):
	soma = 0
	for c in numeros:
		soma += float(c)
	media = float(soma)/len(numeros)
	return "%.4f"%media

def media_harmonica(numeros):
	soma = 0
	for i in numeros:
		soma += 1/float(i)
	media = len(numeros)/soma
	return "%.4f"%media
	

while True:
	modo = raw_input()
	modo_split = []
	if modo == "Q": break
	modo_split = modo.split()
	if len(modo_split) != 1:
		numeros = raw_input().split()
		for op in range(len(modo_split)):
			if modo_split[op] == "MA":
				resultadoa = media_aritmetica(numeros)
				print "Média Aritmética: %s"%resultadoa
			if modo_split[op] == "MG":
				resultadog = media_geometrica(numeros)
				print "Média Geométrica: %s"%resultadog
			if modo_split[op] == "MH":
				resultadoh = media_harmonica(numeros)
				print "Média harmônica: %s"%resultadoh
		print "----"
	else:
		if modo_split[op] == "MA":
			numeros = raw_input().split()
			resultado = media_aritmetica(numeros)
			print "Média Aritmética: %s"%resultado
		if modo_split[op] == "MG":
			numeros = raw_input().split()
			resultado = media_geometrica(numeros)
			print "Média Geométrica: %s"%resultado
		if modo_split[op] == "MH":
			numeros = raw_input().split()
			resultado = media_harmonica(numeros)
			print "Média harmônica: %s"%resultado
		
		
		











