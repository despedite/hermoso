class formato:
    negrita    = "\033[1m"
    cursiva    = "\033[2m"
    subrayado  = "\033[4m"
    reverso    = "\033[7m"
    fin = '\x1b[0m'

	### ACCIONES DE FORMATO ###
	
def negrita(text):
	return (formato.negrita + text + formato.fin)

def subrayado(text):
	return (formato.subrayado + text + formato.fin)

def cursiva(text):
	return (formato.cursiva + text + formato.fin)

def reverso(text):
	return (formato.reverso + text + formato.fin)

### LIMPIAR PANTALLA ###

def limpiar():
	import os
	return os.system('cls')
