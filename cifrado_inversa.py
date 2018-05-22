#Creado por: Abraham Meza Vega
#Fecha de creación: 6/4/18 11:20 a.m.
#Última modificación: 6/4/18 12:00 p.m.
from listas_y_strings import *

"""
Entradas: palabra de tipo string
Salidas: palabra invertida
Funcionamiento: invierte la palabra para aplicar una codificación por palabra
inversa
"""
def cifrarInversa(palabra):
	return palabra[::-1]
#Nota: Esta función codifica y decodifica palabra y mensaje inverso

"""
Entradas: frase de tipo string
Salidas: lista con las palabras que conforman la frase codificadas
Funcionamiento: convierte la frase en una lista con cada palabra una posicion y
devuelve un lista con estas palabras ya codificadas
"""
def separarFraseInv(frase):
        if isinstance(frase, str):
                frase = frase.split()
        if len(frase) == 1:
                return cifrarInversa(frase[0])
        else:
                return separarFraseInv(frase[:-1]) + " " + cifrarInversa(frase[-1:][0])
