#coding:utf-8
def meu_in(elemento, seq):
	for e in seq:
		if e == elemento:
			return True
			
	return False
def acordes(musica_1, musica_2):
	aprendidos = []
	
	for c in range (len(musica_1)):
		aprendidos.append(musica_1[c])
	for m in range(len(musica_2)):
		if  not meu_in(musica_2[m], aprendidos):
			aprendidos.append(musica_2[m])
	
	#print aprendidos
	return aprendidos
	
	

m1 = ['c', 'd', 'dm']
m2 = ['c', 'a']
assert acordes(m1, m2) == ['c', 'd', 'dm', 'a']
assert m1 == ['c', 'd', 'dm']
assert m2 == ['c', 'a']

m1 = ['c', 'd']
m2 = ['c', 'a']
assert acordes(m1, m2) == ['c', 'd', 'a']
