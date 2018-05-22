#Creado por: Abraham Meza Vega
#Fecha de creación 16/4/18 9:45 p.m.
#Última modificación: 16/4/18 9:45 p.m.
from alfabeto import *

def validarGenericamente(frase, funcion):
    """
    Funcion: Valida que la frase sea un String y que no tenga caracteres no contemplados y retorna la funcion pasada
    Entradas: String(str) Frase a validar y funcion(function) función a la que se llamará
    Salidas: String(str) Frase Validado
    """
    if not(isinstance(frase, str)):
        return ["Debe ingresar datos de tipo texto"]
    frase = pasarAMinusculas(frase)
    if caracteresNoAdmitidos(frase):
        return ["Debe ingresar texto solo con letras o espacios"]
    else:
        return funcion(frase)
