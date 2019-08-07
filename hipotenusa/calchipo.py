#coding: utf-8
import math
cat1 = float(raw_input("Medida do Cateto 1? "))
cat2 = float(raw_input("Medida do Cateto 2? "))
hip = math.sqrt(cat1**2 + cat2**2)
print "Medida da Hipotenusa: %.2f"%(hip)
