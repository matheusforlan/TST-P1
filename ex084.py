#coding:utf-8

pessoas = []
contador = 0
while True:
	lst_nomepeso = []
	
	nome = raw_input("Nome: ")
	lst_nomepeso.append(nome)
	peso = float(raw_input("Peso: "))
	lst_nomepeso.append(peso)
	pessoas.append(lst_nomepeso)
	contador += 1
	
	continuar = raw_input("Quer continuar? [s/n]: ")
	if continuar in "nN": break

maior = pessoas[0][1]
menor = pessoas[0][1]
for c in range (len(pessoas)):
	if pessoas[c][1] > maior:
		maior = pessoas[c][1]
	if pessoas[c][1] < menor:
		menor = pessoas[c][1]

maiores = []
menores = []

for j in range(len(pessoas)):
	if pessoas[j][1]== maior:
		maiores.append(pessoas[j][0])
	elif pessoas[j][1] == menor:
		menores.append(pessoas[j][0])
		
		
print "Ao todo, você cadastrou {} pessoas".format(pessoas)
print "O maior peso foi de %.1f peso de %s"%(maior,maiores) 
print "O menor peso foi de %1.f peso de %s"%(menor,menores)
	
	
