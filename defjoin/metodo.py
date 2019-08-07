#coding:utf-8

def meu_join(delimitador, sequencia_de_string):
	nova_seq = ""
	if len(sequencia_de_string) == 1:
		return sequencia_de_string
	else:
		for c in range(len(sequencia_de_string)-1):
			if c == (len(sequencia_de_string)-2):
				nova_seq += sequencia_de_string [c]
				nova_seq += delimitador
				nova_seq += sequencia_de_string[c+1]
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
