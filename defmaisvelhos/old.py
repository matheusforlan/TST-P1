#coding:utf-8

def idosos_inicio(fila):
	idoso = 0
	for pos in range (len(fila)):
		if fila[pos] >= 60:
			fila[idoso], fila[pos] = fila[pos], fila[idoso]
			idoso += 1
	
			
		


fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)
assert fila == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]
