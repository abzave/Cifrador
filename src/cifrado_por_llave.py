#Creado por: Abraham Meza Vega
#Fecha de creación: 3/4/18 11:30 p.m.
#Última modificación 6/4/18 11:30 a.m.
from alfabeto import *
from listas_y_strings import *

"""
Entradas: Palabra y clave de tipo string
Salidas: Posicion del caracter de la clave con el que se debe sumar el último
caracter de la palabra
Funcionamiento: Compara el tamaño de los strings y con base a eso calcula la
posicion del caracter de la clave que se debe sumar a la última letra de la
palabra
"""
def obtenerPosicionDeClave(palabra, clave):
	if len(palabra) > len(clave):
		return (len(palabra) - 1) % len(clave)
	else:
		return len(palabra) - 1

"""
Entradas: frase y clave de tipo string
Salidas: Mensaje codificado usando coidificación por llave
Funcionamiento: suma el valor de los caracteres de la frase y la clave y en caso
de que esta suma sea mayor a 26 se le resta este monto. Esto para luego retornar
el caracter con el valor resultante de estas operaciones
"""
def codificarPorLlave(frase, clave):
	posicionClave = obtenerPosicionDeClave(frase, clave)
	posicionFrase = alfabetoADigitos(frase[-1:]) + alfabetoADigitos(clave[posicionClave])
	if posicionFrase > 26:
		posicionFrase -= 26
	if len(frase) == 1:
		return digitosAAlfabeto(posicionFrase)
	else:
		return codificarPorLlave(frase[:-1], clave) + digitosAAlfabeto(posicionFrase)
"""
Entradas: frase y clave de tipo string
Salidas: Mensaje decodificado usando coidificación por llave
Funcionamiento: resta el valor de los caracteres de la frase y la clave, y en caso
de que esta suma sea menor a 0 se le suma este monto. Esto para luego retornar
el caracter con el valor resultante de estas operaciones
"""
def decodificarPorLlave(frase, clave):
	posicionClave = obtenerPosicionDeClave(frase, clave)
	posicionFrase = alfabetoADigitos(frase[-1:]) - alfabetoADigitos(clave[posicionClave])
	if posicionFrase < 0:
		posicionFrase += 26
	if len(frase) == 1:
		return digitosAAlfabeto(posicionFrase)
	else:
		return decodificarPorLlave(frase[:-1], clave) + digitosAAlfabeto(posicionFrase)

"""
Entradas: frase y clave de tipo string y accion de tipo entero
Salidas: lista con las palabras que conforman la frase descodificadas
Funcionamiento: convierte la frase en una lista con cada palabra una posicion y
devuelve un lista con estas palabras ya descodificadas(2) o codificadas(1) dependiendo
de acción
"""
def separarFrase(frase, clave, accion):
        if isinstance(frase, str):
                frase = frase.split()
        if len(frase) == 1:
                if accion == 1:
                        return [codificarPorLlave(frase[0], clave)]
                elif accion == 2:
                        return [decodificarPorLlave(frase[0], clave)]
        else:
                if accion == 1:
                        return separarFrase(frase[:-1], clave, accion) + [codificarPorLlave(frase[-1:][0], clave)]
                elif accion == 2:
                        return separarFrase(frase[:-1], clave, accion) + [decodificarPorLlave(frase[-1:][0], clave)]
                else:
                        return ["Error: Accion no valida"]

"""
Entradas: frase y clave de tipo string y accion de tipo int
Salidas: datos para la codificacion validados
Funcionamiento: pasa la frase y clave a minúsculas y comprueba que no tengan
caracteres diferentes a letra o espacios; además de que la clave no conste de
más de dos palabras. Según el parametro accion este llama a codificar(1) o
decodificar(2)
"""
def validarFraseYClave(frase, clave, accion):
        frase = pasarAMinusculas(frase)
        clave = pasarAMinusculas(clave)
        if caracteresNoAdmitidos(frase) or caracteresNoAdmitidos(clave):
                return ["Error: Debe ingresar valores con solo texto"]
        elif " " in clave:
                return ["Error: La clave debe ser de una sola palabra"]
        else:
                return listaAString(separarFrase(frase, clave, accion))
