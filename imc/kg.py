kg = float(raw_input())
m = float(raw_input())
imc = kg/(m**2)
print "IMC atual = {:.2f}".format(imc)
ideal = 24.9*(m**2)
imcideal = ideal - kg
print "Peso a ser ganho/perdido = {:.2f}".format(imcideal)
