from node import StackNode as Node
from structureS import Structure


class Stack(Structure):
    ''' Class that describes a Stack '''

    def __init__(self):
        self._top = None
        self._size = 0

    def top(self):
        ''' Returns the value at the top of the stack '''
        if self._top:
            return self._top.data
        else:
            return "None"

    def clear(self):
        self._top = None
        self._size = 0

    def iter(self):
        ''' Brings the values of the stack'''
        current = self._top
        while current:
            data = current.data
            current = current.prev
            yield data

    def push(self, data):
        ''' Inserts a new element at the end of the queue '''
        node = Node(data)

        if self._top == None:
            self._top = node
        else:
            node.prev = self._top
            self._top = node

        self._size+=1

    def pop(self):
        ''' Deleted the last element in the queue '''
        top = self._top
        new_node = self._top.prev
        self._top = new_node
        self._size-=1
        
        return top.data
