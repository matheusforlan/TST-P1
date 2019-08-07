#coding:utf-8


dados = {}

dados["nome"] = raw_input("Nome: ")
dados ["media"] = float(raw_input("Média de %s: "%(dados["nome"])))
print "===="*50
print "Seu nome é: %s"%dados["nome"]
print "Sua média é igual a: %.1f"%dados["media"]

if dados["media"] >= 7:
	print "Situação: Aprovado"
elif dados["media"] > 5:
	print "Situação: Em recuperação"
else:
	print "Situação: Reprovado"
