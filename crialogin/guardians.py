#coding:utf-8
def meu_in(elemento,sequencia):
	for e in sequencia:
		if e == elemento:
			return True
		
	return False

def cria_login(nome):
	split_nome= nome.split()
	login = ""
	login += split_nome[0].lower()
	conectores = ["de","da","do"]
	for c in range(1,len(split_nome)):
		if  not meu_in(split_nome[c],conectores):
			login += split_nome[c][0].lower()

	return login


while True:
	name = raw_input()
	if name == "fim":break
	login = cria_login(name)
	print "%s: %s"%(name,login)
