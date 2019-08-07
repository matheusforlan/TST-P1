#coding:utf-8
lista = []

while True:
	dados = {}
	dados["nome"] = raw_input("Nome: ")
	dados["sexo"] = raw_input("Sexo [M/F]: ")
	dados["idade"] = int(raw_input("Idade: "))
	lista.append(dados)
	acao = raw_input("Você quer continuar? [S/N]: ")
	if acao in "Nn": break

print "=-"*30
print "O grupo tem %s pessoas"%(len(lista))
soma = 0
for c in range(len(lista)):
	soma += float(lista[c]["idade"])
media = soma/len(lista)
print "A média de idade é %.2f anos"%media
print ("As mulheres cadastradas foram: ")
for c in range(len(lista)):
	if lista[c]["sexo"] in "Ff":
		print lista[c]["nome"]
print "Lista das pessoas com idade acima da média"
for l in range(len(lista)):
	for k,v in lista[l].items():
		if lista[l]["idade"] > media:
			print " %s = %s"%(k,v) 
	print "="*10
