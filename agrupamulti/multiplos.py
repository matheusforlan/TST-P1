#coding:utf-8

def agrupa_multiplos(seq, k):
	for c in range(len(seq)-1,-1,-1):
		for j in range(len(seq)-1,0,-1):
			if seq[j] % k== 0 and seq[j-1]% k!= 0:
				seq[j-1], seq[j] = seq[j], seq[j-1]
				
	print seq
	

	
	
seq = [6, 15, 12, 6, 8, 3, 25, 14, 1, 10, 7]

# agrupando seq por múltiplos de 5
agrupa_multiplos(seq, 5)
assert seq == [15, 25, 10, 6, 12, 6, 8, 3, 14, 1, 7]

# reagrupando por pares
agrupa_multiplos(seq, 2)
assert seq == [10, 6, 12, 6, 8, 14, 15, 25, 3, 1, 7]
