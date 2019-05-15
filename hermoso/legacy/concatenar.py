class concatenar:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    VERDE = '\x1b[6;30;42m'
    AZUL = '\x1b[0;30;44m'
    ROJO = '\x1b[0;30;41m'
    BLANCO = '\x1b[7;37;40m'
    AMARILLO = '\x1b[0;30;43m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    CURSIVA = '\x1b[3;37;40m'
    ENDC = '\x1b[0m'



def violeta(text):
	return (concatenar.HEADER + text + concatenar.ENDC)

def azul(text):
	return (concatenar.OKBLUE + text + concatenar.ENDC)

def verde(text):
	return (concatenar.OKGREEN + text + concatenar.ENDC)

def amarillo(text):
	return (concatenar.WARNING + text + concatenar.ENDC)

def rojo(text):
	return (concatenar.FAIL + text + concatenar.ENDC)

def mverde(text):
	return print (concatenar.VERDE + text + concatenar.ENDC)

def mazul(text):
	return print(concatenar.AZUL + text + concatenar.ENDC)

def mrojo(text):
	return print(concatenar.ROJO + text + concatenar.ENDC)

def mblanco(text):
	return print(concatenar.BLANCO + text + concatenar.ENDC)

def mamarillo(text):
	return print(concatenar.AMARILLO + text + concatenar.ENDC)

def negrita(text):
	return print(concatenar.BOLD + text + concatenar.ENDC)

def subrayado(text):
	return print(concatenar.UNDER + text + concatenar.ENDC)

def cursiva(text):
	return print(concatenar.CURSIVA + text + concatenar.ENDC)

def texto(text,color):
	return print( '\x1b[0;'+str(color)+';40m' + text + concatenar.ENDC)