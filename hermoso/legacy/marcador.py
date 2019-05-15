class fondo:
    negro = '\x1b[0;30;40m'
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
    blanco = '\x1b[0;37;107m'
    blancopuro = '\x1b[0;30;107m'
    fin = '\x1b[0m'
	
	BackgroundDefault      = "\033[49m"
    BackgroundBlack        = "\033[40m"
    BackgroundRed          = "\033[41m"
    BackgroundGreen        = "\033[42m"
    BackgroundYellow       = "\033[43m"
    BackgroundBlue         = "\033[44m"
    BackgroundMagenta      = "\033[45m"
    BackgroundCyan         = "\033[46m"
    BackgroundLightGray    = "\033[47m"
    BackgroundDarkGray     = "\033[100m"
    BackgroundLightRed     = "\033[101m"
    BackgroundLightGreen   = "\033[102m"
    BackgroundLightYellow  = "\033[103m"
    BackgroundLightBlue    = "\033[104m"
    BackgroundLightMagenta = "\033[105m"
    BackgroundLightCyan    = "\033[106m"
    BackgroundWhite        = "\033[107m"

def verde(text):
	return print (marcador.VERDE + text + marcador.ENDC)

def azul(text):
	return print(marcador.AZUL + text + marcador.ENDC)

def rojo(text):
	return print(marcador.ROJO + text + marcador.ENDC)

def blanco(text):
	return print(marcador.BLANCO + text + marcador.ENDC)

def amarillo(text):
	return print(marcador.AMARILLO + text + marcador.ENDC)