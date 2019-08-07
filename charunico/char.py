#coding:utf-8
def contastrings(davez,sequencia):
	repeticao = 0
	for c in sequencia:
		if c == davez:
			repeticao += 1
	
	return repeticao
			
def char_unico(string):
	unica = " "
	
	for letra in string:
		quantidade = contastrings(letra,string)
		if quantidade == 1:
			unica = letra
	
	return unica

		
	
assert char_unico("aa***xxxzzb+++") == "b"
assert char_unico("bbbbbbgkkkk") == "g"
