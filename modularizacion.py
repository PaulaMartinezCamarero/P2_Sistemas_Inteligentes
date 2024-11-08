#Autora: Paula Martínez Camarero

#MODULARIZACIÓN DE FUNCIONES:
#Tarea 1:

def crea_diccionario(ruta_archivo):
    """
    Esta función crea un diccionario que pone un indices para cada uno de los cuales asigna caracteres a partir de un archivo específico.


    Parámetros:
        - ruta_archivo: ruta en la que se encuentra el archivo

    Return:
        - diccionario: es un diccionario en el cual la clave es un indice y el valor es un caracter que se corresponde  con el valor ASCII del archivo claves-ascii
    """
    diccionario = {}
    #abrimos el archivo
    archivo=open(ruta_archivo)
    for i in archivo:
        indice = int( i.split()[0]) #el primer elemento de cada línea del archivo claves_ascii es el índice
        valor_ascii = int(i.split()[1]) #2ndo es el valor ASCII 
        caracter = chr(valor_ascii) #convertir el ascii a caracter
        diccionario[indice] = caracter #se mete en el diccionario el indice con su debido caracter
    return diccionario