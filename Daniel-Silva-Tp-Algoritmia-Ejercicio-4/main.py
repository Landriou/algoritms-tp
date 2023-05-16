from binarytree import *
from algo1 import *
from array import *
from random import *
from queue import *

#Ejercicio 4 funcion que devuelve true si el arbol esta balanceado
def Isbalanced(B):
    if B.Root == None:
        return None
    contadorizq = 0
    contadorder = 0
    if B.Root.Leftnode != None:
        contadorizq = traverseBalanced(B.Root.Leftnode,contadorizq) #Cuento por recursividad los nodos del arbol derecho
    else:
        contadorizq = 0
    if B.Root.Rightnode != None:
        contadorder = traverseBalanced(B.Root.Rightnode, contadorder) #Lo mismo con el izquierdo
    else:
        contadorder = 0
    if contadorder == contadorizq:
        return True
    else:
        return False
def traverseBalanced(currentnode,contador):
    
    if currentnode.Leftnode != None:
        contador = traverseBalanced(currentnode.Leftnode,contador +1 )
    if currentnode.Rightnode != None:
        contador = traverseBalanced(currentnode.Rightnode,contador + 1)
    return contador

B2 = BinaryTree()
bt_insert(B2,"A",10)
bt_insert(B2,"B",5)
bt_insert(B2,"D",3)
bt_insert(B2,"H",1)
bt_insert(B2,"I",4)
bt_insert(B2,"E",7)
bt_insert(B2,"J",6)
bt_insert(B2,"K",8)
bt_insert(B2,"C",15)
bt_insert(B2,"F",13)
bt_insert(B2,"L",11)
bt_insert(B2,"M",14)
bt_insert(B2,"G",18)
bt_insert(B2,"N",16)
bt_insert(B2,"O",20)
B = BinaryTree()
bt_insert(B,1,3)
bt_insert(B,1,2)
bt_insert(B,1,1)
print(Isbalanced(B))
print(Isbalanced(B2))