#coding:utf-8
preco = float(raw_input("Digite o preço da unidade do tijolo (Em reais): "))
altij = float(raw_input("Digite a altura do tijolo (Em metros): "))
comtij = float(raw_input("Digite o comprimento do tijolo (Em metros): "))
alpar = float(raw_input("Digite a altura das paredes (Em metros): "))
compar = float(raw_input("Digite o comprimento das paredes (Em metros): "))
num_tij_al = alpar/altij
num_tij_com = compar/comtij
num_tij_total = num_tij_al*num_tij_com
orcamento = num_tij_total * preco
print "O número total de tijolos é {:.1f} e o orçamento final é de R$ {:.1f}".format(num_tij_total,orcamento)
