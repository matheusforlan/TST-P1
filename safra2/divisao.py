kg = int(raw_input())
atacado = int(raw_input())
varejo = int(raw_input())
kg_ata = kg/atacado
sobra = 1.0*kg-(kg_ata*atacado)
kg_var = sobra/varejo
print "Clientes no atacado = {}kg cada.".format(kg_ata)
print "Clientes no varejo = {:.2f}kg cada.".format(kg_var)
