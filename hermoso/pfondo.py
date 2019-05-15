class fondo:
    negropuro = '\x1b[0;30;40m'
    negro = '\x1b[0;37;40m'
    rojo = '\x1b[0;30;41m'
    verde = '\x1b[0;30;42m'
    amarillo = '\x1b[0;30;43m'
    azul = '\x1b[0;30;44m'
    violeta = '\x1b[0;30;45m'
    celeste = '\x1b[0;30;46m'
    gris = '\x1b[0;30;100m'
    grisclaro = '\x1b[0;30;47m'
    rojoclaro = '\x1b[0;30;101m'
    verdeclaro = '\x1b[0;30;102m'
    amarilloclaro = '\x1b[0;30;103m'
    azulclaro = '\x1b[0;30;104m'
    violetaclaro = '\x1b[0;30;105m'
    celesteclaro = '\x1b[0;30;106m'
    blancopuro = '\x1b[0;37;107m'
    blanco = '\x1b[0;30;107m'
    fin = '\x1b[0m'

	### COLORES ESTÁNDARES ###
	
def negro(text):
	return print (fondo.negro + text + fondo.fin)
	
def rojo(text):
	return print(fondo.rojo + text + fondo.fin)

def verde(text):
	return print(fondo.verde + text + fondo.fin)

def amarillo(text):
	return print(fondo.amarillo + text + fondo.fin)

def azul(text):
	return print(fondo.azul + text + fondo.fin)

def violeta(text):
	return print(fondo.violeta + text + fondo.fin)

def celeste(text):
	return print(fondo.celeste + text + fondo.fin)

def gris(text):
	return print(fondo.gris + text + fondo.fin)

	### COLORES CLAROS ###
	
def grisclaro(text):
	return print(fondo.grisclaro + text + fondo.fin)

def rojoclaro(text):
	return print(fondo.rojoclaro + text + fondo.fin)

def verdeclaro(text):
	return print(fondo.verdeclaro + text + fondo.fin)

def amarilloclaro(text):
	return print(fondo.amarilloclaro + text + fondo.fin)

def azulclaro(text):
	return print(fondo.azulclaro + text + fondo.fin)

def violetaclaro(text):
	return print(fondo.violetaclaro + text + fondo.fin)

def celesteclaro(text):
	return print(fondo.celesteclaro + text + fondo.fin)

def blanco(text):
	return print(fondo.blanco + text + fondo.fin)
	
	### COLORES PUROS ###

def blancopuro(text):
	return print(fondo.blancopuro + text + fondo.fin)

def negropuro(text):
	return print (fondo.negropuro + text + fondo.fin)
