
def caixa_alta(frase):
	altada = ""
	
	for m in range(len(frase)):
		if len(frase) > 1:
			if m==0:
				if frase[m+1] == " ":
					altada += frase[m].lower()
				else:
					altada += frase[m].upper()
			elif m==(len(frase)-1):
				if frase[m-1] == " ":
					altada += frase[m].lower()
				else:
					altada += frase[m]
			else:
				if frase[m-1] == " " and frase[m+1] == " ":
					altada += frase[m].lower()
				elif frase[m-1] == " " and frase[m+1] != " ":
					altada += frase[m].upper()
				else:
					altada += frase[m]
		
		else:
			altada += frase[m].lower()
			
	return "%s"%altada


assert caixa_alta("A primeira letra de cada palavra")=="a Primeira Letra De Cada Palavra"

		
