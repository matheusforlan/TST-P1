atual = float(raw_input("Valor atual? "))
novo = float(raw_input("Novo valor? "))
aumento = (novo/atual)*100
reajuste = aumento-100
print "Reajuste de {:.1f}%".format(reajuste)
