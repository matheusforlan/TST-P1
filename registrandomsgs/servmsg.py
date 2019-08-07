#coding: utf-8
mensagem = raw_input()
timestamp = int(raw_input())
fuso = int(timestamp + 300)
print "%s - %i"%(mensagem, fuso)
