from binarytree import *
from algo1 import *
from array import *
from random import *
from queue import *

def vectortotree(B,A):
    largo = A_length(A)
    contador = 0
    contador2 = 0
    if largo % 2 != 0:
        Arrayizquierda = Array(int(A_length(A)/2),0)
        Arrayderecha = Array(int(A_length(A)/2),0)
    else:
        Arrayizquierda = Array(int(A_length(A)/2),0)
        Arrayderecha = Array(int(A_length(A)/2)-1,0)
    bt_insert(B,A[int(largo/2)],A[int(largo/2)]) #Inserto el elemento del medio
    for i in range(int(largo/2)+1,len(A)):
        Arrayderecha[contador] = A[i]   #divido el array en izquierda y derecha
        contador = contador + 1
    for n in range(0,int(largo/2)):
        Arrayizquierda[contador2] = A[n]
        contador2 = contador2 + 1
    if len(Arrayderecha) != 0: #Caso base si el array esta vacio
        vectortotree(B,Arrayderecha) #Llamo a la recursividad con cada array 
    if len(Arrayizquierda) != 0:
        vectortotree(B,Arrayizquierda)


#Prueba ejercicio 2
B = BinaryTree()
vector = Array(10,0)
for n in range(len(vector)):
    vector[n] = n
vectortotree(B,vector)
imprimirlista(traverseBreadFirst(B))
