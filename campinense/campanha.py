#coding:utf-8
campanha = []
vitorias = 0
empates= 0
derrotas = 0
pontos_casa = 0
pontos_fora = 0
gols_pro = 0
gols_contra = 0
for c in range(10):
	jogos = raw_input()
	campanha.append(jogos)
for mando in campanha:
	if mando[5] == "c":
		if int(mando[0]) > int(mando[2]):
			vitorias += 1
			pontos_casa += 3
		elif int(mando[0]) == int(mando[2]):
			empates += 1
			pontos_casa+= 1
		else:
			derrotas += 1
		gols_pro += int(mando[0])
		gols_contra += int(mando[2])
	elif mando[5] == "f":
		if int(mando[0]) > int(mando[2]):
			derrotas+= 1
			
		elif int(mando[0]) == int(mando[2]):
			empates += 1
			pontos_fora += 1
		
		else:
			vitorias += 1
			pontos_fora += 3
		gols_pro+= int(mando[2])
		gols_contra += int(mando[0])
print "{}v, {}e, {}d".format(vitorias,empates,derrotas)
print "pontos: {}".format(vitorias*3+empates*1)
print "saldo: {} ({} pro, {} contra)".format(gols_pro-gols_contra, gols_pro, gols_contra)
print "pontos em casa: {}".format(pontos_casa)
print "pontos fora: {}".format(pontos_fora)

		
