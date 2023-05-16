from algo1 import *
def A_search(array, element):
    indice = None
    for n in range(len(array)):
        if array[n]== element:
            indice = n
            return indice
    return None
    
def A_insert(array, element, position):
    vector = Array(len(array), 0)
    for i in range(len(array)):
        vector[i] = array[i]        #Copio el array
    
    if position >= len(array):  
        return None
    if position == len(vector)-1:
        array[position] = element
        return search(array, element)
        
    for n in range(len(vector)):
        if n != len(vector)-1:
            array[n+1] = vector[n]  
     
    array[position] = element
    return search(array, element)

def A_delete(array, element):
    vector = Array(len(array), 0)
    for i in range(len(array)):
        vector[i] = array[i]
    position = search(array, element)
        
    if position == None:
        return None
        
    for n in range(position,len(vector)):
        if n != len(vector)-1:
            array[n] = vector[n+1]  
        else:
            array[n] = None
    return position   

def A_length(array):
    cantdistnone = 0
    for n in range(len(array)):
        if array[n] != None :
            cantdistnone = cantdistnone + 1
    return cantdistnone