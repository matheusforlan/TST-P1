#coding:utf-8

def meu_join(delimitador, sequencia_de_string):
	nova_seq = ""
	
	for c in range(len(sequencia_de_string)):
		if c == (len(sequencia_de_string)-1):
			nova_seq += sequencia_de_string[c]
		else:
			nova_seq += sequencia_de_string[c]
			nova_seq += delimitador
	

	return nova_seq
	
assert meu_join("*", "abcde") == "a*b*c*d*e"
assert meu_join("*", "abc") == "a*b*c"
assert meu_join("*", ["a", "b", "c"]) == "a*b*c"
assert meu_join("*", "a") == "a"
assert meu_join ("*", "ab c ")== "a*b* *c* "
assert meu_join("*", ["a","b","c","d","e"]) == "a*b*c*d*e"
assert meu_join("*", "ab") == "a*b"
		
