class colores:
    fin = '\033[0m'
    negro        = "\033[30m"
    rojo         = "\033[31m"
    verde        = "\033[32m"
    amarillo     = "\033[33m"
    azul         = "\033[34m"
    violeta      = "\033[35m"
    celeste      = "\033[36m"
    gris         = "\033[90m"
    grisclaro    = "\033[37m"
    rojoclaro    = "\033[91m"
    verdeclaro   = "\033[92m"
    amarilloclaro= "\033[93m"
    azulclaro    = "\033[94m"
    violetaclaro = "\033[95m"
    celesteclaro = "\033[96m"
    blanco       = "\033[97m"

	### COLORES ESTÁNDARES ###
	
def negro(text):
	return (colores.negro + text + colores.fin)

def rojo(text):
	return (colores.rojo + text + colores.fin)

def verde(text):
	return (colores.verde + text + colores.fin)

def amarillo(text):
	return (colores.amarillo + text + colores.fin)

def azul(text):
	return (colores.azul + text + colores.fin)

def violeta(text):
	return (colores.violeta + text + colores.fin)

def celeste(text):
	return (colores.celeste + text + colores.fin)

def blanco(text):
	return (colores.blanco + text + colores.fin)
	
	### COLORES CLAROS ###

def grisclaro(text):
	return (colores.grisclaro + text + colores.fin)

def rojoclaro(text):
	return (colores.rojoclaro + text + colores.fin)

def verdeclaro(text):
	return (colores.verdeclaro + text + colores.fin)

def amarilloclaro(text):
	return (colores.amarilloclaro + text + colores.fin)

def azulclaro(text):
	return (colores.azulclaro + text + colores.fin)

def violetaclaro(text):
	return (colores.violetaclaro + text + colores.fin)

def celesteclaro(text):
	return (colores.celesteclaro + text + colores.fin)
	
	### COLORES PERSONALIZADOS ###

def custom(text,color,fondo):
	return print( '\x1b[0;'+str(color)+';'+str(fondo)+'m' + text + colores.fin)