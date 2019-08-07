#coding:utf-8
conta = raw_input()
soma = int(conta[0])+int(conta[1])+int(conta[2])+int(conta[3])+int(conta[4])
verf = soma%11
print "%s-%02d"%(conta, verf)


