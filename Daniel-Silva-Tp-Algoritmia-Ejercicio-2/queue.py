from linkedlist import *



def enqueue(Q, element):
    add(Q,element)

def dequeue(Q):
    if length(Q) == 0:
        return None
    element = access(Q,length(Q)-1)
    deleteposition(Q, length(Q)-1)
    return element