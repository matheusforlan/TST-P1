#coding:utf-8
def inverte2a2_condicional(seq):
	
	if len(seq)%2 ==0:
		for c in range(0,len(seq)-1, 2):
			if seq[c] > seq[c+1]:
				seq[c], seq[c+1] = seq[c+1], seq[c]
	else:     #sequencia ímpar
		for m in range(0, len(seq)-2,2):
			if seq[m] > seq[m+1]:
				seq[m], seq[m+1] = seq[m+1], seq[m]	
	
	
	
seq = [3,1,2,3,10,5,6,5]
inverte2a2_condicional(seq)
assert seq == [1,3,2,3,5,10,5,6]

seq = [5,4,3,2,1]
inverte2a2_condicional(seq)
assert seq == [4,5,2,3,1]
