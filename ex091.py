#coding:utf-8
import random
import time
import operator

jogadores = {}
jogadores["jogador1"] = random.randint(1,6)
jogadores["jogador2"] = random.randint(1,6)
jogadores["jogador3"] = random.randint(1,6)
jogadores["jogador4"] = random.randint(1,6)

for k,v in  jogadores.items():
	print "%s tirou %s no dado"%(k,v)
	time.sleep(1)
print "="*50
ranking = []
ranking = sorted(jogadores.items(), key = operator.itemgetter(1), reverse = True)
print ranking
