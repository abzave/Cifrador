#Creado por: Abraham Meza Vega y Tribeth Rivas Perez
#Fecha de creación: 8/4/18 6:10 p.m.
#Última modificación: 9/4/18 10:50 p.m.
import random
import time
import sys
from Primos import *
sys.setrecursionlimit(16384)

def generarPrimos():
    """
    Entradas: No requiere entradas
    Salidas: Número primo generado aleatoriamente
    Funcionamiento: Con base en un Random Number Generator (RNG) se obtiene un
    número y caso de no se primo se devuelve el primo más cercano
    """
    rng = random.SystemRandom(time.time())
    primo = rng.randint(2, 2**6)
    if not(esPrimo(primo)):
        primo = primoMasCercano(primo)
    return primo

def calcularN():
    """
    Entadas: No requiere entradas
    Salidas: número n que será parte de la clave privada/pública
    Funcinamiento: Genera dos número primos y los multiplica para dar como
    resultado n
    """
    p = generarPrimos()
    q = generarPrimos()
    return p * q

def calcularE(n):
    """
    Entradas: N de tipo entero
    Salidas: E para cifrar por RSA
    Funcionamiento: Genera un número; luego verifica que este cumpla las
    condiciones para ser el exponente público y lo retorna, de lo contrario lo
    vuelve a intentar
    """
    e = random.randint(1, phiEuler(n, n))
    if eRSA(e, n):
        return e
    else:
        return calcularE(n)

def phiEuler(n,n2):
    """
    Funcion: La funcion retorna el numero de enteros positivos menores o iguales a "n" y coprimos con "n"
    Entradas: Se debe pasar a "n" y "n2" como numeros iguales
    Salidas: Número de enteros positivos menores o iguales a "n" y coprimos con "n"
    """
    if(n2==0):
        return 0
    else:
        if(sonCoprimos(n,n2)):
            return 1+phiEuler(n,n2-1)
        elif(esPrimo(n)):
            return n-1
        else:
            return phiEuler(n,n2-1)

#Se debe pasar a "e" y "n2" como numeros iguales
#El número que retorna será dado a conocer como exponente de la clave pública        
def eRSA(e,n):
    """
    Funcion: La funcion retorna verdadero(True) si "e" es un numero menor que phi de n  y coprimo con phi de n si no retorna falso(False)
    Entradas: Enteros(int) "e" y "n"
    Salidas: Booleano(bool)
    """
    phi = phiEuler(n,n)
    if (e<phi and sonCoprimos(e,phi)):
        return True
    else:
        return False

def dRSA(e,phiN,phiN2):
    """
    Funcion: La funcion retorna "d" del RSA 
    Entradas: Enteros(int)"phiN" es el phi de "n", "e" es el "e" del RSA y "phiN2" se tiene que ingresar con el mismo valor de "phiN"
    Salidas: Entero(int) Número D en RSA
    """
    if(phiN2 == 0):
        return
    else:
        if (((phiN2*e)-1)%phiN)==0:
            return phiN2
        else:
            return dRSA(e,phiN,phiN2-1)

def cifrarRSA(texto,n,e):
    """
    Funcion: Toma un frase y la convierte en código RSA
    Entradas: String(str) Texto que se quiere cifrar, Enteros(int) "N" y "E" pertenecientes al código RSA
    Salida: String(str) Frase convertida a código RSA
    """
    phi = phiEuler(n,n)
    return retornarCifradoRSA(texto,e,n)

def retornarCifradoRSA(texto,e,n):
    """
    Funcion: Toma un frase y la convierte en código RSA
    Entradas: String(str) Texto que se quiere cifrar, Enteros(int) "N" y "E" pertenecientes al código RSA
    Salida: String(str) Frase convertida a código RSA
    """
    if(len(texto) == 0):
        return ""
    elif(len(texto) == 1):
        return str((ord(texto[0])**e)%n)+ retornarCifradoRSA(texto[1:],e,n)
    else:
        return str((ord(texto[0])**e)%n)+"*"+ retornarCifradoRSA(texto[1:],e,n)

def descifrarRSA(texto,n,d):
    """
    Funcion: Toma una frase en codigo RSA y lo convierte a una frase normal
    Entradas: String(str) Texto que se quiere descifrar, Enteros(int) "N" y "D" pertenecientes al código RSA
    Salidas: String(str) Frase convertida de código RSA a frase normal
    """
    return retornarDescifradoRSA(texto.split("*"),d,n)

def retornarDescifradoRSA(texto,d,n):
    """
    Funcion: Toma una frase en codigo RSA y lo convierte a una frase normal
    Entradas: String(str) Texto que se quiere descifrar, Enteros(int) "N" y "D" pertenecientes al código RSA
    Salidas: String(str) Frase convertida de código RSA a frase normal
    """
    if(len(texto) == 0):
        return ""
    else:
        return chr((int(texto[0])**d)%n)+ retornarDescifradoRSA(texto[1:],d,n)
