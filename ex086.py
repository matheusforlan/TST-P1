#coding:utf-8



matriz = [ [0,0,0], [0,0,0], [0,0,0] ]

for linha in range(3):
	for coluna in range(3):
		adicionado = int(raw_input("Digite um valor para [ {}, {} ]".format(linha,coluna)))
		matriz[linha][coluna] = adicionado 
		
somapares = 0
terceiracol = 0
maiorseg = matriz[1][0]
for linha in range(3):
	for coluna in range(3):
		if matriz[linha][coluna] %2 ==0:
			somapares += matriz[linha][coluna]
		if matriz[linha][coluna] == matriz[linha][2]:
			terceiracol += matriz[linha][coluna]
		if linha == 1:
			if matriz[linha][coluna] > maiorseg:
				maiorseg = matriz[linha][coluna]

print somapares
print terceiracol
print maiorseg
			
		
		
		

