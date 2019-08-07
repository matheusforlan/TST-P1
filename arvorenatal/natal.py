n = int(raw_input())
beira = 0
meio = 1
espaco = 1
for c in range (n):
	print " "*(n-espaco)+"o"*(meio+beira)
	beira += 2
	espaco += 1
print " "*(((meio+beira)/2)-1)+"o"
	
