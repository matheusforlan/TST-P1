#coding:utf-8



def bubblesort(dados):
	for c in range(len(dados)):
		for j in range(0,len(dados)-1,1):
			if dados[j] > dados[j+1]:
				dados[j],dados[j+1] = dados[j+1], dados[j]
				
