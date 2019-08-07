#coding:utf-8

dados = {}

nome = raw_input("Nome: ")
nascimento = int(raw_input("Data de nascimento: "))
ctps = int(raw_input("Carteira de trabalho (0 não tem):" ))
idade = 2019-nascimento
if ctps != 0:
	ano_in = int(raw_input( "Ano de contratação: "))
	salario = int(raw_input("Salário:  R$"))
	idade_in = ano_in - nascimento
	dados["nome"] = nome
	dados["idade"] = idade
	dados["ctps"] = ctps
	trabalhado = 2019 - ano_in
	restante = 35- trabalhado
	aposentadoria = restante + idade_in + trabalhado
	dados["aposentadoria"] = aposentadoria
	dados["salário"] = salario
	print dados
	for k,v in dados.items():
		print "%s tem o valor %s"%(k,v)
	
else:
	dados["nome"] = nome
	dados["idade"] = idade
	dados["ctps"] = ctps
	print dados
	for k,v in dados.items():
		print "%s tem o valor %s"%(k,v)
