#Creado por: Abraham Meza Vega
#Fecha de creación: 8/4/18 7:50 p.m.
#Última modifiación: 9/4/18 10:50 p.m.
import math

"""
Entradas: dos números de tipo entero
Salidas: True/False si los números dados son coprimos
Funcionamiento: Determina si dos números son coprimos basandose en la propiedad
que dice que el mcd de dos números coprimos es 1
"""
def sonCoprimos(numero1, numero2):
	if math.gcd(numero1, numero2) == 1:
		return True
	else:
		return False
"""
Entradas: número de tipo entero
Salidas: True/False si un número es primo
Funcionamiento: Utilizando el teorema de Wilson, que dice: "un número n es primo
si y solo si (n-1)! + 1 es múltiplo de n", se determina si un número es primo
"""
def esPrimo(numero):
        if abs(numero) == 1 or numero == 0:
                return False
        result = math.factorial(abs(numero) - 1) + 1
        if (result % numero) == 0:
                return True
        else:
                return False

"""
Entrada: número de tipo entero
Salidas: número primo más cercano al número ingresado
Funcionamiento: Comprueba si el número ingresado es primo, si no prueba con el
anterior de manera recursiva
"""
def primoMasCercano(numero):
        if esPrimo(numero):
                return abs(numero)
        else:
                return primoMasCercano(numero - 1)



