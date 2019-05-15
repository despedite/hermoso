class colores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    fin = '\033[0m'
    Negro        = "\033[30m"
    Rojo         = "\033[31m"
    Verde        = "\033[32m"
    Amarillo     = "\033[33m"
    Azul         = "\033[34m"
    Magenta      = "\033[35m"
    Cyan         = "\033[36m"
    Gris         = "\033[90m"
    GrisClaro    = "\033[37m"
    RojoClaro    = "\033[91m"
    VerdeClaro   = "\033[92m"
    AmarilloClaro= "\033[93m"
    AzulClaro    = "\033[94m"
    MagentaClaro = "\033[95m"
    CyanClaro    = "\033[96m"
    Blanco       = "\033[97m"

def negro(text):
	return print (colores.negro + text + colores.fin)

def rojo(text):
	return print (colores.rojo + text + colores.fin)



def violeta(text):

def azul(text):
	return print(colores.OKBLUE + text + colores.ENDC)

def verde(text):
	return print(colores.OKGREEN + text + colores.ENDC)

def amarillo(text):
	return print(colores.WARNING + text + colores.ENDC)

def rojo(text):
	return print(colores.FAIL + text + colores.ENDC)