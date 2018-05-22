"""
- Nombre: Jostin Tribeth Rivas Perez
- Carné: 2017097261
- Grupo: 3
- Curso: Taller de programación
"""
from alfabeto import *

def cifrarVigenere(frase,codigo,codigoM):
    """
    Funcion: Toma un frase y la convierte en código Vigenére
    Entradas: La clave debe ser un string, debe tener solo dos digitos, se debe ingresar la frase completamente en minusculas, luego la clave en reversa"reversa = codigo[1:]+codigo[:1]" y por ultimo la clave normal
    Salida: String(str) Frase convertida a código Vigenére
    """
    codigoR = codigo[1:]+codigo[:1]
    if(len(frase)>0):
        if(frase[0]==" "):
            return " " + cifrarVigenere(frase[1:],codigoM[1:]+codigoM[:1],codigoM)
        else:
            letra = alfabetoADigitos(frase[0])  + int(codigoR[0])
            return digitosAAlfabeto(letra)+cifrarVigenere(frase[1:],codigoR,codigoM)
    else:
        return ""

def descifrarVigenere(frase,codigo,codigoM):
    """
    Funcion: Toma una frase en codigo vigenere y lo convierte a una frase normal
    Entradas: Los parametros tienen el mismo orden que los de cifrado
    Salidas: String(str) Frase convertida de vigenere a frase normal
    """
    codigoR = codigo[1:]+codigo[:1]
    if(len(frase)>0):
        if(frase[0]==" "):
            return " " + descifrarVigenere(frase[1:],codigoM[1:]+codigoM[:1],codigoM)
        else:
            letra = alfabetoADigitos(frase[0])  - int(codigoR[0])
            return digitosAAlfabeto(letra)+descifrarVigenere(frase[1:],codigoR,codigoM)
    else:
        return ""

def validarVigenereCifrar(frase, codigo):
    """
    Funcion: Verifica que la frase y el codigo sean strings, que el codigo contenga 2 digitos y sean numericos y la frase no contenga caracteres no admitidos
    Entrads: La clave debe ser un string, debe tener solo dos digitos, se debe ingresar la frase, y la clave normal
    Salidas: Datos validados para la sustitución vigenére
    """
    if not(isinstance(frase, str)):
        return "Debe ingresar un mensaje de tipo texto"
    elif not(isinstance(codigo, str)):
        return "El código debe de ser de tipo texto"
    elif len(codigo) != 2:
        return "El código debe de constar de dos números"
    frase = pasarAMinusculas(frase)
    try:
        int(codigo)
    except:
        return "La cifra de constar de dos números"
    if caracteresNoAdmitidos(frase):
        return "Debe ingresar texto solo con letras o espacios"
    else:
        return cifrarVigenere(frase, codigo[::-1], codigo)

def validarVigenereDescifrar(frase, codigo):
    """
    Funcion: Verifica que la frase y el codigo sean strings, que el codigo contenga 2 digitos y sean numericos y la frase no contenga caracteres no admitidos
    Entrads: La clave debe ser un string, debe tener solo dos digitos, se debe ingresar la frase, y la clave normal
    Salidas: Datos validados para la sustitución vigenére
    """
    if not(isinstance(frase, str)):
        return ["Debe ingresar un mensaje de tipo texto"]
    elif not(isinstance(codigo, str)):
        return "El código debe de ser de tipo texto"
    elif len(codigo) != 2:
        return ["El código debe de constar de dos números"]
    else:
        return descifrarVigenere(frase, codigo[::-1], codigo)


