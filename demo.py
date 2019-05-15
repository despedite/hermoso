## DEPENDENCIAS DE hermoso.py ##

from hermoso import color # Dependencia de color - para usar en un print("").
from hermoso import pcolor # Dependencia de color - un color y print("") todo en uno.
from hermoso import fondo # Dependencia de fondo - para usar en un print("").
from hermoso import pfondo # Dependencia de fondo - un fondo y print("") todo en uno.
from hermoso import formato # Dependencia de formato - para usar en un print("").
from hermoso import pformato # Dependencia de formato - formateo y print("") todo en uno.

#Limpia la pantalla. Es equivalente a un os.system("cls") si tenés integrada esa librería.
formato.limpiar()

print("Esto es un ejemplo de como usar " + color.amarillo("hermoso.py ") + "en tus proyectos!")
print("Para entender mejor como funciona el código, ingresa a el " + color.rojo("código fuente") + ".")

print("\n")
#Usamos la herramienta PFONDO cuando queremos imprimir un texto con fondo en una línea. También aplica a PCOLOR y PFORMATO.
pfondo.blanco(" ** EJEMPLOS ** ")
print("")
pcolor.verdeclaro("Usando el módulo pcolor, podés escribir una línea entera en un tipo de color!")
#Usamos la herramienta COLOR adentro de un print para cuando querés escribir de color una parte en específico. Fambién aplica a FONDO y FORMATO.
print("Si en cambio solo querés escribir una palabra en una línea, podés usar " + color.azul("el módulo color ") + "para hacerlo.")
#Usamos la herramienta FONDO para llenar un texto de un color de fondo. Increíble.
print("Con el módulo " + fondo.azul("FONDO") + " vas a poder ponerle un color en específico al fondo de texto.")
pfondo.celeste("Hey! También podés usar PFONDO para hacerlo en una línea entera.")
#Usamos la herramienta FORMATO (o PFORMATO) para opciones de formatar el texto. Por ejemplo, NEGRITA, CURSIVA, SUBRAYADO, y REVERSA.
print("También admite para " + formato.subrayado("herramientas de formato!") + " Mirá que tán " + formato.negrita("grueso") + " que quedó este texto. Y este se ve tan " + formato.cursiva("finito") + "! Puede no mostrarse en ciertas lineas de comando.")
#Usamos la herramienta CUSTOM en COLOR (o PCOLOR) para personalizar el color de texto (primer argumento, 30-39) y fondo (40-49) a tu elección.
pcolor.custom("La herramienta COLOR.CUSTOM te deja poner la combinación de color de texto y fondo que quieras, poniendo dos argumentos a el final del texto. Los colores de texto van de 30 a 39, y los de fondo de 40 a 49.",39,42)
print("")