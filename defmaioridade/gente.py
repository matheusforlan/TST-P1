#coding:utf-8

def maioridade_penal(nomes, idades):
	namesplit= nomes.split()
	agesplit = idades.split()
	maiores = ""
	for c in range (len(agesplit)):
		if int(agesplit[c]) >= 18:
			if c == len(agesplit)-1:
				maiores += namesplit[c]
			else:
				maiores += namesplit[c]+" "
	
	

	return maiores
	
			
		
			












assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
