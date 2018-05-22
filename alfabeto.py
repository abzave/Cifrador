#Creado por: Abraham Meza Vega y Tribeth Rivas Perez
#Fecha de creación: 3/4/18 10:20 p.m.
#Última modificación: 9/4/18 1:00 p.m.
import string

#Valores del alfabeto en código binario
alfabetoBinario = {" ":"*", "a":"00000", "b":"00001", "c":"00010", "d":"00011", "e":"00100", "f":"00101", "g":"00110", "h":"00111", "i":"01000", "j":"01001", "k":"01010", "l":"01011", "m":"01100", "n":"01101", "o":"01110", "p":"01111", "q":"10000", "r":"10001", "s":"10010", "t":"10011", "u":"10100", "v":"10101", "w":"10110", "x":"10111", "y":"11000", "z":"11001"}
#Abecedario del cifrado César y normal
abecedario = "abcdefghijklmnopqrstuvwxyz"
abecedarioCesar = "defghijklmnopqrstuvwxyzabc"
#Abecedario del cifrado telefonico
abecedarioTelefonico = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def alfabetoADigitos(letra):
    """
    Entradas: Letra de tipo caracter
    Salidas: Digitos correspondientes a la letra
    Funcionamiento: Busca en la constante ascii_lowercase de la clase string de
    Python y retorna su posición más uno
    """
    digito = string.ascii_lowercase.find(letra) + 1
    if digito == 0:
        return " "
    else:
        return digito

def digitosAAlfabeto(digito):
    """
    Entradas: digito de tipo entero
    Salidas: Letra correspondiente al digito ingresado
    Funcionamiento: Busca en la constante ascii_lowercase de la clase string de
    Python y retorna la letra en la posición del digito menos 1 o espacio
    """
    letra = string.ascii_lowercase[digito - 1]
    if digito == 0:
        return " "
    else:
        return letra

def pasarAMinusculas(texto):
    """
    Entradas: Texto de tipo string
    Salidas: String ingresado con todas las letras en minúsculas
    Funcionamiento: Usa el metodo lower para pasar todas las letras mayúsculas de un
    string a minúsculas
    """
    return texto.lower()

"""
Entradas: frase de tipo string
Salidas: Devuelve si un string contiene al menos un caracter diferente a una
letra, con la excepción del espacio
Funcionamiento: Recorre el string en busca de algún caracter no admitido y en
caso de encontrarlo retorna True, de lo contrario False
"""
def caracteresNoAdmitidos(frase):
	if len(frase) == 1:
		return not(frase in string.ascii_lowercase or frase == " ")
	elif not(frase[-1:] in string.ascii_lowercase or frase[-1:] == " "):
		return True
	else:
		return caracteresNoAdmitidos(frase[:-1])

"""
Entradas: string de tipo string
Salidas: Devuelve si un string contiene al menos un caracter diferente a una
letra, con la excepción del espacio
Funcionamiento: Recorre el string en busca de algún caracter no admitido y en
caso de encontrarlo retorna True, de lo contrario False
"""
def tieneNumeros(frase):
	if len(frase) == 1:
		return frase.isnumeric() or frase == " "
	elif frase[-1:].isnumeric() or frase[-1:] == " ":
		return True
	else:
		return tieneNumeros(frase[:-1])
"""
Entradas: letra de tipo caracter
Salidas: letra codificadado en binario
Funcionamiento: Busca en el diccionario definido previamente el valor en codigo
binario de la letra ingresada. En caso de no encontrarla regresa error
"""
def alfabetoABinario(letra):
    try:
        return alfabetoBinario[letra]
    except:
        return "Error: La letra a codificar no se ha encontrado"

"""
Entradas: binario de tipo string
Salidas: la letra que representa el código ingresa o error en caso de no haber
dicha letra
Funcionamiento: Busca en una lista con todas las letras una posición dada por
la posicion del codigo en una lista con todos los valores binarios y en caso de
no estar retorna error
"""
def binarioAAlfabeto(binario):
	try:
		return list(alfabetoBinario.keys())[list(alfabetoBinario.values()).index(binario)]
	except:
		return "Error: El digito a decodificar no se ha encontrado "
