"""
- Nombre: Jostin Tribeth Rivas Perez
- Carné: 2017097261
- Grupo: 3
- Curso: Taller de programación
"""
from alfabeto import *

#cesar esta funcion depende de las dos variables globales abecedario y abecedario cesar pero tambien puede usarse recorrerAbecedario solo que consume más recursos
def cifrarCesar(frase):
    """
    Funcion: Toma un frase y la convierte en código Cesar
    Entradas: String(str) Frase a codificar
    Salidas: String(str) Frase convertida a código Cesar
    """
    if(len(frase)>0):
        if(frase[0] == " "):
            return " " + cifrarCesar(frase[1:])
        else:
            return abecedarioCesar[abecedario.index(frase[0])]+ cifrarCesar(frase[1:])
    else:
        return ""

def descifrarCesar(frase):
    """
    Funcion: Toma una frase en codigo Cesar y lo convierte a una frase normal
    Entradas: String(str) Frase a decodificar
    Salidas: String(str) Frase convertida de código Cesar a frase normal
    """
    if(len(frase)>0):
        if(frase[0] == " "):
            return " " + descifrarCesar(frase[1:])
        else:
            return abecedario[abecedarioCesar.index(frase[0])]+ descifrarCesar(frase[1:])
    else:
        return ""

