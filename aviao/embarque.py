#coding:utf-8
identificador = raw_input()
horario = raw_input()
assento = raw_input()
portao = raw_input()
preco_semi= float(raw_input())
preco_comi = float(raw_input())
print "### Cartão de Embarque ###"
print "Identificador do voo: {}. Horário: {}. Assento: {}. Portão: {}.".format(identificador,horario,assento,portao)
imposto = (preco_comi-preco_semi)*100/preco_comi
print "Total de Imposto: {:.1f}%.".format(imposto)
