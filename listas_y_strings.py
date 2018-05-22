#Creado por: Abraham Meza Vega y Tribeth Rivas Perez
#Fecha de creación: 6/4/18 11:45 a.m.
#Última modificación: 9/4/18 1:00 p.m.

"""
Entradas: lista de tipo lista de strings
Salidas: string con los elementos de la lista separados por espacio
Funcionamiento: recorre la lista la convierte en un string y agrega espacios
entre elementos
"""
def listaAString(lista):
	if len(lista) == 1:
		return "".join(lista)
	else:
		return listaAString(lista[:-1]) + " " + "".join(lista[-1:])

def revisarEnLista(caracter,lista):
    """
    Funcion: La funcion busca en una lista de strings el bloque en el que se encuentra el caracter
    Entradas: Se le pasa por parametro un caracter(char) y una lista de strings(list[]) 
    Salidas: String(str) string perteneciente a la lista en el cual exisitia el caracter que se buscaba
    """
    if(caracter in lista[0]):
        return lista[0]
    else:
        return revisarEnLista(caracter,lista[1:])
