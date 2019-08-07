#coding:utf-8

while True:
	codigo = raw_input().split()
	if codigo[0] == "5":break
	if codigo[0] == "1":
		print int(codigo[1])+int(codigo[2])
	elif codigo [0] == "2":
		print int(codigo[1])-int(codigo[2])
	elif codigo [0] ==  "3":
		print int(codigo[1])*int(codigo[2])
	elif codigo [0] == "4":
		if codigo [2] == "0":
			print "Erro: Divisão por 0"
			break
		else:
			print int(codigo[1]) / int(codigo [2])
	
