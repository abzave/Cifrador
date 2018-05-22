#Creado por: Abrham Meza Vega
#Fecha de creación: 8/4/18 2:10 p.m.
#Última modificación: 8/4/18 3:10 p.m.
from alfabeto import *

#Simbolos binarios
simbolosBinarios = ["1", "0", "*", " "]

"""
Entradas: frase de tipo string
Salidas: la frase ingresada codificada usando cifrado binario
Funcionamiento: pasa cada letra de la frase ingresada a su respectivo código
binario
"""
def codificarBinario(frase):
    if len(frase) == 1:
        return alfabetoABinario(frase)
    else:
        return codificarBinario(frase[:-1]) + " " + alfabetoABinario(frase[-1:])

"""
Entradas: frase de tipo lista de strings
Salidas: string con el contenido de la frase decodificado
Funcionamiento: recorre las lista dada y, mientras hace esto, convierte el
último elemento en su letra correspondiente
"""
def decodificarBinario(frase):
    letra = binarioAAlfabeto(frase[-1:][0])
    if len(letra) > 1:
        print(letra)
        return
    elif len(frase) == 1:
        return letra
    else:
        resultado = decodificarBinario(frase[:-1])
        if resultado == None:
            return
        else:
            return resultado + letra

"""
Entradas: frase de tipo string
Salidas: True/False si un string contiene solo los caracteres 0, 1, * o espacio
Funcionamiento: Verifica si a un string se le puede aplicar una decodificacion
binaria
"""
def esBinario(frase):
	if len(frase) == 1 and frase in simbolosBinarios:
		return True
	elif len(frase) > 1 and frase[-1:] in simbolosBinarios:
		return esBinario(frase[:-1])
	else:
		return False
"""
Entradas: frase de tipo string
Salidas: frase validada
Funcionamiento: Revisa que la frase solo conste de caracteres que se puedan
decodificar
"""
def validarBinario(frase):
	if not(esBinario(frase)):
		return "Error: El mensaje solo puede contener 0, 1, * o espacios"
	else:
		return decodificarBinario(frase.split())
