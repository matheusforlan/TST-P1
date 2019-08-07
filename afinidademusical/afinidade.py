#coding:utf-8
def meu_in(elemento,sequencia):
	for e in sequencia:
		if e == elemento:
			return True
	return False

def tem_afinidade(l1, l2):
	afinidade = 0
	
	for c in range(len(l1)):
		if meu_in(l1[c],l2):
			afinidade += 1
	
	if afinidade >= 3:
		return True
	
	return False


l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'u2', 'jquest']
assert tem_afinidade(l1, l2) == True
