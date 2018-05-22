"""
- Nombre: Jostin Tribeth Rivas Perez
- Carné: 2017097261
- Grupo: 3
- Curso: Taller de programación
"""
from listas_y_strings import revisarEnLista
from alfabeto import *

def cifrarTelefonico(frase):
    """
    Funcion: Toma un frase y la convierte en código telefónico
    Entradas: String(str) Frase a codificar
    Salidas: String(str) Frase convertida a código telefónico
    """
    if(len(frase)>0):
        if(frase[0] == " "):
            return "* " + cifrarTelefonico(frase[1:])
        else:
            letras = revisarEnLista(frase[0],abecedarioTelefonico)
            return str(abecedarioTelefonico.index(letras)+2)+str(letras.index(frase[0])+1)+" "+cifrarTelefonico(frase[1:])
    else:
        return ""

def descifrarTelefonico(frase):
    """
    Funcion: Toma una frase en codigo telefónico y lo convierte a una frase normal
    Entradas: String(str) Frase a decodificar
    Salidas: String(str) Frase convertida de código telefónico a frase normal
    """
    if(len(frase)>0):
        if(frase[0] == "*"):
            return " " + descifrarTelefonico(frase[1:])
        elif(frase[0] == " "):
            return descifrarTelefonico(frase[1:])
        else:
            return abecedarioTelefonico[int(frase[0])-2][(int(frase[1]))-1]+descifrarTelefonico(frase[2:])
    else:
        return ""

def validarTelefonico(frase):
    """
    Funcion: Comprueba que la frase sea un String y no contenga caracteres no contemplados
    Entradas: String(str) Frase a validar
    Salidas: Frase validada
    """
    if not(isinstance(frase, str)):
        return "Debe ingresar datos de tipo texto"
    elif not(tieneNumeros(frase)):
        return "El mensaje debe contener solo números o espacios"
    else:
        return descifrarTelefonico(frase)

        
