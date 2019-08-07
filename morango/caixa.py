#coding:utf-8
quant = int(raw_input())
caixas = (quant/400)
fora = float(quant-(caixas*400))
print "Serão necessárias {} caixa(s) para embalar os morangos.".format(caixas)
perdidos = fora*100/(quant*1.0)
print "{:.1f}% dos morangos serão perdidos.".format(perdidos)

