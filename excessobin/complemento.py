#coding:utf-8

def excesso_127(numero):
	return none
	
	
def complemento1(numero):

	binario = bin(int(numero))
	num = ""
	if numero>= 0:
		
		if len(binario[2:]) < 8:
			num = "0" * (8 - len(binario[2:])) + (binario[2:])
	
	else: #número < 0:
		if len(binario[2:]) < 8:
			num = "0" * (8 - len(binario[2:])) + (binario[2:])
			print binario[2:]
			print num
			for i in range(len(num)-1):
				if num[i] == "0":
					num[i] == "1"
				elif num[i] == "1":
					num[i] == "0"
				
	return num
	
	
while True:
	operacao = raw_input()
	if operacao == "***": break
	op_split = operacao.split()
	if op_split[0] == "C1":
		binario = complemento1(op_split[1])
		print binario
