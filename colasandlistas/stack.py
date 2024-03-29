# FUENTES Bruno
# 12401


from algo1 import *
from linkedList import *



"""Ejercicio 1
         
Crear un modulo de nombre stack.py que implemente las siguientes especificaciones de las operaciones elementales para  un TAD pila  utilizando el TAD lista. Recordar que una Pila/stack puede implementarse también sobre una estructura LinkedList donde, el último elemento en ingresar a la lista es el primero en salir (LIFO).


push(S,element) 
Descripción: Agrega un elemento al comienzo de  S, siendo S una estructura de tipo  LinkedList 
Entrada: La pila S sobre la cual se quiere agregar el elemento (LinkedList)  y el valor del elemento (element) a  agregar.
Salida: No hay salida definida


pop(S)
Descripción: extrae el primer elemento de la pila S, siendo S una estructura de tipo LinkedList
Poscondición: Se debe desvincular el Node a eliminar.  
Entrada: la pila S (Linkedlist) sobre el cual se quiere realizar la eliminación 
Salida: Devuelve el elemento eliminado. Devuelve None si la pila esta vacia.
"""
def pushStack(S, element):
    insertLinkedlist(S, element, lengthLinkedList(S) ) 

def popStack(S):
    if lengthLinkedList(S) == 0 :
        return None
    else:
        posicion = lengthLinkedList(S) - 1
        elememto  = accessLinkedlist(S,posicion )
        deleteLinkedlist(S, elememto)
        return elememto