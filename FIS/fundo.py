#coding:utf- 8 
soma = 0
quantidade = 0

while True:
	valor = float(raw_input())
	soma += valor
	quantidade += 1
	media = 1.0*soma/quantidade
	if valor < media: break
	
print "Saldo total do FIS: R$%.2f."%(soma-valor)
print "Média das contribuições: R$%.2f."%((soma-valor)/(quantidade-1))
