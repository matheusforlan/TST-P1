#coding:utf-8
n1 = float(raw_input())
n2 = float(raw_input())
n3 = float(raw_input())
peso1=float(raw_input())
peso2 = float(raw_input())
peso3 = 100-peso1-peso2
media = (n1*(peso1/100)+n2*(peso2/100) +n3*(peso3/100))/(peso1/100+peso2/100+peso3/100)
print "Média Final: {:.1f}".format(media)
