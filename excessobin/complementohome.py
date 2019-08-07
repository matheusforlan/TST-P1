#coding:utf-8

def excesso_127(numero):
	num = ""
	binario_n = bin(int(numero)-1)
	#print binario_n
	if int(numero)>0:
		binario_n = bin(int(numero)-1)
		num = "1"+ "0"*(7-len(binario_n[2:])) + ((binario_n[2:]))
		return num
	
	elif int(numero)<0:
		binario_n = bin(127 + int(numero))
		num = "0" + "0"*(7-len(binario_n[2:])) + ((binario_n[2:]))
		return num
			
	else: #int(numero) == 0:
		return "01111111"
	
	
	
def complemento1(numero):

	binario = bin(int(numero))
	num = ""
	num_neg = ""
	if int(numero) >= 0:
		
		if len(binario[2:]) < 8:
			num = "0" * (8 - len(binario[2:])) + (binario[2:])
			return num
	
	else: #número < 0:
		if len(binario[3:]) < 8:  #TIRAR O "-0b"  
			num = "0" * (8 - len(binario[3:])) + (binario[3:])
		for i in range(len(num)):
			if num[i] == "0":
				num_neg += "1"
			else: # num[i] == "1":
				num_neg += "0"
		return num_neg
	
	
while True:
	operacao = raw_input()
	if operacao == "***": break
	op_split = operacao.split()
	if op_split[0] == "C1":
		binario_global = complemento1(op_split[1])
		print binario_global
	elif op_split[0] == "E127":
		binario_global2 = excesso_127(op_split[1])
		print binario_global2
