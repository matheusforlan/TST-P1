b = raw_input()
lista_bin = []
lista_bin.append(b)
diminuidor = 1
decimal = 0
soma = 0
pos = 0
for c in b:
	expoente = 2**(len(b)-diminuidor)
	decimal = int(c)*expoente
	print "{} * {} = {}".format(int(c),expoente,decimal)
	diminuidor += 1
	soma += decimal
	pos+=1
print "{}(2) = {}(10)".format(b,soma)
	
