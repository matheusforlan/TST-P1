estrategia = "ok"

pos = 0
ordem = raw_input().split()
for c in range(len(ordem)-1):
	if (int(ordem[pos])%2 == 0) and (int(ordem[pos+1])%2 != 0):
		estrategia = "erro"
	pos += 1
print estrategia
	
