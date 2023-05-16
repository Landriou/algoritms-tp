from binarytree import *
from algo1 import *
from array import *
from random import *
from queue import *
#Funcion que devuelve una lista que contiene una lista por cada nivel del arbol binario
def lvltolists(B):
    if B.Root == None:
        return None
    QueueAux = LinkedList()
    Queue1 = LinkedList()
    enqueue(QueueAux,B.Root) #Meto la raiz en una cola aux

    while(length(QueueAux) != 0):#Voy sacando uno por uno de la cola auxiliar mientras meto en otra cola los hijos de cada uno y asi sucesivamente
        aux = dequeue(QueueAux)
        enqueue(Queue1,aux)
        if aux.Leftnode != None:
            enqueue(QueueAux,aux.Leftnode)
        if aux.Rightnode != None:
            enqueue(QueueAux,aux.Rightnode)
    Queue1 = inverse(Queue1)
    currentnode = Queue1.head       #Hasta aca es recorrido por amplitud
    Listadelistas = LinkedList()
    nivel = 0
    nextlvl = 0
    L = LinkedList()
    while currentnode != None:
        nivel = nodelvl(currentnode.value) #Saco el nivel del nodo
        if currentnode.nextNode != None:
            nextlvl = nodelvl(currentnode.nextNode.value) #Saco el nivel del proximo nodo
        else:
            nextlvl = nivel + 1
        add(L,currentnode.value) 
        if nextlvl > nivel: #Si el nivel del proximo es mayor, agrego la lista al conjunto
            add(Listadelistas, L) #Y creo una lista nueva
            L = LinkedList()
        currentnode = currentnode.nextNode
    return Listadelistas
        

def nodelvl(binarynode):
    contador = 0
    puntero = binarynode
    if binarynode == None:
        return None
    while binarynode.Parent != None:
        contador = contador + 1
        binarynode = binarynode.Parent
    binarynode = puntero
    return contador

#Prueba ejercicio 3
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

Listadelistas = lvltolists(B2)
lista = Listadelistas.head
while lista != None:
    print("")
    imprimirlistanodes(lista.value)
    lista = lista.nextNode
