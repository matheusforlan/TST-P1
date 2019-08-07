#coding:utf-8
def maior_palavra(frase):
	palavra = ""
	tamanho = 0
	maior = ""
	if len(frase) == 1:
		maior += frase[0]
	
	else:
		for c in range(len(frase)-1):
			if c == (len(frase)-2): #penúltima letra
				if frase[c+1] != " " and frase[c] != " ":
					tamanho += 2
					palavra += frase[c]
					palavra += frase[c+1]
					if tamanho >= len(maior):
						maior = palavra
					
				elif frase[c+1] == " ":
					tamanho += 1
					palavra += frase[c]
					if tamanho >= len(maior):
						maior = palavra
					
				else:
					tamanho += 1
					palavra += frase[c+1]
					if tamanho >= len(maior):
						maior = palavra
			
			elif frase[c+1] == " ": #fim da palavra e o teste
				tamanho += 1
				palavra += frase[c]
				if tamanho >= len(maior):
					maior = palavra
					palavra = ""
					tamanho = 0
				else:
					palavra = ""
					tamanho = 0
	
			
			elif frase[c+1] != " " and frase[c] != " ": #Para não contar o espaço na palavra e ir criando a nova palavra
				tamanho += 1
				palavra += frase[c]

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


