#coding:utf-8
n1 = int(raw_input())
n2 = int(raw_input())
n3 = int(raw_input())
n4 = int(raw_input())
n5 = int(raw_input())
soma = n1+n2+n3+n4+n5
media = soma*1.0/5
produtividade = soma*1.0/7200
episodios = soma/50
print "Você perdeu {} min na semana (média de {:.1f} min por dia).".format(soma,media)
print "Isso significa {:.2f}% da sua semana produtiva.".format(produtividade*100)
print "Daria para assistir {} episódio(s) de House.".format(episodios) 
