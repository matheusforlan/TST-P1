#coding:utf-8
frasebcd = "BCD inválido."
listafinal = []
frasewrong = "Tente novamente."
while True:
	bimn = raw_input()
	if bimn == "fim":break
	if len(bimn) == 8:
		bin1 = ""
		bin2 = ""
		dec1 = 0
		dec2 = 0	
		lista1 = []
		lista2 = []
		for c in range(4):
			lista1.append(bimn[c])
		for m in range(4,8):
			lista2.append(bimn[m])
		for num1 in lista1:
			bin1 += num1
		for num2 in lista2:
			bin2 += num2
		dec1 = int("{}".format(bin1),2) #primeiro digito
		dec2 = int("{}".format(bin2),2) #segundo digito
		decfinal = str(dec1)+str(dec2) #Os dois dígitos juntos
		if dec1 <= 9 and dec2 <= 9:
			listafinal.append(decfinal)
		else:
			listafinal.append(frasebcd)
			
	else:
		listafinal.append(frasewrong)
		
		
for bcd in listafinal:
	print bcd
	
