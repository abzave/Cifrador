#Creado por: Abrham Meza y Tribeth Rivas
#Fecha de creación: 9/4/18 11:00 a.m.
#Última modificación: 9/4/18 2:20 p.m.
#Versión: 3.6.4

#Importaciones
import getpass
from Correos import *
from sustitucion_vigenere import *
from cifrado_por_llave import *
from RSA import *

#Definición de funciones
"""
Entradas: Pide al usuario el mensaje a cifrar
Salidas: confirmación/error de que se ha enviado el correo
Funcionamiento: Le pide al usuario un mensaje para cifrar, si la validación de
este no es exisitosa returna el mensaje de error, sino envia un correo con el
mensaje cifrado
"""
def opcionCesar():
    frase = input("Ingrese el mensaje a cifrar: ")
    resultado = validarGenericamente(frase, cifrarCesar)
    if isinstance(resultado, list):
        print(resultado[0])
        return opcionCesar()
    else:
        print(enviarCorreo(correo, contrasenna, resultado, 1))
        return

"""
Entradas: Pide al usuario el mensaje y la llave para cifrar
Salidas: confirmación/error de que se ha enviado el correo
Funcionamiento: Le pide al usuario un mensaje para cifrar, si la validación de
este no es exisitosa returna el mensaje de error, sino envia un correo con el
mensaje cifrado
"""
def opcionPorLlave():
    frase = input("Ingrese el mensaje a cifrar: ")
    clave = input("Ingrese la llave de cifrado: ")
    resultado = validarFraseYClave(frase, clave, 1)
    if isinstance(resultado, list):
        print(resultado[0])
        return opcionPorLlave()
    else:
        print(enviarCorreo(correo, contrasenna, resultado, 2))
        return

"""
Entradas: Pide al usuario el mensaje y la cifra para cifrar
Salidas: confirmación/error de que se ha enviado el correo
Funcionamiento: Le pide al usuario un mensaje para cifrar, si la validación de
este no es exisitosa returna el mensaje de error, sino envia un correo con el
mensaje cifrado
"""
def opcionVigenere():
    frase = input("Ingrese el mensaje a cifrar: ")
    cifra = input("Ingrese la cifra para la codificación: ")
    resultado = validarVigenereCifrar(frase, cifra)
    if isinstance(resultado, list):
        print(resultado[0])
        return opcionVigenere()
    else:
        print(enviarCorreo(correo, contrasenna, resultado, 3))
        return

"""
Entradas: Pide al usuario el mensaje para cifrar
Salidas: confirmación/error de que se ha enviado el correo
Funcionamiento: Le pide al usuario un mensaje para cifrar, si la validación de
este no es exisitosa returna el mensaje de error, sino envia un correo con el
mensaje cifrado
"""
def opcionPalabraInv():
    frase = input("Ingrese el mensaje a cifrar: ")
    print(enviarCorreo(correo, contrasenna, separarFraseInv(frase), 4))
    return

"""
Entradas: Pide al usuario el mensaje para cifrar
Salidas: confirmación/error de que se ha enviado el correo
Funcionamiento: Le pide al usuario un mensaje para cifrar, si la validación de
este no es exisitosa returna el mensaje de error, sino envia un correo con el
mensaje cifrado
"""
def opcionMensajeInv():
    frase = input("Ingrese el mensaje a cifrar: ")
    print(enviarCorreo(correo, contrasenna, cifrarInversa(frase), 5))
    return

"""
Entradas: Pide al usuario el mensaje para cifrar
Salidas: confirmación/error de que se ha enviado el correo
Funcionamiento: Le pide al usuario un mensaje para cifrar, si la validación de
este no es exisitosa returna el mensaje de error, sino envia un correo con el
mensaje cifrado
"""
def opcionTelefonico():
    frase = input("Ingrese el mensaje a cifrar: ")
    resultado = validarGenericamente(frase, cifrarTelefonico)
    if isinstance(resultado, list):
        print(resultado)
        return opcionTelefonico()
    else:
        print(enviarCorreo(correo, contrasenna, resultado, 6))
        return

"""
Entradas: Pide al usuario el mensaje para cifrar
Salidas: confirmación/error de que se ha enviado el correo
Funcionamiento: Le pide al usuario un mensaje para cifrar, si la validación de
este no es exisitosa returna el mensaje de error, sino envia un correo con el
mensaje cifrado
"""
def opcionBinario():
    frase = input("Ingrese el mensaje a cifrar: ")
    resultado = validarGenericamente(frase, codificarBinario)
    if isinstance(resultado, list):
        print(resultado[0])
        return opcionBinario()
    else:
        print(enviarCorreo(correo, contrasenna, resultado, 7))
        return

def opcionRSA():
    """
    Entradas: Pide al usuario el mensaje a cifrar, le pregunta si tiene clave
    de encriptación y se la pide
    Salidas: Mensaje de confirmación/Error de que se envio el correo
    Funcionamiento: Pide el usuario el mensaje a cifrar, le pregunta  si tiene
    clave de encriptación de ser así se la pide, de lo contrario, la genera y por último,
    envia el correo
    """
    frase = input("Ingrese el mensaje a cifrar: ")
    try:
        opcion = int(input("1)Sí\n2)No\n¿Tiene clave de encriptación?: "))
    except:
        print("Error: Debe ingresa 1 para sí y 2 para no.")
        return opcionRSA()
    if opcion == 1:
        try:
            e = int(input("Ingrese e: "))
            n = int(input("Ingrese n: "))
        except:
            print("Error: Debe ingresar los valores n y e de su clave pública.")
            return opcionRSA()
    elif opcion == 2:
        n = calcularN()
        e = calcularE(n)
        d = dRSA(e, phiEuler(n, n), phiEuler(n, n))
        print("Su clave pública es n =", n, " y e =", e, " y su clave privada: d es =", d, "y n =", n)
    else:
        print("Error: Debe ingresa 1 para sí y 2 para no.")
    print(enviarCorreo(correo, contrasenna, retornarCifradoRSA(frase, e, n), 8))
    return

"""
Entradas: Pide al usuario los datos necesarios para el descrifrado
Salidas: Datos ingresados por el usuario
Funcionamiento: Según el código de encriptación usado se pide al usuario los
datos necesarios para descifrar el mensajes.
"""
def pedirDatos(codigo):
    if codigo == 2:
        llave = input("Ingrese la llave para el descifrado: ")
        return llave
    elif codigo == 3:
        cifra = input("Ingrese la cifra para decodificar: ")
        return cifra
    elif codigo == 8:
        try:
            n = int(input("Ingrese n de su clave privada: "))
            d = int(input("Ingrese d de su clave privada: "))
        except:
            return ["Error: Debe de ingresar los datos de su clave privada"]
        return str(n) + " " + str(d)
    else:
        return ["Error: El codigo ingresado no corresponde a un algoritmo valido"]

"""
Entradas: Mensaje y datos de tipo string y codigo de tipo entero
Salidas: Mensaje descifrado/Error
Funcionamiento: Según el código de encriptación llama al algoritmo necesario
para descifrar ese mensaje.
"""
def descifrar(mensaje, datos, codigo):
    if codigo == 2:
        return validarFraseYClave(mensaje[:-5], datos, 2)
    elif codigo == 3:
        return validarVigenereDescifrar(mensaje[:-5], datos)
    elif codigo == 8:
        datos = datos.split()
        return descifrarRSA(mensaje[:-5], int(datos[0]), int(datos[1]))
    else:
        return "Error: El codigo ingresado no corresponde a un algoritmo valido"

"""
Entradas: No requiere entradas
Salidas: Función de cifrado seleccionada
Funcionamiento: Imprime los algoritmos de cifrado, pide una opción y llama a la
función seleccionada
"""
def menuCifrado():
    print("\nSeleccione una opción: ")
    print("1) Cifrado César")
    print("2) Cifrado por llave")
    print("3) Sustición Vigenére")
    print("4) RSA")
    print("5) palabra inversa")
    print("6) mensaje inverso")
    print("7) Cifrado telefonico")
    print("8) Cifrado binario")
    print("9) Volver")
    try:
        opcion = int(input("Ingrese el número de la opción que desea seleccionar: "))
    except:
        print("Error: Debe ingresar un número del 1 al 9")
        return menuCifrado()
    if opcion == 1:
        opcionCesar()
    elif opcion == 2:
        opcionPorLlave()
    elif opcion == 3:
        opcionVigenere()
    elif opcion == 4:
        opcionRSA()
    elif opcion == 5:
        opcionPalabraInv()
    elif opcion == 6:
        opcionMensajeInv()
    elif opcion == 7:
        opcionTelefonico()
    elif opcion == 8:
        opcionBinario()
    elif opcion == 9:
        return
    else:
        print("Error: Debe ingresar un número del 1 al 9")
        return menuCifrado()
    return

"""
Entradas: N/A
Salidas: Mensaje del último correo descifrado
Funcionamiento: recupera el último correo, analiza el cifrado de este y en caso
de no requerir datos adicionales imprime el mensaje y de lo contrario llama a la
función correspondiente
"""
def menuDescifrado():
    resultado = recuperarCorreo(correo, contrasenna)
    mensaje = analizarCorreo(resultado)
    if isinstance(mensaje, int):
        datos = pedirDatos(mensaje)
        if isinstance(datos, list):
            print(datos[0])
            return menúDescifrado()
        else:
            print("Mensaje: ", descifrar(resultado, datos, mensaje))
    else:
        print("Mensaje: ", mensaje)
    return

"""
Entradas: No requiere entradas
Salidas: Submenú que el usuario escogió o finalización del programa
Funcionamiento: Presenta al usuario una serie de opciones y pide que escoja una
de estas
"""
def menuPrincipal():
    print("\nSeleccione una opción:")
    print("1) Cifrado")
    print("2) Descifrado")
    print("3) Salir")
    try:
        opcion = int(input("Ingrese el número de la opción que desea seleccionar: "))
    except:
        print("Error: Debe ingresar un dígito del 1 al 3\n")
        return menuPrincipal()
    if opcion == 1:
        menuCifrado()
    elif opcion == 2:
        menuDescifrado()
    elif opcion == 3:
        return
    else:
        print("Error: Debe ingresar un número del 1 al 3 \n")
    return menuPrincipal()

"""
Entradas: Correo de tipo string
Salidas: Correo validado
Funcionamiento: Verifica que el correo dado sea valido en caso contrario lo pide
indefinidamente hasta que sea valido
"""
def corregirCorreo(correo):
    resultado = validarCorreo(correo)
    if isinstance(resultado, str):
        print(resultado)
        correo = input("Ingrese la cuenta de correo con la que desea trabajar: ")
        return corregirCorreo(correo)
    else:
        return correo

#Programa principal
correo = input("Ingrese la cuenta de correo con la que desea trabajar: ")
correo = corregirCorreo(correo)
contrasenna = getpass.getpass("Ingrese la contraseña del correo: ")
menuPrincipal()
