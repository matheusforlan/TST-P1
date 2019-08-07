#coding:utf-8
def maior_palavra(frase):
	palavra = ""
	maior =""
	ultima = ""
	if len(frase) == 1:
		maior += frase[0]
	else:
		for c in range(len(frase)):
			if frase[c] != " ":
				palavra += frase[c]
				ultima += frase[c]
			else:
				if len(palavra) >= len(maior):
					maior = palavra
					palavra = ""
					ultima = ""
				else:
					palavra= ""
					ultima = ""
					
		if len(ultima) >= len(maior):
			maior = ultima
	print maior
	return maior
	
	
assert maior_palavra("eu acredito que seja um bom exemplo") == "acredito"
assert maior_palavra("Maior eh aquis") == "aquis"
assert maior_palavra("Aqui eh a maismaior maior") == "maismaior"
assert maior_palavra("Aqui eh a maismaior") == "maismaior"
assert maior_palavra("Primeiramente  eh a maismaior") == "Primeiramente"
assert maior_palavra("Aqui") == "Aqui"
assert maior_palavra("a e i o u") == "u"
assert maior_palavra("Aqui eh a maismaior ") == "maismaior"
assert maior_palavra ("a") == "a"
assert maior_palavra ("a ") == "a"

	
