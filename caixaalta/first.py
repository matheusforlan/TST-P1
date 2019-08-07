

def caixa_alta(frase):
	altada = ""
	pos = 0
	for m in frase:
		if m == frase[0]:
			altada += m.lower()
		elif frase[pos-1]== " ":
			altada += m.upper()
		else:
			altada += m
		pos += 1
	return "%s"%altada



assert caixa_alta("A primeira letra de cada palavra")=="a Primeira Letra De Cada Palavra"
assert caixa_alta("A")=="a"
