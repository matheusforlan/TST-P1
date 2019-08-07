#coding:utf-8
print "Análise da Turma"
print "==="
aprov = int(raw_input("Número de aprovados? "))
reprov = int(raw_input("Número de reprovados? "))
print "---"
total = float(aprov+reprov)
print "Total de alunos na turma: {}".format(aprov+reprov)
print "Aprovados: {} = {:.1f}%".format(aprov, aprov*100/total)
print "Reprovados: {} = {:.1f}%".format(reprov, reprov*100/total)
