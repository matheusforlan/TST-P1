#coding:utf-8
nome = (raw_input())
horas_extra = float(raw_input())
minimo = float(raw_input())
valordahora = float(raw_input())
sal_horaextra = valordahora*horas_extra
sal_bruto = 4*minimo+sal_horaextra
inss = sal_bruto*0.12
ir = sal_bruto*0.20
sal_liq = sal_bruto - ir - inss
print "O Salário Bruto de {} é de R$ {:.2f}".format(nome, sal_bruto)
print "O Salário Líquido de {} é de R$ {:.2f}".format(nome, sal_liq)
