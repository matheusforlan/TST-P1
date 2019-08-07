#coding:utf-8
dist = float(raw_input())
aliquota = float(raw_input())
passagem = (dist*aliquota+51)*1.0
seis = passagem*1.0-(0.05*passagem*1.0)
print "Valor da passagem: R$ {:.2f}".format(passagem)
print ""
print "Pagamento:"
print "1. À vista. R$ {:.2f}".format(passagem-(0.25*passagem))
print "2. Em 6 parcelas. Total: R$ {:.2f}".format(seis)
print "   6 x R$ {:.2f}".format(seis/6)
print "3. Em 10 parcelas. Total: R$ {:.2f}".format(passagem)
print "   10 x R$ {:.2f}".format(passagem/10)
