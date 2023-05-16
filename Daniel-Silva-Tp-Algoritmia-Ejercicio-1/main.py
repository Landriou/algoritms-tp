from binarytree import *
from algo1 import *
from array import *
from random import *
from queue import *
#Ejercicio 1, Funcion que devuelve true si el string pasado como parametro tiene
#caracteres repetidos
def isUnique(S):
    largo = A_length(S)
    for i in range(largo):
        for j in range(largo):
            if i != j: #Si j e i son iguales ignoro la comparacion
                if S[i] == S[j]:
                    return True
    return False

#Prueba ejercicio 1
cadena = "hola"
cadena2 = "chaua"
print(isUnique(cadena))
print(isUnique(cadena2))
